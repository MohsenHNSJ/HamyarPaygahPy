"""Information sub-model for Mission details model."""
# pylint: disable=R0902

import datetime
from dataclasses import dataclass


@dataclass(slots=True)
class Information:
    """Holds general information of the patient and mission."""

    patient_name: str
    """Full name of the patient."""
    years_of_age: int
    """Years of patient age."""
    months_of_age: int
    """Remaining months of patient age."""

    @property
    def full_age(self) -> str | None:
        """Combined years and months as a persian string."""
        # If both years and months of age are not provided, return nothing.
        if self.years_of_age == 0 and self.months_of_age == 0:
            return None
        # If only years of age is provided, return only age.
        if self.years_of_age != 0 and self.months_of_age == 0:
            return f"{self.years_of_age} سال"
        # If only months of age is provided, return only months.
        if self.years_of_age == 0 and self.months_of_age != 0:
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
    national_code: int
    """National code of the patient."""
    document_serial_number: str
    """Serial number of mission details"""
    caller_number: str
    """Number of the emergency caller"""
    backup_number: str
    """Backup number provided by emergency caller"""
    ambulance_code: int
    """Code of the ambulance responding to mission"""
    document_request_time: datetime.datetime
    """Timestamp of the last update to the mission details"""
    province: str
    """Province the mission is located at"""
    summary: str
    """Summary of the mission"""
