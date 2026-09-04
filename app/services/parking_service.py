from datetime import datetime


def get_parking_status(parked_at: datetime) -> dict:
    weekday = parked_at.weekday()
    hour = parked_at.hour

    is_weekday = weekday <= 4
    is_restricted_time = 12 <= hour < 18

    allowed = not (is_weekday and is_restricted_time)

    return{
        "weekday": weekday,
        "parked_at": parked_at,
        "allowed": allowed
    }