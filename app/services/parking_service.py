from datetime import datetime


def get_parking_status(parked_at: datetime) -> dict:
    weekday = parked_at.weekday()

    return{
        "weekday": weekday,
        "parked_at": parked_at
    }