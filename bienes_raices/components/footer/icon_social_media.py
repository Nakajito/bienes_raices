import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def icon_social_media(social_media: str, href: str):
    return rx.link(
        rx.icon(social_media, size=20, color=COLOR_STYLE["background"]),
        href=href,
        is_external=True,
    )
