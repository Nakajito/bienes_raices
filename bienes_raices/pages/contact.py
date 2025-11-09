import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.layout.footer import footer
from bienes_raices.components.contact.contact_form import contact_form


def contact() -> rx.Component:
    return rx.box(
        navbar_icons(),
        rx.vstack(
            # Encabezado de la sección
            rx.vstack(
                rx.heading(
                    "Contact Our Expert Real Estate Agents Today",
                    size=rx.breakpoints(initial="6", md="7", lg="8"),
                    font_weight="bold",
                    color=COLOR_STYLE["primary_text"],
                    text_align="center",
                    as_="h1",
                ),
                rx.text(
                    "Ready to find your dream home? Contact us today and one of our expert agents will help you get started on your journey.",
                    size=rx.breakpoints(initial="3", md="4", lg="5"),
                    color=COLOR_STYLE["secondary_text"],
                    text_align="center",
                    max_width="600px",
                    line_height="1.6",
                    padding_x=rx.breakpoints(initial="1em", md="1.5em", lg="2em"),
                ),
                spacing="4",
                align_items="center",
            ),
            contact_form(),
            background_color=COLOR_STYLE["background"],
            min_height="100vh",
            padding_y="3em",
            padding_x=rx.breakpoints(initial="1em", md="1.5em", lg="2em"),
            align_items="center",
        ),
        footer(),
    )
