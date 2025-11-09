import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.testimonial.testimonial_box import testimonial_box


def testimonials() -> rx.Component:
    return rx.box(
        rx.heading(
            "Client Success Stories and Reviews",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
            font_weight="bold",
            margin_y="30px",
            color=COLOR_STYLE["primary_text"],
            text_align=rx.breakpoints(initial="center", md="left"),
            as_="h2",
        ),
        rx.flex(
            testimonial_box(
                src="/public/media-webp/avatars/avatar_01-400.webp",
                alt="Portrait photo of John Smith, satisfied real estate client",
                testimonial="This service was exceptional and helped me find the perfect home!",
                rate=5,
                author="Jane Doe",
            ),
            testimonial_box(
                src="/public/media-webp/avatars/avatar_02-400.webp",
                alt="Portrait photo of Emily Johnson, happy homeowner",
                testimonial="A seamless experience from start to finish. Highly recommended!",
                rate=4,
                author="Eva Davis",
            ),
            testimonial_box(
                src="/public/media-webp/avatars/avatar_03-400.webp",
                alt="Portrait photo of Michael Brown, satisfied customer",
                testimonial="I couldn't have asked for a better experience. Thank you!",
                rate=5,
                author="Michael Brown",
            ),
            direction="row",
            wrap="wrap",
            justify="center",
            align="stretch",
            gap="2em",
            width="100%",
        ),
        background_color=COLOR_STYLE["accent"],
        padding="3em",
        padding_x=rx.breakpoints(initial="1em", md="2em", lg="3em"),
        margin_x="auto",
    )
