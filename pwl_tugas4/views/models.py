# di models/models.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)

engine = create_engine('sqlite:///photos.db')  

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

dummy_photos = [
    {'title': 'Photo 1', 'url': 'https://example.com/photo1.jpg'},
    {'title': 'Photo 2', 'url': 'https://example.com/photo2.jpg'},
    {'title': 'Photo 3', 'url': 'https://example.com/photo3.jpg'},
    {'title': 'Photo 4', 'url': 'https://example.com/photo4.jpg'},
    {'title': 'Photo 5', 'url': 'https://example.com/photo5.jpg'},
    {'title': 'Photo 6', 'url': 'https://example.com/photo6.jpg'},
    {'title': 'Photo 7', 'url': 'https://example.com/photo7.jpg'},
    {'title': 'Photo 8', 'url': 'https://example.com/photo8.jpg'},
    {'title': 'Photo 9', 'url': 'https://example.com/photo9.jpg'},
    {'title': 'Photo 10', 'url': 'https://example.com/photo10.jpg'},

]

for dummy_photo in dummy_photos:
    new_photo = Photo(**dummy_photo)
    session.add(new_photo)

session.commit()