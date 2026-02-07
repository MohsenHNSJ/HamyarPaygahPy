"""Times and distances sub-model for Mission details model."""
# pylint: disable=R0902

import datetime
from dataclasses import dataclass


@dataclass(slots=True)
class TimesAndDistances:
    """Holds information about mission times and distances."""

    mission_date: datetime.datetime | None
    """Date of the mission."""
    mission_received_time: datetime.time | None
    """Time when mission was received by EMS personnel"""
    depart_from_station_odometer: int | None
    """ODO meter of EMS vehicle on departure from station to emergency location"""
    time_to_depart: datetime.timedelta | None
    """Period of time between receiving the mission and departure of EMS personnel"""
    time_to_arrive: datetime.timedelta | None
    """Period of time between departure and arriving to emergency location"""
    time_at_emergency_location: datetime.timedelta | None
    """Period of time EMS personnel were present at emergency location"""
    time_to_hospital: datetime.timedelta | None
    """Period of time between departure from emergency location to hospital"""
    time_to_deliver: datetime.timedelta | None
    """Period of time between arriving to hospital and delivering the patient to hospital"""
    time_to_complete: datetime.timedelta | None
    """Period of time between completing the mission and arriving at station"""
    overall_mission_time: datetime.timedelta | None
    """Period of time between receiving the mission and arriving at station"""
    arrive_at_emergency_odometer: int | None
    """ODO meter of EMS vehicle on arriving to emergency location.
    Most of the time, it's not recorded by EMS personnel and will be zero"""
    arrive_at_hospital_odometer: int | None
    """ODO meter of EMS vehicle on arriving to hospital"""
    mission_complete_odometer: int | None
    """ODO meter of EMS vehicle on completing the mission"""
    arrive_at_station_odometer: int | None
    """ODO meter of EMS vehicle on arriving to station from the mission"""
    vehicle_refuel_odometer: int | None
    """ODO meter of EMS vehicle on refueling. This is 0 if no refueling is done"""
    senior_staff_code: int | None
    """Staff code of senior technician"""
    first_staff_code: int | None
    """Staff code of first technician"""
    second_staff_code: int | None
    """Staff code of second technician"""
    depart_from_station_time: datetime.time | None = None
    """Time when EMS personnel departed from station to emergency location"""
    arrive_at_emergency_time: datetime.time | None = None
    """Time when EMS personnel arrived at emergency location"""
    depart_from_emergency_time: datetime.time | None = None
    """Time when EMS personnel departed from emergency location either to hospital or station"""
    arrive_at_hospital_time: datetime.time | None = None
    """Time when EMS personnel arrived at hospital"""
    deliver_to_hospital_time: datetime.time | None = None
    """Time when EMS personnel delivered the patient to hospital personnel"""
    mission_complete_time: datetime.time | None = None
    """Time when mission was completed"""
    arrive_at_station_time: datetime.time | None = None
    """Time when EMS personnel arrived at station from the mission"""

    @property
    def overall_mission_distance(self) -> int:
        """Distance traveled in this mission."""
        # If either depart-from_station_odometer and arrive_at_station_odometer are zero
        # Return 0
        if (
            self.depart_from_station_odometer == 0
            or self.arrive_at_station_odometer == 0
            or self.depart_from_station_odometer is None
            or self.arrive_at_station_odometer is None
        ):
            return 0
        # Else, calculate the distance and return it
        return self.arrive_at_station_odometer - self.depart_from_station_odometer
