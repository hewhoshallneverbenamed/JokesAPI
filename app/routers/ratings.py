from .. import schemas, models, utils, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, HTTPException, APIRouter

router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"]
)

@router.post("/", response_model=schemas.Rating)
def create_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    joke = db.query(models.Joke).filter(models.Joke.id == rating.joke_id).first()
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    if rating.rating < 1 or rating.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
    if db.query(models.Rating).filter(models.Rating.joke_id == rating.joke_id, models.Rating.user_id == current_user.id).first():
        raise HTTPException(status_code=400, detail="You have already rated this joke")
    
    new_rating = models.Rating(**rating.model_dump())
    new_rating.user_id = current_user.id
    db.add(new_rating)

    joke.avg_rating = utils.calculate_avg_rating(joke.avg_rating, joke.num_ratings, rating.rating)
    joke.num_ratings += 1
    db.commit()
    db.refresh(new_rating)  

    return new_rating

@router.delete("/{joke_id}")
def delete_rating(joke_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    rating = db.query(models.Rating).filter(models.Rating.joke_id == joke_id, models.Rating.user_id == current_user.id).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    joke = db.query(models.Joke).filter(models.Joke.id == joke_id).first()
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")

    joke.avg_rating = utils.calculate_avg_rating(joke.avg_rating, joke.num_ratings, rating.rating, delete=True)
    joke.num_ratings -= 1
    db.delete(rating)
    db.commit()

    return {"data": "Rating deleted"}