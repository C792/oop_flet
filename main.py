import flet as ft
from db import create_tables

create_tables()


def main(page: ft.Page):
    pass

ft.app(target=main, view=ft.WEB_BROWSER)
