import flet as ft
from views.routing import Params, Basket
import db

db.create_tables()

def Editor(page: ft.Page, params: Params, basket: Basket):
    post = db.Posts.get_by_id(db.Posts, id=params.id)
    ref_title = ft.Ref[ft.TextField]()
    ref_text = ft.Ref[ft.TextField]()

    def save_post(e):
        basket.posts.update(
            id=params.id,
            title=ref_title.current.value,
            post=ref_text.current.value,
            notice=c.value if c.disabled == False else False,
        )
        page.go(f"/posts/{params.id}")
    c = ft.Checkbox(label="Notice", disabled=False if basket.get("role") == "admin" else True)
    V = ft.View(
        f"/posts/{params.id}/edit",
        controls=[
            ft.AppBar(
                title=ft.Text("DSHub - Edit Post"),
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
    ref_title.current.value = post.title
    ref_text.current.value = post.post
    c.value = post.notice
    return V
