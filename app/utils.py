from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def calculate_avg_rating(old_avg: int, nb_of_ratings: int, new_rating: int, delete: bool = False):
    if delete:
        return (old_avg * nb_of_ratings - new_rating) / (nb_of_ratings - 1)
    return (old_avg * nb_of_ratings + new_rating) / (nb_of_ratings + 1)