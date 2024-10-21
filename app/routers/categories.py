from .. import schemas, models, utils, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, HTTPException, APIRouter

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    # if current_user.role != "admin":
    #     raise HTTPException(status_code=403, detail="You are not an admin") (no need for roles at the moment)
    new_category = models.Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

@router.get("/", response_model=List[schemas.Category])
def get_categories(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    categories = db.query(models.Category).all()
    if not categories:
        raise HTTPException(status_code=404, detail="Categories not found")
    return categories

@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryBase, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    query = db.query(models.Category).filter(models.Category.id == category_id)
    update_category = query.first()
    if not update_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    if category.category_name:
        update_category.category_name = category.category_name
    db.commit()

    return update_category

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    
    return {"data": "Category deleted"}
