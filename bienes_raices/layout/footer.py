import reflex as rx
import datetime
from bienes_raices.styles.styles import COLOR_STYLE
import bienes_raices.components.footer.icon_social_media as icons


def footer():
    return rx.hstack(
        rx.hstack(
            icons.icon_social_media("facebook", "https://www.facebook.com"),
            icons.icon_social_media("instagram", "https://www.instagram.com"),
            icons.icon_social_media("twitter", "https://www.twitter.com"),
            icons.icon_social_media("youtube", "https://www.youtube.com"),
            width="30%",
            justify="center",
        ),
        rx.hstack(
            rx.text(
                f"Todos los derechos reservados © {datetime.datetime.now().year}",
                color=COLOR_STYLE["background"],
                weight="bold",
            ),
            width="40%",
            text_align="center",
            justify="center",
        ),
        rx.hstack(
            rx.link(
                rx.text(
                    "Desarrollado por Nakajito",
                    color=COLOR_STYLE["background"],
                ),
                text_decoration="none",
                href="https://danielbonilla.vercel.app/",
                is_external=True,
                weight="bold",
            ),
            width="30%",
            text_align="center",
            justify="center",
        ),
        justify="between",
        align_items="center",
        height="80px",
        background_color=COLOR_STYLE["primary"],
    )
