from flet import View, Page, AppBar, NavigationBar
from repath import match
from typing import Callable


class Basket:
    def get(self, var: str):
        try:
            return self.__getattribute__(var)
        except AttributeError:
            pass

    def delete(self, var: str):
        try:
            self.__delattr__(var)
        except AttributeError:
            pass

    def get_all(self):
        return self.__dict__

    def __str__(self) -> str:
        show = ""
        dic = self.__dict__
        for key in dic:
            show = show + f"{key} = {dic[key]}\n"
        return show[0:-1]


class Params:
    def __init__(self, dic=dict) -> None:
        for i in dic:
            self.__setattr__(str(i), str(dic[i]))

    def get(self, var: str):
        try:
            return self.__getattribute__(var)
        except AttributeError:
            pass

    def delete(self, var: str):
        try:
            self.__delattr__(var)
        except AttributeError:
            pass

    def get_all(self):
        return self.__dict__

    def __str__(self) -> str:
        show = ""
        dic = self.__dict__
        for key in dic:
            show = show + f"{key} = {dic[key]}\n"
        return show[0:-1]

# class Params(dict):
#     pass

def route_str(route):
    if type(route) == str:
        return route
    else:
        return str(route.route)


def path(
    url: str,
    clear: bool,
    view: Callable[[Page, Params, Basket], View],
    middleware: Callable[[Page, Params, Basket], None] = None,
):
    return [url, clear, view, middleware]


class Routing:
    def __init__(
        self,
        page: Page,
        app_routes: list,
        middleware: Callable[[Page, Params, Basket], None] = None,
        async_is=False,
        appbar: AppBar = None,
        navigation_bar: NavigationBar = None,
    ):
        self.async_is = async_is
        self.page = page
        self.app_routes = app_routes
        self.appbar = appbar
        self.navigation_bar = navigation_bar
        self.__middleware = middleware
        self.__params = Params({})
        self.__basket = Basket()
        if self.async_is:
            self.page.on_route_change = self.change_route_async
            self.page.on_view_pop = self.view_pop_async
        else:
            self.page.on_route_change = self.change_route
            self.page.on_view_pop = self.view_pop

    def change_route(self, route):
        notfound = True
        for url in self.app_routes:
            path_match = match(url[0], self.page.route)
            if path_match:
                self.__params = Params(path_match.groupdict())
                if self.__middleware != None:
                    self.__middleware(
                        page=self.page, params=self.__params, basket=self.__basket
                    )
                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return

                if url[3] != None:
                    url[3](page=self.page, params=self.__params, basket=self.__basket)

                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return

                if url[1]:
                    self.page.views.clear()
                view = url[2](
                    page=self.page, params=self.__params, basket=self.__basket
                )
                view.appbar = self.appbar
                view.navigation_bar = self.navigation_bar
                self.page.views.append(view)
                notfound = False
                break
        if notfound:
            self.__params = Params({"url": self.page.route})
            self.page.views.append(
                self.not_found_view(
                    page=self.page, params=self.__params, basket=self.__basket
                )
            )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    async def change_route_async(self, route):
        notfound = True
        for url in self.app_routes:
            path_match = match(url[0], self.page.route)
            if path_match:
                self.__params = Params(path_match.groupdict())
                if self.__middleware != None:
                    await self.__middleware(
                        page=self.page, params=self.__params, basket=self.__basket
                    )
                if self.page.route != route_str(route=route):
                    await self.page.go_async(self.page.route)
                    return

                if url[3] != None:
                    await url[3](
                        page=self.page, params=self.__params, basket=self.__basket
                    )

                if self.page.route != route_str(route=route):
                    await self.page.go_async(self.page.route)
                    return

                if url[1]:
                    self.page.views.clear()
                view = await url[2](
                    page=self.page, params=self.__params, basket=self.__basket
                )
                view.appbar = self.appbar
                view.navigation_bar = self.navigation_bar

                self.page.views.append(view)
                notfound = False
                break
        if notfound:
            self.__params = Params({"url": self.page.route})
            self.page.views.append(
                await self.not_found_view(
                    page=self.page, params=self.__params, basket=self.__basket
                )
            )
        await self.page.update_async()

    async def view_pop_async(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        await self.page.go_async(top_view.route)
