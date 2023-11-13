from sqlmodel import (
    SQLModel,
    create_engine,
    Session,
    Field,
    select,
)
from typing import Optional


database_file_name = "database.sqlite3"
engine = create_engine(f"sqlite:///{database_file_name}")


class Posts(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, nullable=False)
    title: str = Field(nullable=False)
    post: str = Field(nullable=False)
    notice: bool = Field(default=False)

    def add(self, title, post):
        new_post = Posts(title=title, post=post)
        with Session(engine) as session:
            session.add(new_post)
            session.commit()
            return True

    def update(self, id, title, post):
        with Session(engine) as session:
            statement = select(Posts).where(Posts.id == id)
            results = session.exec(statement)
            old_post = results.one()
            old_post.title = title
            old_post.post = post
            session.add(old_post)
            session.commit()
            return True

    def get_all(self):
        with Session(engine) as session:
            statement = select(Posts)
            results = session.exec(statement)
            return results.all()

    def get_by_id(self, id):
        with Session(engine) as session:
            statement = select(Posts).where(Posts.id == id)
            results = session.exec(statement)
            return results.first()

    def delete(self, id):
        with Session(engine) as session:
            statement = select(Posts).where(Posts.id == id)
            results = session.exec(statement).first()
            session.delete(results)
            session.commit()
            return True


def create_tables():
    SQLModel.metadata.create_all(engine)
