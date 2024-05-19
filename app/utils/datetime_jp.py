from datetime import datetime
import pytz

def now() -> datetime:
    now_utc = datetime.now(pytz.utc)
    japan_tz = pytz.timezone('Asia/Tokyo')
    now_japan = now_utc.astimezone(japan_tz)

    return now_japan