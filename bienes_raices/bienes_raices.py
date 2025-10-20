import reflex as rx
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.layout.heading import heading
from bienes_raices.layout.footer import footer
from bienes_raices.styles.styles import COLOR_STYLE
from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    """The main page of the app."""
    return rx.box(
        navbar_icons(),
        heading(),
        footer(),
        bg=COLOR_STYLE["background"],
    )


app = rx.App()
app.add_page(index)
