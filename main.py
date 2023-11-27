import flet as ft
from views.routing import Routing, path
from views.index_view import IndexView
from views.new_post_view import NewPostView
from views.posts_view import PostsView
from user.login import Login, Register
from db import create_tables

create_tables()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    app_routes = [
        path(url="/", clear=True, view=IndexView),
        path(url="/new_post/", clear=False, view=NewPostView),
        path(url="/posts/:id", clear=False, view=PostsView),
        path(url="/login/", clear=False, view=Login),
        path(url="/register/", clear=False, view=Register),
    ]

    Routing(page, app_routes)
    page.go(page.route)


ft.app(target=main)
