from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Movie, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def get_movies_with_directors(sess):
    movies_list = []
    query = select(Movie, Director.name).join(Movie.director).order_by(Movie.title)
    result = sess.execute(query)
    for movie, director_name in result:
        movies_list.append(f"{movie.title} by {director_name}, "
                           f"released on {movie.release_date}, duration: {movie.duration} min,"
                           f" genre: {movie.genre}, rating: {movie.rating}")
    return movies_list
# END
