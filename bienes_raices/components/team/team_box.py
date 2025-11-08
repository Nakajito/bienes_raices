import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.team.team_text import team_text
from bienes_raices.components.team.team_avatar import team_avatar


def team_box(src: str, alt: str, position: str, name: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Avatar en la parte superior
            team_avatar(
                src=src,
                alt=alt,
            ),
            # Contenido del testimonio
            team_text(position=position, name=name),
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
