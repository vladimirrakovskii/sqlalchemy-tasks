from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_all_movies(sess):
    movies_list = []
    query = select(Movie)
    result = sess.execute(query)
    for movie in result.scalars():
        movies_list.append(f"{movie.title} by {movie.director}, "
                           f"released on {movie.release_date}, duration: {movie.duration} min,"
                           f" genre: {movie.genre}, rating: {movie.rating}")
    return movies_list

def get_movies_by_director(sess, director_name):
    movies_list = []
    query = select(Movie).where(Movie.director == director_name).order_by(Movie.release_date)
    result = sess.execute(query)
    for movie in result.scalars():
        movies_list.append(f"{movie.title} by {movie.director}, "
                           f"released on {movie.release_date}, duration: {movie.duration} min,"
                           f" genre: {movie.genre}, rating: {movie.rating}")
    return movies_list

def get_top_rated_movies(sess, n):
    movies_list = []
    query = select(Movie).order_by(Movie.rating.desc()).limit(n)
    result = sess.execute(query)
    for movie in result.scalars():
        movies_list.append(f"{movie.title} by {movie.director}, "
                           f"released on {movie.release_date}, duration: {movie.duration} min,"
                           f" genre: {movie.genre}, rating: {movie.rating}")
    return movies_list
# END
