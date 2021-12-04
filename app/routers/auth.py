from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from app import oauth2

from ..import database, schemas, models, utilis

router = APIRouter(tags = ['Authentication'])

@router.post('/login', response_model = schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db) ):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user :
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f'Invalid Credentials')

    if not utilis.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail= f"Invalid Credentials")

    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return {"access_token" : access_token, "token_type": "bearer"}