from sqlalchemy import Column, Integer, String, DateTime, Float, Time, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class UserFeedback(Base):
    __tablename__ = 'user_feedback'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    feedback_text = Column(String)
    data_submitted = Column(DateTime)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String)
    username = Column(String)
    feedback = relationship('UserFeedback', backref='user', lazy="selectin")


class UserWatched(Base):
    __tablename__ = 'user_watched'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    video_id = Column(Integer, ForeignKey('videos.id'))
    user_rating = Column(Integer)
    when_watched = Column(DateTime)


class Videos(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    popularity_rating = Column(Float)
    video_duration = Column(Time)
    video_post_date = Column(DateTime)
    tags = relationship('Tags', secondary='videos_tags', backref='videos', lazy="selectin")


class VideosTags(Base):
    __tablename__ = 'videos_tags'
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey('videos.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    playlist_url = Column(String)
