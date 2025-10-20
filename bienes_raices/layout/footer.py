import reflex as rx
import datetime
from bienes_raices.styles.styles import COLOR_STYLE


def footer():
    return rx.hstack(
        rx.hstack(
            rx.link(
                rx.icon("facebook", size=20, color=COLOR_STYLE["primary_text"]),
                href="https://www.facebook.com",
                is_external=True,
            ),
            rx.link(
                rx.icon("instagram", size=20, color=COLOR_STYLE["primary_text"]),
                href="https://www.instagram.com",
                is_external=True,
            ),
            rx.link(
                rx.icon("twitter", size=20, color=COLOR_STYLE["primary_text"]),
                href="https://www.twitter.com",
                is_external=True,
            ),
            rx.link(
                rx.icon("youtube", size=20, color=COLOR_STYLE["primary_text"]),
                href="https://www.youtube.com",
                is_external=True,
            ),
            width="30%",
            justify="center",
        ),
        rx.hstack(
            rx.text(
                f"Todos los derechos reservados © {datetime.datetime.now().year}",
                color=COLOR_STYLE["primary_text"],
                weight="bold",
            ),
            width="40%",
            # background_color=COLOR_STYLE["background"],
            text_align="center",
            justify="center",
        ),
        rx.hstack(
            rx.link(
                rx.text(
                    "Desarrollado por Nakajito",
                    color=COLOR_STYLE["primary_text"],
                ),
                text_decoration="none",
                href="https://danielbonilla.vercel.app/",
                is_external=True,
                weight="bold",
            ),
            width="30%",
            # padding="10px",
            # background_color=COLOR_STYLE["background"],
            text_align="center",
            justify="center",
        ),
        justify="between",
        align_items="center",
        height="80px",
    )
