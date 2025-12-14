from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET = "SWEET_KATA_SECRET"
ALGO = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_pwd(pwd):
    return pwd_context.hash(pwd)

def verify_pwd(pwd, hashed):
    return pwd_context.verify(pwd, hashed)

def create_token(data: dict):
    data["exp"] = datetime.utcnow() + timedelta(hours=5)
    return jwt.encode(data, SECRET, algorithm=ALGO)
