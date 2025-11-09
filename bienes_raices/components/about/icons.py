import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def icons_about(icon: str, text: str) -> rx.Component:
    return (
        rx.vstack(
            rx.icon(icon, size=40, color=COLOR_STYLE["background"]),
            rx.text(
                text,
                size=rx.breakpoints(initial="3", md="4", lg="5"),
                font_weight="bold",
                color=COLOR_STYLE["background"],
            ),
            align_items="center",
            spacing=rx.breakpoints(initial="1", md="2"),
        ),
    )
