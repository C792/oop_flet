import flet as ft
from views.routing import Params, Basket
from db import Users

def Login(page: ft.Page, params: Params, basket: Basket):
    ref_username = ft.Ref[ft.TextField]()
    ref_password = ft.Ref[ft.TextField]()
    Alert = ft.Text(
        "",
        size=30,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.RED_800,
        weight=ft.FontWeight.NORMAL,
    )
    def login(e):
        pw = basket.users.get_by_username(username=ref_username.current.value)
        if not pw or pw.password != ref_password.current.value:
            Alert.value = "Please check ID or Password"
            page.update()
        else:
            basket.user = ref_username.current.value
            basket.role = pw.role
            page.update()
            page.go("/")
            page.update()
                

    return ft.View(
        "/login/",
        controls=[
            ft.AppBar(
                title=ft.Text("Login"),
                actions=[
                    ft.IconButton(ft.icons.SAVE, on_click=login),
                    ft.IconButton(ft.icons.LOGIN, on_click=lambda e: page.go("/register/")),
                ],
            ),
            ft.TextField(
                ref=ref_username,
                label="Username",
                min_lines=1,
                max_lines=2,
            ),
            ft.TextField(
                ref=ref_password,
                label="Password",
                min_lines=1,
                max_lines=2,
            ),
            Alert,
        ],
        scroll="auto",
    )

def Register(page: ft.Page, params: Params, basket: Basket):
    ref_username = ft.Ref[ft.TextField]()
    ref_password = ft.Ref[ft.TextField]()
    c = ft.Checkbox(label="Admin", disabled=False)
    def register(e):
        Users().add(
            username=ref_username.current.value,
            password=ref_password.current.value,
            role="admin" if c.value else "user",
        )
        page.go("/login/")

    return ft.View(
        "/register/",
        controls=[
            ft.AppBar(
                title=ft.Text("Register"),
                actions=[
                    ft.IconButton(ft.icons.SAVE, on_click=register),
                ],
            ),
            ft.TextField(
                ref=ref_username,
                label="Username",
                min_lines=1,
                max_lines=2,
            ),
            ft.TextField(
                ref=ref_password,
                label="Password",
                min_lines=1,
                max_lines=2,
            ),
            c,
        ],
        scroll="auto",
    )