import flet as ft
from views.routing import Params, Basket
import db

db.create_tables()


def PostsView(page: ft.Page, params: Params, basket: Basket):
    post = db.Posts.get_by_id(db.Posts, id=params.id)
    return ft.View(
        f"/posts/{params.id}",
        controls=[
            ft.AppBar(
                title=ft.Text("Post"),
                actions=[
                    ft.IconButton(
                        icon=ft.icons.SHARE,
                        on_click=lambda e: print(f"/posts/{params.id}"),
                    ),
                ],
            ),
            # ft.TextField(
            #     ref=ft.Ref[ft.TextField](),
            #     label="Title",
            #     disabled=True,
            # ),
            ft.Stack(
                [
                    ft.Text(
                        value=post.title,
                        size=20,
                        top=10,
                        left=10,
                    ),
                    ft.Text(
                        value=post.post,
                        top=50,
                        left=10,
                        size=15,
                        max_lines=100,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                ]
            ),
        ],
        scroll="auto",
    )
