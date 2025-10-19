import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def footer():
    return rx.box(
        rx.text("Todos los derechos reservados © 2024", color=COLOR_STYLE["secondary"]),
        width="100%",
        padding="20px",
        background_color=COLOR_STYLE["background"],
        text_align="center",
    )
