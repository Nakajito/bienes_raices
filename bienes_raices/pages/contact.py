import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.layout.footer import footer


def contact() -> rx.Component:
    return rx.box(
        navbar_icons(),
        rx.heading(
            "Contact Us",
            font_weight="bold",
            size="8",
            margin_y="30px",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
        ),
        rx.form(
            rx.input(placeholder="Your Name", margin_y="10px"),
            rx.input(placeholder="Your Email", margin_y="10px"),
            rx.text_area(placeholder="Your Message", margin_y="10px"),
            rx.button("Send", type="submit", margin_y="10px"),
        ),
        footer(),
        background_color=COLOR_STYLE["background"],
        margin_x="auto",
    )
