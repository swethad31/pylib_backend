from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Book

router = APIRouter()


@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


@router.post("/books")
def add_book(book: dict, db: Session = Depends(get_db)):
    new_book = Book(
        title=book["title"],
        author=book["author"]
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return {
        "message": "Book added",
        "data": new_book
    }