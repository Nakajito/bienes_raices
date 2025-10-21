import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
        color=COLOR_STYLE["background"],
        text_decoration="none",
        _hover={"color": COLOR_STYLE["secondary"]},
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
        ),
        href=url,
    )
