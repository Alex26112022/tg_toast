import os

from dotenv import load_dotenv
from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, \
    AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()

engine = create_async_engine(url=os.environ.get('POSTGRES'), echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Theme(Base):
    """ Тема тоста. """
    __tablename__ = 'themes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f'<Theme(id={self.id}, title={self.title})>'


class Toast(Base):
    """ Тост. """
    __tablename__ = 'toasts'

    id: Mapped[int] = mapped_column(primary_key=True)
    theme_id: Mapped[int] = mapped_column(ForeignKey('themes.id'))
    content: Mapped[str] = mapped_column()

    def __repr__(self):
        return f'<Toast(id={self.id}, theme_id={self.theme_id}, content={self.content})>'


async def async_run_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
