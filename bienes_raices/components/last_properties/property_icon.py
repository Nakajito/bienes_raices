import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def property_icon(icon: str, label: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(icon, color=COLOR_STYLE["primary"], size=25),
            rx.text(
                label,
                margin_left="5px",
                color=COLOR_STYLE["secondary_text"],
                font_size="14px",
            ),
            display="flex",
            flex_direction="column",
            align_items="center",
        ),
        display="flex",
        flex_direction="column",
        align_items="center",
    )
