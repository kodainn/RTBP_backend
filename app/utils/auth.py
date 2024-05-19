from datetime import timedelta
import hashlib

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.config import get_env_value
import app.utils.datetime_jp as datetime_jp
from app.repositories.user_repository import UserRepository
from app.database.model.models import User
from app.database.config.connect import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(username: str) -> str:
    expire = datetime_jp.now() + timedelta(minutes=int(get_env_value('ACCESS_TOKEN_EXPIRE_MINUTES')))
    payload = {
        "exp": expire,
        "sub": username
    }
    
    encode_jwt = jwt.encode(payload, get_env_value('SECRET_KEY'), algorithm=get_env_value('ALGORITHM'))

    return encode_jwt


def get_current_user(access_token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Colud not validate credentials',
        headers={'WWW-Authenticate': "Bearer"}
    )

    try:
        payload = jwt.decode(access_token, get_env_value('SECRET_KEY'), algorithms=get_env_value('ALGORITHM'))
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = UserRepository(session).find_by_username(username)
    if user is None:
        raise credentials_exception
    return user


def create_hash_password(plaintext_password: str) -> str:
    return hashlib.sha256(plaintext_password.encode()).hexdigest()


def vertify_password(hash_password: str, plaintext_password: str) -> bool:
    if hashlib.sha256(plaintext_password.encode()).hexdigest() != hash_password:
        return False
    
    return True