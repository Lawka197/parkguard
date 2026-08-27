# ParkGuard

ParkGuard is a location-based parking reminder system for time-restricted parking zones.

## Problem

In some streets, parking is allowed only during specific time windows. When a car is parked in such a zone, it is easy to forget when it needs to be moved.

ParkGuard aims to detect whether a car has been parked in a predefined parking zone and determine when the driver needs to move it.

## MVP

The first version of ParkGuard should:

- receive the parked car's location
- check whether the location is inside a predefined parking zone
- evaluate the parking rules based on weekday and time
- calculate when the car needs to be moved
- return a reminder time

## Planned Extensions

- iOS Shortcuts integration
- automatic detection when the car is parked
- support for multiple parking zones
- automatic notifications and reminders
- parking history
- AirTag integration for locating the parked car

## Tech Stack

- Python
- FastAPI
- iOS Shortcuts
- Git / GitHub