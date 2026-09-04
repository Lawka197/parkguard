from datetime import datetime

from app.services.parking_service import get_parking_status, calculate_move_by, calculate_reminder_at


def test_weekday_before_restriction():
    parked_at = datetime(2026, 9, 4,10,0)

    result = get_parking_status(parked_at)
    assert result["allowed"] is True

def test_weekday_during_restriction():
    parked_at = datetime(2026, 9, 4, 13, 0)

    result = get_parking_status(parked_at)
    assert result["allowed"] is False

def test_weekday_after_restriction():
    parked_at = datetime(2026, 9, 4, 19, 0)

    result = get_parking_status(parked_at)
    assert result["allowed"] is True

def test_weekend_during_restriction():
    parked_at = datetime(2026, 9, 5, 13, 0)

    result = get_parking_status(parked_at)
    assert result["allowed"] is True

def test_weekday_at_restriction_start_is_not_allowed():
    parked_at = datetime(2026, 9, 4, 12, 0)

    result = get_parking_status(parked_at)
    assert result["allowed"] is False

def test_weekday_at_restriction_end_is_allowed():
    parked_at = datetime(2026, 9, 4, 18, 0)

    result = get_parking_status(parked_at)
    assert result["allowed"] is True

def test_monday_evening_moves_by_tuesday_noon():
    parked_at = datetime(2026, 9, 7, 20, 0)

    move_by = calculate_move_by(parked_at)

    assert move_by == datetime(2026, 9, 8, 12, 0)

def test_friday_evening_moves_by_monday_noon():
    parked_at = datetime(2026, 9, 4, 20, 0)

    move_by = calculate_move_by(parked_at)

    assert move_by == datetime(2026, 9, 7, 12, 0)

def test_reminder_is_one_hour_before_move_by():
    move_by = datetime(2026, 9, 8, 12, 0)

    reminder_at = calculate_reminder_at(move_by)

    assert reminder_at == datetime(2026, 9, 8, 11, 0)