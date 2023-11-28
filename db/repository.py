from abc import ABC, abstractmethod
from .database import engine, async_session
from .models import *
from sqlalchemy import select


class AbstractAsyncRepository(ABC):
    @abstractmethod
    async def add_user(self, telegram_id, username):
        pass

    @abstractmethod
    async def add_watched_video(self, user_id, video_id, user_rating, when_watched):
        pass

    @abstractmethod
    async def add_video(self, url, title, description, category, popularity_rating, video_duration, video_post_date, tags):
        pass

    @abstractmethod
    async def add_user_feedback(self, user_id, feedback_text, data_submitted):
        pass

    @abstractmethod
    async def get_tags(self):
        pass


class SqlAlchemyAsyncRepository(AbstractAsyncRepository):
    def __init__(self):
        self.engine = engine
        self.Session = async_session

    async def add_user(self, telegram_id, username):
        async with self.Session() as session:
            async with session.begin():
                new_user = Users(telegram_id=telegram_id, username=username)
                session.add(new_user)

    async def add_watched_video(self, user_id, video_id, user_rating, when_watched):
        async with self.Session() as session:
            async with session.begin():
                watched_video = UserWatched(user_id=user_id, video_id=video_id, user_rating=user_rating, when_watched=when_watched)
                session.add(watched_video)

    async def add_video(self, url, title, description, category, popularity_rating, video_duration, video_post_date, tags):
        async with self.Session() as session:
            async with session.begin():
                video = Videos(url=url,
                               title=title,
                               description=description,
                               category=category,
                               popularity_rating=popularity_rating,
                               video_duration=video_duration,
                               video_post_date=video_post_date,
                               tags=tags)
                session.add(video)

    async def add_user_feedback(self, user_id, feedback_text, data_submitted):
        async with self.Session() as session:
            async with session.begin():
                feedback = UserFeedback(user_id=user_id, feedback_text=feedback_text, data_submitted=data_submitted)
                session.add(feedback)

    async def get_tags(self):
        async with self.Session(engine) as session:
            result = await session.execute(select(Tags.name, Tags.playlist_url))
            tags = {row[0]: row[1] for row in result}
            return tags
