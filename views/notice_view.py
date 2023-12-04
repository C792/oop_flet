import flet as ft
from views.routing import Params, Basket

def NoticeView(page: ft.Page, params: Params, basket: Basket):
    def deletebutton(i):
        if basket.role == "admin" or basket.user == i.author:
            return ft.IconButton(
                icon=ft.icons.DELETE,
                right=5,
                top=10,
                on_click=lambda e, id=i.id: delete_post(id),
            )
        else:
            return ft.Container()

    def delete_post(i):
        basket.posts.delete(id=i)
        get_all_posts()
        page.update()

    row = []

    def container_notice(post) -> ft.Container:
        if post.notice:
            return ft.Container(content=ft.Icon(ft.icons.INFO, size=30), top=20, left=15)
        else:
            return ft.Container(content=ft.Icon(ft.icons.NOTE, size=50), top=10, left=5)

    def get_all_posts():
        row.clear()
        for i in basket.posts.get_all():
            if not i.notice: continue
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
                                right=ft.BorderSide(width=1),
                            ),
                        ),
                        container_notice(i),
                        ft.Text(
                            max_lines=1,
                            overflow=ft.TextOverflow.CLIP,
                            top=20,
                            left=60,
                            value=i.title,
                            size=20,
                        ),
                        ft.Container(
                            height=70,
                            border_radius=10,
                            on_click=lambda e, id=i.id: page.go(f"/posts/{id}"),
                        ),
                        ft.Text(
                            max_lines=1,
                            overflow=ft.TextOverflow.CLIP,
                            top=50,
                            left=60,
                            value=i.author,
                            size=10,
                        ),
                        ft.Text(
                            max_lines=1,
                            overflow=ft.TextOverflow.CLIP,
                            top=50,
                            left=160,
                            value=i.created_at.strftime("%Y-%m-%d %H:%M"),
                            size=10,
                        ),
                        deletebutton(i),
                    ]
                )
            )
    def logout(e):
        basket.user = None
        basket.role = None
        page.update()
        page.go("/login/")
        page.go("/")
    if basket.get("user") == None:
        return ft.View(
            "/notices/",
            controls=[
                ft.AppBar(
                    # leading=ft.Icon(ft.icons.FORMAT_QUOTE_OUTLINED, size=60),
                    leading=ft.Icon(ft.icons.ACCOUNT_BALANCE, size=50),
                    # leading=ft.Icon(ft.icons.API_OUTLINED, size=50),
                    leading_width=60,
                    title=ft.Text("DSHub"),
                    center_title=False,
                    actions=[
                        ft.IconButton(ft.icons.HOME, on_click=lambda e: page.go("/")),
                        ft.IconButton(
                            ft.icons.POST_ADD, on_click=lambda e: page.go("/new_post/")
                        ),
                        ft.IconButton(
                            ft.icons.ACCOUNT_CIRCLE, on_click=lambda e: page.go("/login/")
                        )
                    ],
                ),
            ],
            scroll="auto",
        )
    get_all_posts()
    return ft.View(
        "/all/",
        controls=[
            ft.AppBar(
                # leading=ft.Icon(ft.icons.FORMAT_QUOTE_OUTLINED, size=60),
                leading=ft.Icon(ft.icons.ACCOUNT_BALANCE, size=50),
                # leading=ft.Icon(ft.icons.API_OUTLINED, size=50),
                leading_width=60,
                title=ft.Text("DSHub"),
                center_title=False,
                actions=[
                    ft.IconButton(ft.icons.HOME, on_click=lambda e: page.go("/")),
                    ft.IconButton(
                        ft.icons.POST_ADD, on_click=lambda e: page.go("/new_post/")
                    ),
                    ft.Text(f"Loggined in as {basket.user} " + ("(admin)" if basket.role == "admin" else "(user)")),
                    ft.IconButton(
                        ft.icons.LOGOUT, on_click=logout
                    )
                ],
            ),
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(width=10),
                            ft.IconButton(
                                icon=ft.icons.HOME,
                                on_click=lambda e: page.go("/"),
                            ),
                            ft.Container(width=10),
                            ft.IconButton(
                                icon=ft.icons.INFO,
                                on_click=lambda e: page.go("/notices/"),
                            ),
                            ft.Container(width=10),
                            ft.IconButton(
                                icon=ft.icons.NOTE,
                                on_click=lambda e: page.go("/normalposts/"),
                            ),
                            ft.Container(width=10),
                            ft.IconButton(
                                icon=ft.icons.LIST,
                                on_click=lambda e: page.go("/all/"),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],                    
            ),
            ft.Column(row),
        ],
        scroll="auto",
    )