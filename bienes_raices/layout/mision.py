import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def mision() -> rx.Component:
    return rx.box(
        rx.heading(
            "Our Mission",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
            margin_bottom="1rem",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
        ),
        rx.text(
            "At Bienes Raíces S.A., our mission is to connect people with their ideal homes,offering exceptional service and innovative real estate solutions.We are committed to providing expert advice, transparency, and dedication at every step of the process,ensuring total customer satisfaction.",
            font_size="1.2rem",
            line_height="1.6",
            color=COLOR_STYLE["secondary_text"],
            padding=rx.breakpoints(initial="1em 1em", md="1.5em 3em", lg="2em 8em"),
            text_align="center",
        ),
        rx.center(
            rx.image(
                src="/public/media-webp/about-800.webp",
                alt="Foto de Ketut Subiyanto",
                margin_bottom="1rem",
                height="20em",
                max_width="100%",
                border_radius="10px",
            ),
        ),
        rx.text(
            "We believe in building lasting relationships based on trust and respect, and in contributing positively to the communities where we operate.Our passion for real estate drives us to exceed expectations and be leaders in the market, always with integrity and professionalism.",
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
