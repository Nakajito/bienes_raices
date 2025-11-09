import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def mision() -> rx.Component:
    return rx.box(
        rx.heading(
            "About Us - Your Trusted Real Estate Partner",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
            margin_bottom="1rem",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
            as_="h1",
        ),
        rx.heading(
            "Our Mission and Commitment to Excellence",
            size=rx.breakpoints(initial="5", md="6", lg="7"),
            margin_bottom="1rem",
            margin_top="1.5rem",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
            as_="h2",
        ),
        rx.text(
            "At Bienes Raíces S.A., our mission is to connect people with their ideal homes, "
            "offering exceptional service and innovative real estate solutions. "
            "We are committed to providing expert advice, transparency, and dedication at every step of the process, "
            "ensuring total customer satisfaction. With years of experience in the real estate industry, "
            "we understand the importance of finding the perfect property that meets your unique needs and lifestyle. "
            "Our comprehensive approach combines market knowledge, technological innovation, and personalized service "
            "to deliver outstanding results for our clients.",
            font_size="1.2rem",
            line_height="1.6",
            color=COLOR_STYLE["secondary_text"],
            padding=rx.breakpoints(initial="1em 1em", md="1.5em 3em", lg="2em 8em"),
            text_align="center",
        ),
        rx.center(
            rx.image(
                src="/public/media-webp/about-800.webp",
                alt="Professional real estate team meeting with clients - Photo by Ketut Subiyanto",
                margin_bottom="1rem",
                height="20em",
                max_width="100%",
                border_radius="10px",
            ),
        ),
        rx.text(
            "We believe in building lasting relationships based on trust and respect, and in contributing positively "
            "to the communities where we operate. Our passion for real estate drives us to exceed expectations and be "
            "leaders in the market, always with integrity and professionalism. We offer a full range of services including "
            "property buying, selling, renting, investment consulting, market analysis, property valuation, and legal support "
            "coordination. Our team of experienced professionals is dedicated to making your real estate journey smooth, "
            "efficient, and successful. Whether you're a first-time homebuyer, seasoned investor, or looking to sell your property, "
            "we provide tailored solutions that align with your goals and budget.",
            font_size="1.2rem",
            line_height="1.6",
            color=COLOR_STYLE["secondary_text"],
            padding=rx.breakpoints(initial="1em 1em", md="1.5em 3em", lg="2em 8em"),
            text_align="center",
        ),
        padding="2rem",
        margin="0 auto",
        background_color=COLOR_STYLE["background"],
        min_height="100vh",
    )
