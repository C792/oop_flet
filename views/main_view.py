import flet as ft
from views.routing import Params, Basket
from db import Posts, Users


def MainView(page: ft.Page, params: Params, basket: Basket):
    if basket.get("posts") == None:
        basket.posts = Posts()
    if basket.get("users") == None:
        basket.users = Users()

    def logout(e):
        basket.user = None
        basket.role = None
        page.update()
        page.go("/login/")
        page.go("/")
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
                        ft.IconButton(ft.icons.LIST, on_click=lambda e: page.go("/all/")),
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
                                "\n\nWelcome to DSHub!",
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
        ],
        scroll="auto",
    )