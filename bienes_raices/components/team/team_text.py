import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def team_text(position: str, name: str) -> rx.Component:
    return (
        rx.vstack(
            rx.text(position, color=COLOR_STYLE["primary_text"]),
            rx.text(name, color=COLOR_STYLE["secondary_text"]),
            align_items="center",
        ),
    )
