from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from app.services.parking_service import get_parking_status

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

    return {
        "message": "Parking event received",
        "latitude": event.latitude,
        "longitude": event.longitude,
        "parked_status": parking_status

    }


