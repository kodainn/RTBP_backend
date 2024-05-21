from datetime import datetime, date
import pytz

def now() -> datetime:
    now_utc = datetime.now(pytz.utc)
    japan_tz = pytz.timezone('Asia/Tokyo')
    now_japan = now_utc.astimezone(japan_tz)

    return now_japan


def now_date() -> date:
    now_utc = datetime.now(pytz.utc)
    japan_tz = pytz.timezone('Asia/Tokyo')
    now_japan = now_utc.astimezone(japan_tz)

    return now_japan.date()


def now_year() -> int:
    now_utc = datetime.now(pytz.utc)
    japan_tz = pytz.timezone('Asia/Tokyo')
    now_japan = now_utc.astimezone(japan_tz)

    return now_japan.year