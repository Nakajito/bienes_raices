import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.layout.about import about
from bienes_raices.layout.footer import footer


def about_page() -> rx.Component:
    return rx.box(
        navbar_icons(),
        about(),
        footer(),
    )
