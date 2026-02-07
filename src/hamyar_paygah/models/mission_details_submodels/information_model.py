"""Information sub-model for Mission details model."""
# pylint: disable=R0902

import datetime
from dataclasses import dataclass


@dataclass(slots=True)
class Information:
    """Holds general information of the patient and mission."""

    patient_name: str | None
    """Full name of the patient."""
    years_of_age: int | None
    """Years of patient age."""
    months_of_age: int | None
    """Remaining months of patient age."""

    @property
    def full_age(self) -> str | None:
        """Combined years and months as a persian string."""
        # If both years and months of age are not provided, return nothing.
        if (self.years_of_age == 0 or self.years_of_age is None) and (
            self.months_of_age == 0 or self.months_of_age is None
        ):
            return None
        # If only years of age is provided, return only age.
        if (self.years_of_age != 0 and self.years_of_age is not None) and (
            self.months_of_age == 0 or self.months_of_age is None
        ):
            return f"{self.years_of_age} سال"
        # If only months of age is provided, return only months.
        if (self.years_of_age == 0 or self.years_of_age is None) and (
            self.months_of_age != 0 and self.months_of_age is not None
        ):
            return f"{self.months_of_age} ماه"
        # Else, return the combined age
        return f"{self.years_of_age} سال و {self.months_of_age} ماه"

    iranian_nationality: bool
    """Wether the patient is Iranian"""
    foreign_nationality: bool
    """Wether the patient is non-Iranian"""
    is_male_gender: bool
    """Wether the patient's gender is male"""
    is_female_gender: bool
    """Wether the patient's gender is female"""
    is_unknown_gender: bool
    """Wether the patient's gender is unknown"""
    national_code: int | None
    """National code of the patient."""
    document_serial_number: str | None
    """Serial number of mission details"""
    caller_number: str | None
    """Number of the emergency caller"""
    backup_number: str | None
    """Backup number provided by emergency caller"""
    ambulance_code: int | None
    """Code of the ambulance responding to mission"""
    document_request_time: datetime.datetime | None
    """Timestamp of the last update to the mission details"""
    province: str | None
    """Province the mission is located at"""
    summary: str | None
    """Summary of the mission"""
