import flet as ft
from views.routing import Params, Basket


def Writer(page: ft.Page, params: Params, basket: Basket):
    ref_title = ft.Ref[ft.TextField]()
    ref_text = ft.Ref[ft.TextField]()

    def save_post(e):
        basket.posts.add(
            title=ref_title.current.value,
            post=ref_text.current.value,
            notice=c.value if c.disabled == False else False,
            author=basket.user if basket.user else "Anonymous",
        )
        basket.categories.add(
            category="notice" if c.value == True else "post",
            post_id=len(basket.posts.get_all()),
        )
        page.go("/")
        page.go(f"/posts/{basket.posts.get_all()[-1].id}")
    c = ft.Checkbox(label="Notice", disabled=False if basket.get("role") == "admin" else True)
    return ft.View(
        "/new_post/",
        controls=[
            ft.AppBar(
                title=ft.Text("DSHub - New Post"),
                actions=[
                    ft.IconButton(ft.icons.QUESTION_MARK_ROUNDED, on_click=lambda e: page.go("/new_post/help/")),
                    c,
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
