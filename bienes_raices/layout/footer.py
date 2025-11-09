import reflex as rx
import datetime
from bienes_raices.styles.styles import COLOR_STYLE
import bienes_raices.components.footer.icon_social_media as icons


def footer():
    return rx.box(
        # Contenedor principal del footer
        rx.vstack(
            # Sección superior - Links y redes sociales
            rx.flex(
                # Columna 1 - Información de la empresa
                rx.vstack(
                    rx.heading(
                        "Real Estate",
                        size="6",
                        color="white",
                        font_weight="bold",
                        margin_bottom="1em",
                        as_="div",
                    ),
                    rx.text(
                        "Find your dream home with us. We offer the best properties in the market.",
                        color="rgba(255, 255, 255, 0.8)",
                        font_size="14px",
                        line_height="1.6",
                        max_width="300px",
                    ),
                    align_items="flex-start",
                    spacing="2",
                    width="100%",
                ),
                # Columna 2 - Links rápidos
                rx.vstack(
                    rx.text(
                        "Quick Links",
                        color="white",
                        font_weight="bold",
                        font_size="16px",
                        margin_bottom="1em",
                    ),
                    rx.link(
                        "Home",
                        href="/",
                        color="rgba(255, 255, 255, 0.8)",
                        font_size="14px",
                        _hover={"color": "white", "text_decoration": "underline"},
                    ),
                    rx.link(
                        "About Us",
                        href="/about_page",
                        color="rgba(255, 255, 255, 0.8)",
                        font_size="14px",
                        _hover={"color": "white", "text_decoration": "underline"},
                    ),
                    rx.link(
                        "Properties",
                        href="/properties",
                        color="rgba(255, 255, 255, 0.8)",
                        font_size="14px",
                        _hover={"color": "white", "text_decoration": "underline"},
                    ),
                    rx.link(
                        "Contact",
                        href="/contact",
                        color="rgba(255, 255, 255, 0.8)",
                        font_size="14px",
                        _hover={"color": "white", "text_decoration": "underline"},
                    ),
                    align_items="flex-start",
                    spacing="2",
                    width="100%",
                ),
                # Columna 3 - Redes sociales
                rx.vstack(
                    rx.text(
                        "Follow Us",
                        color="white",
                        font_weight="bold",
                        font_size="16px",
                        margin_bottom="1em",
                    ),
                    rx.hstack(
                        icons.icon_social_media("facebook", "https://www.facebook.com"),
                        icons.icon_social_media(
                            "instagram", "https://www.instagram.com"
                        ),
                        icons.icon_social_media("twitter", "https://www.twitter.com"),
                        icons.icon_social_media("youtube", "https://www.youtube.com"),
                        spacing="4",
                    ),
                    rx.text(
                        "Stay connected with us on social media",
                        color="rgba(255, 255, 255, 0.8)",
                        font_size="14px",
                        line_height="1.6",
                        margin_top="1em",
                    ),
                    align_items="flex-start",
                    spacing="2",
                    width="100%",
                ),
                # Propiedades del flex
                direction=rx.breakpoints(initial="column", lg="row"),
                wrap="wrap",
                justify="between",
                align="start",
                gap="3em",
                width="100%",
                max_width="1200px",
                margin_x="auto",
            ),
            # Divisor
            rx.divider(
                margin_y="2em",
                border_color="rgba(255, 255, 255, 0.2)",
                width="100%",
            ),
            # Sección inferior - Copyright y créditos
            rx.flex(
                rx.text(
                    f"© {datetime.datetime.now().year} Real Estate. All rights reserved.",
                    color="rgba(255, 255, 255, 0.8)",
                    font_size="14px",
                    text_align=rx.breakpoints(initial="center", lg="left"),
                ),
                rx.link(
                    rx.hstack(
                        rx.text(
                            "Developed by",
                            color="rgba(255, 255, 255, 0.8)",
                            font_size="14px",
                        ),
                        rx.text(
                            "Nakajito",
                            color="white",
                            font_weight="bold",
                            font_size="14px",
                        ),
                        spacing="1",
                    ),
                    href="https://danielbonilla.vercel.app/",
                    is_external=True,
                    text_decoration="none",
                    _hover={"opacity": "0.8"},
                ),
                direction=rx.breakpoints(initial="column", lg="row"),
                wrap="wrap",
                justify=rx.breakpoints(initial="center", lg="between"),
                align="center",
                gap="1em",
                width="100%",
                max_width="1200px",
                margin_x="auto",
            ),
            spacing="4",
            width="100%",
            padding="4em 2em",
        ),
        # Estilos del contenedor principal
        background=f"linear-gradient(135deg, {COLOR_STYLE['primary']} 0%, #1e3a8a 100%)",
        width="100%",
        position="relative",
        box_shadow="0 -4px 6px rgba(0, 0, 0, 0.1)",
    )
