import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.about.icons import icons_about


def about() -> rx.Component:
    return rx.box(
        rx.heading(
            "We help you find the best properties for sale and rent!",
            size="8",
            font_weight="bold",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
            margin_bottom="2em",
        ),
        rx.vstack(
            rx.text(
                "Welcome to Real Estate, your trusted partner in finding the perfect property. "
                "With years of experience in the real estate market, we are committed to providing "
                "exceptional service and personalized solutions to meet your unique needs.",
                size="5",
                color=COLOR_STYLE["secondary_text"],
                # margin_top="1em",
            ),
            rx.hstack(
                icons_about("building", "+500 Properties"),
                icons_about("home", "+300 Homes"),
                icons_about("users", "+200 Clients"),
                icons_about("trophy", "15 Awards"),
                justify_content="space-around",
                width="100%",
                padding="3em",
            ),
            rx.text(
                "Our team of dedicated professionals is here to guide you through every step of the "
                "buying, selling, or renting process. We pride ourselves on our extensive knowledge "
                "of the local market and our ability to connect clients with their ideal properties.",
                size="5",
                # margin_top="1em",
                color=COLOR_STYLE["secondary_text"],
            ),
            text_align="center",
            margin_top="1em",
        ),
        height="auto",
        padding="5em",
        bg=COLOR_STYLE["accent"],
        margin="auto",
        # propiedades para centrar el box
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
    )
