import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.testimonial.testimonial_text import testimonial_text
from bienes_raices.components.testimonial.avatar import testimonial_avatar


def testimonial_box(
    src: str, alt: str, testimonial: str, rate: int, author: str
) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Avatar en la parte superior
            testimonial_avatar(
                src=src,
                alt=alt,
            ),
            # Contenido del testimonio
            testimonial_text(
                testimonial=testimonial,
                rate=rate,
                author=author,
            ),
            align_items="center",
            spacing="3",
            width="100%",
        ),
        # Propiedades del contenedor
        padding=["1em", "1.5em", "2em"],  # Responsive padding
        margin=["0.5em", "1em"],  # Margen entre elementos
        background_color=COLOR_STYLE["background"],
        border_radius="12px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        border="1px solid #e2e8f0",
        # Tamaño responsive
        width=["100%", "300px", "350px"],  # Ancho responsive
        max_width="400px",  # Ancho máximo
        min_height=["200px", "250px", "280px"],  # Altura mínima responsive
        # Flexbox para centrar contenido
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
    )
