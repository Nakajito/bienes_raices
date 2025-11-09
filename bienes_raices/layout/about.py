import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.about.icons import icons_about


def about() -> rx.Component:
    return rx.box(
        rx.heading(
            "We help you find the best properties for sale and rent!",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
            font_weight="bold",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
            margin_bottom=rx.breakpoints(initial="1em", md="1.5em", lg="2em"),
        ),
        rx.vstack(
            rx.text(
                "Welcome to Real Estate, your trusted partner in finding the perfect property. "
                "With years of experience in the real estate market, we are committed to providing "
                "exceptional service and personalized solutions to meet your unique needs.",
                size=rx.breakpoints(initial="3", md="4", lg="5"),
                color=COLOR_STYLE["secondary_text"],
            ),
            # Cambio de hstack a flex para que se apile en móviles
            rx.flex(
                icons_about("building", "+500 Properties"),
                icons_about("home", "+300 Homes"),
                icons_about("users", "+200 Clients"),
                icons_about("trophy", "15 Awards"),
                direction=rx.breakpoints(initial="column", md="row"),
                justify="between",
                align="center",
                width="100%",
                padding=rx.breakpoints(initial="1em", md="2em", lg="3em"),
                spacing=rx.breakpoints(initial="3", md="4"),
                wrap="wrap",
            ),
            rx.text(
                "Our team of dedicated professionals is here to guide you through every step of the "
                "buying, selling, or renting process. We pride ourselves on our extensive knowledge "
                "of the local market and our ability to connect clients with their ideal properties.",
                size=rx.breakpoints(initial="3", md="4", lg="5"),
                color=COLOR_STYLE["secondary_text"],
            ),
            text_align="center",
            margin_top="1em",
            spacing=rx.breakpoints(initial="3", md="4"),
        ),
        height="auto",
        padding=rx.breakpoints(initial="2em", md="3em", lg="5em"),
        padding_x=rx.breakpoints(initial="1em", md="2em", lg="3em"),
        bg=COLOR_STYLE["accent"],
        margin="auto",
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
    )
