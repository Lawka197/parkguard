from __future__ import annotations

from datetime import datetime
from datetime import timedelta


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
def calculate_move_by(parked_at: datetime) -> datetime | None:
    weekday = parked_at.weekday()
    hour = parked_at.hour

    if weekday <= 4:
        if hour < 12:
            return parked_at.replace(
                hour=12,
                minute=0,
                second=0,
                microsecond=0
            )

        if 12 <= hour < 18:
            return parked_at.replace(
                hour=18,
                minute=0,
                second=0,
                microsecond=0
            )

        if weekday == 4:
            days_until_monday = 3
            next_restriction = parked_at + timedelta(days=days_until_monday)
        else:
            next_restriction = parked_at + timedelta(days=1)

        return next_restriction.replace(
            hour=12,
            minute=0,
            second=0,
            microsecond=0
        )

    if weekday == 5:
        next_restriction = parked_at + timedelta(days=2)

    else:
        next_restriction = parked_at + timedelta(days=1)

    return next_restriction.replace(
        hour=12,
        minute=0,
        second=0,
        microsecond=0
    )

def calculate_reminder_at(move_by: datetime) -> datetime:
    return move_by - timedelta(hours=1)

