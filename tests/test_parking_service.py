from datetime import datetime

from app.services.parking_service import get_parking_status

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