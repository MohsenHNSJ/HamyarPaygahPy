"""Utility functions related to math."""

import datetime


def calculate_time_delta(
    start_time: datetime.time | None,
    end_time: datetime.time | None,
) -> datetime.timedelta | None:
    """Calculates the period of time between start and end.

    Returns None if either is None. Counts for the midnight bug in Asayar.

    Args:
        start_time (datetime.time | None): Starting time of the period
        end_time (datetime.time | None): Ending time of the period

    Returns:
        datetime.timedelta | None: Period of time between start and end.
    """
    # If either depart from station time or arrive at emergency time are zero, return zero
    if start_time is None or end_time is None:
        return None
    # Else, calculate the period and return it
    # Get the current date
    date_of_today = datetime.datetime.today().date()  # noqa: DTZ002
    # Set the times with date
    received_date = datetime.datetime.combine(
        date_of_today,
        start_time,
    )
    depart_date = datetime.datetime.combine(
        date_of_today,
        end_time,
    )

    # If the depart time is lower than received time, it means it's past the midnight
    # so we add one day to depart time
    if depart_date < received_date:
        depart_date += datetime.timedelta(days=1)

    # Return the time delta, or 0 in case of an error
    return max(depart_date - received_date, datetime.timedelta(seconds=0))
