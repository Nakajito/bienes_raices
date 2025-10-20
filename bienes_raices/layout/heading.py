import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def heading() -> rx.Component:
    return rx.box(
        # Imagen de fondo con blur directo
        rx.box(
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background='url("/media/cover.jpg")',
            background_size="cover",
            background_repeat="no-repeat",
            background_position="center",
            # filter="blur(1px)",  # Blur directo a la imagen
            transform="scale(1.1)",  # Evita bordes borrosos
            z_index="1",  # Capa de fondo
            alt="Foto de Alex Staudinger: https://www.pexels.com/es-es/foto/sun-piercing-de-la-casa-de-hormigon-marron-cerca-del-mar-1732414/",
        ),
        # Contenido
        rx.vstack(
            rx.heading(
                "Welcome to Real Estate",
                size="9",
                weight="bold",
                color=COLOR_STYLE["primary_text"],
                as_="h1",
                text_align="right",  # Alinear texto a la derecha
            ),
            rx.text(
                "Find your dream home with us!",
                size="8",
                color=COLOR_STYLE["secondary_text"],
                text_align="right",  # Alinear texto a la derecha
            ),
            rx.link(
                rx.button(
                    "Get Started",
                    background_color=COLOR_STYLE["primary"],
                    color="white",
                    _hover={"background_color": COLOR_STYLE["secondary"]},
                    size="4",
                ),
                href="#",
                text_decoration="none",
            ),
            justify_content="flex-start",  # Alinear al inicio (arriba)
            align_items="flex-end",  # Alinear a la derecha
            position="relative",
            z_index="2",  # Contenido por encima
            height="100%",  # Ocupa toda la altura disponible
            spacing="3",  # Espacio entre elementos
            padding_top="4em",  # Separación desde arriba
        ),
        position="relative",
        padding="2em",
        padding_bottom="4em",
        height="100vh",
        overflow="hidden",
        display="flex",
        align_items="flex-start",  # Alinear al inicio (arriba)
        justify_content="flex-end",  # Alinear al final (derecha)
    )
