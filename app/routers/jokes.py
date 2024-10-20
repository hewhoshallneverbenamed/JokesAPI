from .. import schemas, models, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import Depends, HTTPException, APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/jokes",
    tags=["Jokes"],
)

@router.get("/", response_model=List[schemas.Joke])
async def get_jokes(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user), skip: int = 0, limit: int = 10, search: Optional[str] = None):
    jokes = db.query(models.Joke).offset(skip).limit(limit).all()
    if not jokes:
        raise HTTPException(status_code=404, detail="Jokes not found")
    return jokes

@router.post("/", response_model=schemas.Joke)
async def create_joke(joke: schemas.JokeCreate, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_joke = models.Joke(**joke.model_dump())
    new_joke.owner_id = current_user.id
    db.add(new_joke)
    db.commit()
    db.refresh(new_joke)
    return new_joke

@router.get("/{joke_id}", response_model=schemas.Joke)
async def get_joke(joke_id: int, db: Session = Depends(get_db)):
    joke = db.query(models.Joke).filter(models.Joke.id == joke_id).first()
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    
    return joke

@router.delete("/{joke_id}")
async def delete_joke(joke_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    joke = db.query(models.Joke).filter(models.Joke.id == joke_id).first()
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    if joke.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this joke")

    db.delete(joke)
    db.commit()
    
    return {"data": "Joke deleted"}

@router.put("/{joke_id}", response_model=schemas.Joke)
async def update_joke(joke_id: int, joke: schemas.JokeUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    query = db.query(models.Joke).filter(models.Joke.id == joke_id)
    update_joke = query.first()
    if not update_joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    if update_joke.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="You are not the owner of this joke")

    # update_joke.update(joke.model_dump(), synchronize_session=False) 
    if joke.joke_text:
        update_joke.joke_text = joke.joke_text
    if joke.category_id:
        update_joke.category_id = joke.category_id
    
    update_joke.updated_at = datetime.now()
    db.commit()
    
    return {"data": query.first()}