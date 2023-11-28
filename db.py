from sqlmodel import (
    SQLModel,
    create_engine,
    Session,
    Field,
    select,
    Relationship,
    DateTime,
)
from datetime import datetime
from typing import Optional


database_file_name = "database.sqlite3"
engine = create_engine(f"sqlite:///{database_file_name}")


class Posts(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, nullable=False)
    title: str = Field(nullable=False)
    post: str = Field(nullable=False)
    notice: bool = Field(default=False)
    author: str = Field(default="Anonymous", nullable=False)
    comment: Optional["Comments"] = Relationship(back_populates="post")
    created_at: datetime = Field(default=datetime.now(), nullable=False)

    def add(self, title, post, notice):
        new_post = Posts(title=title, post=post, notice=notice)
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
            statement = select(Comments).where(Comments.post_id == id)
            results = session.exec(statement).all()
            for result in results:
                session.delete(result)
            statement = select(Posts).where(Posts.id == id)
            results = session.exec(statement).first()
            session.delete(results)
            session.commit()
            return True

class Users(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, nullable=False)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    role: str = Field(default="user", nullable=False)
    reg_at: datetime = Field(default=datetime.now(), nullable=False)

    def add(self, username, password, role):
        new_user = Users(username=username, password=password, role=role)
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
            return True

    def get_by_username(self, username):
        with Session(engine) as session:
            statement = select(Users).where(Users.username == username)
            results = session.exec(statement)
            return results.first()

    def get_by_id(self, id):
        with Session(engine) as session:
            statement = select(Users).where(Users.id == id)
            results = session.exec(statement)
            return results.first()

    def update(self, id, username, password):
        with Session(engine) as session:
            statement = select(Users).where(Users.id == id)
            results = session.exec(statement)
            old_user = results.one()
            old_user.username = username
            old_user.password = password
            session.add(old_user)
            session.commit()
            return True

    def delete(self, id):
        with Session(engine) as session:
            statement = select(Users).where(Users.id == id)
            results = session.exec(statement).first()
            session.delete(results)
            session.commit()
            return True

class Comments(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, nullable=False)
    comment: str = Field(nullable=False)
    post_id: int = Field(nullable=False, foreign_key="posts.id")
    post: Posts = Relationship(back_populates="comment")
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

    def add(self, comment, post_id):
        new_comment = Comments(comment=comment, post_id=post_id)
        with Session(engine) as session:
            session.add(new_comment)
            session.commit()
            return True

    def get_by_post_id(self, post_id):
        with Session(engine) as session:
            statement = select(Comments).where(Comments.post_id == post_id)
            results = session.exec(statement)
            return results.all()

    def delete(self, id):
        with Session(engine) as session:
            statement = select(Comments).where(Comments.id == id)
            results = session.exec(statement).first()
            session.delete(results)
            session.commit()
            return True

def create_tables():
    SQLModel.metadata.create_all(engine)
