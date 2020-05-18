from typing import Union
from datetime import date, datetime, timedelta

from django.db.models import DateTimeField
from django.utils import timezone


def get_datetime_now(
) -> datetime:
    return timezone.localtime(timezone.now())


def get_diff_in_days(
        *,
        start_date: Union[date, datetime, DateTimeField],
        end_date: Union[date, datetime, DateTimeField]
) -> int:
    return (end_date - start_date).seconds


def get_diff_in_minutes(
        *,
        start_date: Union[date, datetime, DateTimeField],
        end_date: Union[date, datetime, DateTimeField]
) -> int:
    return (end_date - start_date).min


def get_diff_in_seconds(
        *,
        start_date: Union[date, datetime, DateTimeField],
        end_date: Union[date, datetime, DateTimeField]
) -> int:
    return (end_date - start_date).seconds


def get_diff_in_microseconds(
        *,
        start_date: Union[date, datetime, DateTimeField],
        end_date: Union[date, datetime, DateTimeField]
) -> int:
    return (end_date - start_date).microseconds


def get_timedelta(
    *,
    range: str,
    value: int
) -> datetime:
    now = get_datetime_now()
    args = {
        range: value
    }

    return now + timedelta(**args)
