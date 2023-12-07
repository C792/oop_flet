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
            author=basket.user if basket.user else "Anonymous",
        ),
        page.go("/")
        page.go(f"/posts/{params.id}")

    def deletebutton(comment):
        if basket.role == "admin" or basket.user == comment.author:
            return ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=comment.id:delete_comment(id),
            )
        else:
            return ft.Container()

    def editbutton():
        if basket.role == "admin" or basket.user == post.author:
            return ft.IconButton(
                icon=ft.icons.EDIT,
                on_click=lambda e:page.go(f"/posts/{params.id}/edit"),
            )
        else:
            return ft.Container()

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
                # leading=ft.Icon(ft.icons.ACCOUNT_BALANCE, size=50),
                # leading_width=60,
                title=ft.Text("DSHub"),
                actions=[
                    ft.IconButton(
                        icon=ft.icons.SHARE,
                        on_click=lambda e: print(f"/posts/{params.id}"),
                    ),
                    editbutton(),
                ],
            ),
            ft.Column(
            controls=[
                ft.Container(height=3),
                ft.Text(
                    value=post.title,
                    size=30,
                ),
                ft.Container(height=3),
                ft.Text(
                    value=f'written by {post.author}, at {post.created_at.strftime("%Y-%m-%d %H:%M")}',
                    size=12,
                ),
                ft.Divider(opacity=0.5),
                ft.Markdown(
                    post.post,
                    selectable=False,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    code_theme="atom-one-dark",
                    code_style=ft.TextStyle(font_family="Consolas"),
                    on_tap_link=lambda e: page.launch_url(e.data),
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
                                value=comment.author,
                                size=10,
                            ),
                            ft.Text(
                                value=comment.created_at.strftime("%Y-%m-%d %H:%M"),
                                size=10,
                            ),
                            deletebutton(comment),
                        ]
                    )
                    for comment in comments
                ]),
            ]),
        ],
        scroll="auto",
    )