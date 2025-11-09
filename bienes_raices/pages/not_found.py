import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def not_found() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "404",
                size="9",
                color=COLOR_STYLE["primary_text"],
                font_weight="bold",
                as_="h1",
            ),
            rx.text(
                "La página que buscas no existe o fue movida.",
                color=COLOR_STYLE["secondary_text"],
                text_align="center",
                max_width="600px",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Ir al inicio",
                        size="3",
                        background_color=COLOR_STYLE["primary"],
                        color="white",
                        border_radius="8px",
                    ),
                    href="/",
                ),
                rx.link(
                    rx.button(
                        "Ver propiedades",
                        size="3",
                        background_color="transparent",
                        color=COLOR_STYLE["primary"],
                        border_radius="8px",
                        border=f"1px solid {COLOR_STYLE['primary']}",
                    ),
                    href="/properties",
                ),
                spacing="4",
                justify="center",
            ),
            spacing="6",
            padding=rx.breakpoints(initial="2em", md="4em"),
            align_items="center",
        ),
        width="100%",
        height="70vh",
        background_color=COLOR_STYLE.get("accent", "#f8fafc"),
    )
