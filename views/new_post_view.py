import flet as ft
from views.routing import Params, Basket


def NewPostView(page: ft.Page, params: Params, basket: Basket):
    ref_title = ft.Ref[ft.TextField]()
    ref_text = ft.Ref[ft.TextField]()

    def save_post(e):
        basket.posts.add(
            title=ref_title.current.value,
            post=ref_text.current.value,
        )
        page.go("/")

    return ft.View(
        "/new_post/",
        controls=[
            ft.AppBar(
                title=ft.Text("New Post"),
                actions=[
                    ft.IconButton(ft.icons.SAVE, on_click=save_post),
                ],
            ),
            ft.TextField(
                ref=ref_title,
                label="Title",
                min_lines=1,
                max_lines=2,
            ),
            ft.TextField(
                ref=ref_text,
                expand=True,
                multiline=True,
                min_lines=18,
                max_lines=18,
                label="Content",
            ),
        ],
        scroll="auto",
    )
