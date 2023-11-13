import flet as ft
from views.routing import Params, Basket
from db import Posts


def IndexView(page: ft.Page, params: Params, basket: Basket):

    if basket.get("posts") == None:
        basket.posts = Posts()

    def delete_post(id):
        basket.posts.delete(id = id)
        get_all_posts()
        page.update()

    row = []
    def get_all_posts():
        row.clear()
        for i in basket.posts.get_all():
            row.append(
                ft.Stack(
                    [
                        ft.Container(
                            height=70,
                            border_radius=10,
                            border=ft.Border(
                                top=ft.BorderSide(width=1),
                                bottom=ft.BorderSide(width=1),
                                left=ft.BorderSide(width=1),
                                right=ft.BorderSide(width=1)
                            )
                        ),
                        ft.Container(
                            content=ft.Icon(ft.icons.NOTE, size=50),
                            top=10,
                            left=5
                        ),
                        ft.Text(
                            max_lines=1,
                            overflow=ft.TextOverflow.CLIP,
                            top=20,
                            left=60,
                            value=i.title,
                            size=20
                        ),
                        ft.Container(
                            height=70,
                            border_radius=10,
                            on_click=lambda e,id=i.id: page.go(f"/posts/{id}")
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            right=5,
                            top=10,
                            on_click= lambda e,id=i.id: delete_post(id)
                        ),

                    ]
                )
            )

    get_all_posts()

    return ft.View(
        "/",
        controls=[
            ft.AppBar(
                leading=ft.Icon(ft.icons.NOTE),
                leading_width=40,
                title=ft.Text("Post App"),
                center_title=False,
                actions=[
                    ft.IconButton(
                        ft.icons.NOTE_ADD,
                        on_click=lambda e: page.go("/new_post/")
                    ),
                ],
            ),
            ft.Column(row)

        ],
        scroll="auto"
    )
