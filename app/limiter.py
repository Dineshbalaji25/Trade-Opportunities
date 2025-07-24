
import time
from fastapi import HTTPException

rate_limit_data = {}

def check_rate_limit(user: str, max_calls=5, period=60):
    now = time.time()
    user_log = rate_limit_data.get(user, [])
    user_log = [t for t in user_log if now - t < period]
    if len(user_log) >= max_calls:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    user_log.append(now)
    rate_limit_data[user] = user_log
