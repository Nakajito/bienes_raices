import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def icons_about(icon: str, text: str) -> rx.Component:
    return (
        rx.vstack(
            rx.icon(icon, size=50, color=COLOR_STYLE["background"]),
            rx.text(
                text,
                size="5",
                font_weight="bold",
                color=COLOR_STYLE["background"],
            ),
            align_items="center",
        ),
    )
