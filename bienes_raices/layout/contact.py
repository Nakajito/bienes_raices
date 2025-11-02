import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.contact.contact_input import contact_input
from bienes_raices.components.contact.contact_text_area import contact_text_area


def contact_section() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Encabezado de la sección
            rx.vstack(
                rx.heading(
                    "Contact Us",
                    size="8",
                    font_weight="bold",
                    color=COLOR_STYLE["primary_text"],
                    text_align="center",
                ),
                rx.text(
                    "Ready to find your dream home? Contact us today and one of our expert agents will help you get started on your journey.",
                    size="5",
                    color=COLOR_STYLE["secondary_text"],
                    text_align="center",
                    max_width="600px",
                    line_height="1.6",
                ),
                spacing="4",
                align_items="center",
            ),
            # Formulario de contacto
            rx.box(
                rx.form(
                    rx.vstack(
                        contact_input(
                            label="Name *",
                            type="text",
                        ),
                        contact_input(
                            label="Email *",
                            type="email",
                        ),
                        contact_input(
                            label="Phone",
                            type="tel",
                        ),
                        contact_text_area(
                            label="Message",
                        ),
                        rx.button(
                            "Send Message",
                            type="submit",
                            size="3",
                            background_color=COLOR_STYLE["secondary"],
                            color="white",
                            border_radius="8px",
                            padding="16px 32px",
                            font_weight="semibold",
                        ),
                        spacing="5",
                        width="100%",
                    ),
                    width="100%",
                ),
                background_color=COLOR_STYLE["accent"],
                padding="3em",
                border_radius="12px",
                box_shadow="0 8px 25px rgba(0,0,0,0.1)",
                border="1px solid #f1f5f9",
                max_width="600px",
                width="100%",
            ),
            spacing="6",
            align_items="center",
            max_width="800px",
            width="100%",
            padding_x="2em",
        ),
        background_color=COLOR_STYLE["background"],
        min_height="100vh",
        padding_y="3em",
    )
