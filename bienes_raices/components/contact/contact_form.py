import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.contact.contact_input import contact_input
from bienes_raices.components.contact.contact_text_area import contact_text_area


def contact_form() -> rx.Component:
    return rx.box(
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
    )
