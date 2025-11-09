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
            as_="h2",
        ),
        rx.vstack(
            rx.text(
                "Welcome to Real Estate, your trusted partner in finding the perfect property. "
                "With years of experience in the real estate market, we are committed to providing "
                "exceptional service and personalized solutions to meet your unique needs. "
                "Our dedicated team of professionals understands that buying, selling, or renting a property "
                "is one of the most important decisions you'll make, and we're here to guide you every step of the way. "
                "We pride ourselves on our deep knowledge of the local market, transparent communication, "
                "and unwavering commitment to client satisfaction.",
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
                "of the local market and our ability to connect clients with their ideal properties. "
                "Whether you're a first-time homebuyer, an experienced investor, or looking to sell your property, "
                "we provide tailored solutions that align with your goals and budget. Our comprehensive services "
                "include property valuation, market analysis, negotiation support, legal assistance coordination, "
                "and post-sale support. We leverage cutting-edge technology and traditional real estate expertise "
                "to ensure you get the best possible outcome. Join our family of satisfied clients who have found "
                "their dream homes and successful investments through our personalized approach to real estate.",
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
