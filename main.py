import flet as ft
from views.routing import Routing, path
from views.index_view import IndexView
from views.hub import Hub
from views.writer import Writer
from views.help_md import Help
from views.posts_view import PostsView
from views.notice_view import NoticeView
from views.normal_view import NormalView
from views.editor import Editor
from user.login import Login, Register
from db import create_tables

create_tables()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    app_routes = [
        path(url="/", clear=True, view=Hub),
        path(url="/all/", clear=True, view=IndexView),
        path(url="/new_post/", clear=False, view=Writer),
        path(url="/posts/:id", clear=False, view=PostsView),
        path(url="/posts/:id/edit", clear=False, view=Editor),
        path(url="/login/", clear=False, view=Login),
        path(url="/register/", clear=False, view=Register),
        path(url="/notices/", clear=False, view=NoticeView),
        path(url="/normalposts/", clear=False, view=NormalView),
        path(url="/new_post/help/", clear=False, view=Help),
    ]

    Routing(page, app_routes)
    page.go(page.route)


ft.app(target=main)
