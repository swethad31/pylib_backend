from fastapi import FastAPI
from app.database import engine
from app.models import Book
from app.routes.books import router as book_router

Book.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_router)


@app.get("/")
def home():
    return {"message": "Library Backend Running"}

