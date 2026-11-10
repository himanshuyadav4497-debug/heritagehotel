from datetime import date
from flask import Blueprint, jsonify, request, render_template, current_app
from sqlalchemy.exc import SQLAlchemyError

from . import db
from .models import Booking

api = Blueprint("api", __name__)

@api.get("/")
def index():
    return render_template("index.html")

@api.get("/health")
def health():
    try:
        db.session.execute(db.text("SELECT 1"))
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except SQLAlchemyError:
        return jsonify({"status": "unhealthy", "database": "unavailable"}), 503

@api.post("/api/bookings")
def create_booking():
    payload = request.get_json(silent=True) or {}
    required = ("guest_name", "email", "check_in", "check_out")
    missing = [key for key in required if not payload.get(key)]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400
    try:
        check_in = date.fromisoformat(payload["check_in"])
        check_out = date.fromisoformat(payload["check_out"])
        guests = int(payload.get("guests", 1))
    except (ValueError, TypeError):
        return jsonify({"error": "Dates must use YYYY-MM-DD and guests must be an integer"}), 400
    if check_out <= check_in:
        return jsonify({"error": "check_out must be after check_in"}), 400
    if guests < 1 or guests > 12:
        return jsonify({"error": "guests must be between 1 and 12"}), 400
    email = str(payload["email"]).strip()
    if "@" not in email or "." not in email.split("@")[-1]:
        return jsonify({"error": "A valid email address is required"}), 400
    booking = Booking(
        guest_name=str(payload["guest_name"]).strip()[:120],
        email=email[:254],
        check_in=check_in,
        check_out=check_out,
        guests=guests,
        message=str(payload.get("message", ""))[:1000]
    )
    try:
        db.session.add(booking)
        db.session.commit()
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Could not save booking"}), 500
    return jsonify({
        "message": "Enquiry received",
        "booking": {
            "id": booking.id,
            "guest_name": booking.guest_name,
            "check_in": booking.check_in.isoformat(),
            "check_out": booking.check_out.isoformat(),
            "guests": booking.guests
        }
    }), 201

@api.get("/api/bookings")
def list_bookings():
    # Demo endpoint: protect with authentication before any public production use.
    records = Booking.query.order_by(Booking.created_at.desc()).limit(100).all()
    return jsonify([{
        "id": b.id, "guest_name": b.guest_name, "email": b.email,
        "check_in": b.check_in.isoformat(), "check_out": b.check_out.isoformat(),
        "guests": b.guests
    } for b in records]), 200
