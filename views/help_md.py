import flet as ft
from views.routing import Params, Basket

md = """
# Help
```
This is an H1
=============
```
This is an H1
=============

```
This is an H2
-------------
```
This is an H2
-------------
`# This is an H1`
# This is an H1
`## This is an H2`
## This is an H2
`###### This is an H6`
###### This is an H6
## Link
`[inline-style](https://www.google.com)`

[inline-style](https://www.google.com)

## Style
`> Blockquote`
> Blockquote

`* List 1`
* List 1

`- List 2`
- List 2

`+ List 3`
+ List 3

`1. Numbered List`
1. Numbered List

## Image
`![alt text](image url)`

![alt text](https://i.namu.wiki/i/Po7PIMfBUi0Ic-opSmMUmrniTg6cs--FoILMuog4y-e4dWhNpRwUk1KNSrI0T7VItki4dBY6Z8I6NyeftD0JyQ.webp)

## Syntax
|Syntax                                 |Result                               |
|---------------------------------------|-------------------------------------|
|`1. Numbered List`                     |1. Numbered List                     |
|`[ ] Checkbox`                         |[ ] Checkbox                         |
|`[x] Checked`                          |[x] Checked                          |
|`*italic 1*`                           |*italic 1*                           |
|`_italic 2_`                           | _italic 2_                          |
|`**bold 1**`                           |**bold 1**                           |
|`__bold 2__`                           |__bold 2__                           |
|`This is a ~~strikethrough~~`          |This is a ~~strikethrough~~          |
|`***italic bold 1***`                  |***italic bold 1***                  |
|`___italic bold 2___`                  |___italic bold 2___                  |
|`***~~italic bold strikethrough 1~~***`|***~~italic bold strikethrough 1~~***|
|`~~***italic bold strikethrough 2***~~`|~~***italic bold strikethrough 2***~~|

## Code blocks
` ```python `

` for i in range(10): `

`     print("Hello, World!") `

` ``` `
```python
for i in range(10):
    print("Hello, World!")
```
"""

def Help(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        f"/new_post/help/",
        controls=[
            ft.AppBar(
                title=ft.Text("DSHub - Markdown Help"),
            ),
            ft.Markdown(
                md,
                selectable=False,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                code_theme="atom-one-dark",
                code_style=ft.TextStyle(font_family="Consolas"),
                on_tap_link=lambda e: page.launch_url(e.data),
            ),
        ],
        scroll="auto",
    )