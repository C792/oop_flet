import flet as ft
from views.routing import Params, Basket
from db import Posts, Users, Categories


def Hub(page: ft.Page, params: Params, basket: Basket):
    if basket.get("posts") == None:
        basket.posts = Posts()
    if basket.get("users") == None:
        basket.users = Users()
    if basket.get("categories") == None:
        basket.categories = Categories()
    def logout(e):
        basket.user = None
        basket.role = None
        page.update()
        page.go("/login/")
        page.go("/")
    cnt = [0, 0]
    for i in basket.posts.get_all():
        if i.notice:
            cnt[0] += 1
        else:
            cnt[1] += 1
    row = []
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
                ft.Container(content=ft.Icon(ft.icons.INFO, size=30), top=20, left=15),
                ft.Text(
                    max_lines=1,
                    overflow=ft.TextOverflow.CLIP,
                    top=20,
                    left=60,
                    value=f"notices({str(cnt[0])})",
                    size=20,
                ),
                ft.Container(
                    height=70,
                    border_radius=10,
                    on_click=lambda e: page.go(f"/notices/"),
                ),
            ]
        )
    )
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
                ft.Container(content=ft.Icon(ft.icons.NOTE, size=50), top=10, left=5),
                ft.Text(
                    max_lines=1,
                    overflow=ft.TextOverflow.CLIP,
                    top=20,
                    left=60,
                    value=f"posts({str(cnt[1])})",
                    size=20,
                ),
                ft.Container(
                    height=70,
                    border_radius=10,
                    on_click=lambda e: page.go(f"/normalposts/"),
                ),
            ]
        )
    )
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
                ft.Container(content=ft.Icon(ft.icons.LIST, size=50), top=10, left=5),
                ft.Text(
                    max_lines=1,
                    overflow=ft.TextOverflow.CLIP,
                    top=20,
                    left=60,
                    value=f"all posts({str(cnt[0] + cnt[1])})",
                    size=20,
                ),
                ft.Container(
                    height=70,
                    border_radius=10,
                    on_click=lambda e: page.go(f"/all/"),
                ),
            ]
        )
    )
            
    if basket.get("user") == None:
        return ft.View(
            "/",
            controls=[
                ft.AppBar(
                    # leading=ft.Icon(ft.icons.FORMAT_QUOTE_OUTLINED, size=60),
                    leading=ft.Icon(ft.icons.ACCOUNT_BALANCE, size=50),
                    # leading=ft.Icon(ft.icons.API_OUTLINED, size=50),
                    leading_width=60,
                    title=ft.Text("DSHub"),
                    center_title=False,
                    actions=[
                        ft.IconButton(ft.icons.LOGIN, on_click=lambda e: page.go("/login/")),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "\n\nLogin To See and Create Posts!",
                                    ft.TextStyle(
                                        size=40,
                                        weight=ft.FontWeight.BOLD,
                                        foreground=ft.Paint(
                                            gradient=ft.PaintLinearGradient(
                                                (250, 20), (750, 20), [ft.colors.YELLOW, ft.colors.BLUE]
                                            ),
                                        ),
                                    )
                                )
                            ],
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            scroll="auto",
        )
    return ft.View(
        "/",
        controls=[
            ft.AppBar(
                # leading=ft.Icon(ft.icons.FORMAT_QUOTE_OUTLINED, size=60),
                leading=ft.Icon(ft.icons.ACCOUNT_BALANCE, size=50),
                # leading=ft.Icon(ft.icons.API_OUTLINED, size=50),
                leading_width=60,
                title=ft.Text("DSHub"),
                center_title=False,
                actions=[
                    ft.IconButton(ft.icons.LIST, on_click=lambda e: page.go("/all")),
                    ft.IconButton(
                        ft.icons.POST_ADD, on_click=lambda e: page.go("/new_post/")
                    ),
                    ft.Text(f"Loggined in as {basket.user} " + ("(admin)" if basket.role == "admin" else "(user)")),
                    ft.IconButton(
                        ft.icons.LOGOUT, on_click=logout
                    )
                ],
            ),
            ft.Row(
                controls=[
                    ft.Text(
                        spans=[
                            ft.TextSpan(
                                "\n\nWelcome to DSHub!\n\n",
                                ft.TextStyle(
                                    size=40,
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        gradient=ft.PaintLinearGradient(
                                            (250, 20), (750, 20), [ft.colors.RED, ft.colors.YELLOW]
                                        ),
                                    ),
                                )
                            )
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Column(row),
        ],
        scroll="auto",
    )