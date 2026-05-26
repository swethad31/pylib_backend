from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Book
from app.schemas import BookCreate, BookResponse

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


# CREATE BOOK
@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):

    new_book = Book(
        title=book.title,
        author=book.author
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


# GET ALL BOOKS
@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):

    books = db.query(Book).all()

    return books


# GET SINGLE BOOK
@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book