
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "InzdIWx8PHo721Vsiz7aZ78GApuwkAoLz_KilLL9EG0"
ALGORITHM = "HS256"

def create_token(user: str):
    payload = {"sub": user, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.PyJWTError:
        return None
