from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, users, auth, vote
from .config import Settings
from app import database
from fastapi.middleware.cors import CORSMiddleware



#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Caso tenham o mesmo path o que aparece primeiro é o que tem o código escrito primeiro


my_posts = [{"title":"title of post 1", "content":"content of post 1","id": 1},{"title":"food", "content":"lasagna","id": 2}]


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") #decorator- faz com que a função funcione como um path @(nome da app, neste caso app), método HTTP, path do URL
def root(): #Com async é uma função assincrona e pode ter outro nome sem ser root
    return {"message": "Hello, I am Jose, this is my API!"} 


#Podemos usar redoc ou docs para ver os requests

