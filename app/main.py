from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from app.services.parking_service import (get_parking_status, calculate_move_by, calculate_reminder_at,)

app = FastAPI()

class ParkingEvent(BaseModel):
    latitude: float
    longitude: float
    parked_at: datetime

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/parking")
def create_parking_event(event: ParkingEvent):
    parking_status = get_parking_status(event.parked_at)
    move_by = calculate_move_by(event.parked_at)
    reminder_at = calculate_reminder_at(move_by)

    return {
        "message": "Parking event received",
        "latitude": event.latitude,
        "longitude": event.longitude,
        "parking_status": parking_status,
        "move_by": move_by,
        "reminder_at": reminder_at,

    }


