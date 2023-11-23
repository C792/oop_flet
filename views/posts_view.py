import flet as ft
from views.routing import Params, Basket
import db

db.create_tables()


def PostsView(page: ft.Page, params: Params, basket: Basket):
    post = db.Posts.get_by_id(db.Posts, id=params.id)
    comments = db.Comments.get_by_post_id(db.Comments, post_id=params.id)
    ref_comment = ft.Ref[ft.TextField]()

    def add_comment(e):
        if not ref_comment.current.value:
            return
        db.Comments.add(
            db.Comments,
            comment=ref_comment.current.value,
            post_id=params.id,
        ),
        page.go("/")
        page.go(f"/posts/{params.id}")

    def delete_comment(i):
        db.Comments.delete(
            db.Comments,
            i,
        ),
        page.go("/")
        page.go(f"/posts/{params.id}")

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
            ft.Column(
            controls=[
                ft.Text(
                    value=post.title,
                    size=20,
                ),
                ft.Text(
                    value=post.post,
                    size=15,
                    max_lines=100,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
                ft.Divider(),
                ft.Text(
                    value="Comments",
                    size=18,
                ),
                ft.Row(
                    controls=[
                        ft.TextField(
                            ref=ref_comment,
                            label="Add Comment",
                        ),
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            on_click=add_comment,
                        ),
                    ]
                ),
                ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value=comment.comment,
                                size=15,
                                max_lines=100,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Text(
                                value=comment.created_at.strftime("%Y-%m-%d %H:%M"),
                                size=10,
                            ),
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                on_click=lambda e, id=comment.id:delete_comment(id),
                            ),
                        ]
                    )
                    for comment in comments
                ]),
            ]),
        ],
        scroll="auto",
    )