import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def team_avatar(src: str, alt: str) -> rx.Component:
    return rx.avatar(
        src=src,
        alt=alt,
        radius="full",
        size="8",
    )
