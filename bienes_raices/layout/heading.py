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
            background='url("/public/media-webp/cover-1200.webp")',
            background_size="cover",
            background_repeat="no-repeat",
            background_position="center",
            # filter="blur(1px)",  # Blur directo a la imagen
            transform="scale(1.1)",  # Evita bordes borrosos
            z_index="1",  # Capa de fondo
            alt="Foto de Alex Staudinger en Unsplash",
        ),
        # Contenido
        rx.vstack(
            rx.heading(
                "Welcome to Real Estate",
                size=rx.breakpoints(initial="7", md="8", lg="9"),
                weight="bold",
                color=COLOR_STYLE["primary_text"],
                as_="h1",
                text_align=rx.breakpoints(initial="center", md="right"),
            ),
            rx.text(
                "Find your dream home with us!",
                size=rx.breakpoints(initial="5", md="6", lg="8"),
                color=COLOR_STYLE["secondary_text"],
                text_align=rx.breakpoints(initial="center", md="right"),
            ),
            rx.link(
                rx.button(
                    "Get Started",
                    background_color=COLOR_STYLE["primary"],
                    color="white",
                    _hover={"background_color": COLOR_STYLE["secondary"]},
                    size=rx.breakpoints(initial="3", lg="4"),
                ),
                href="#",
                text_decoration="none",
            ),
            justify_content="flex-start",
            align_items=rx.breakpoints(initial="center", md="flex-end"),
            position="relative",
            z_index="2",
            height="100%",
            spacing=rx.breakpoints(initial="2", md="3"),
            padding_top=rx.breakpoints(initial="2em", md="3em", lg="4em"),
            padding_x=rx.breakpoints(initial="1em", md="2em"),
        ),
        position="relative",
        padding=rx.breakpoints(initial="1em", md="2em"),
        padding_bottom=rx.breakpoints(initial="2em", md="3em", lg="4em"),
        height=rx.breakpoints(initial="60vh", md="80vh", lg="100vh"),
        overflow="hidden",
        display="flex",
        align_items="flex-start",
        justify_content=rx.breakpoints(initial="center", md="flex-end"),
    )
