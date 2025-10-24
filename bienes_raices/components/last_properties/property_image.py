import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def property_image(
    image_src: str, image_alt: str, image_title: str, price: int
) -> rx.Component:
    return rx.box(
        rx.image(
            src=image_src,
            alt=image_alt,
            border_radius="10px",
            loading="lazy",
            height="200px",
            width="300px",
            object_fit="cover",
        ),
        rx.hstack(
            rx.text(
                f"{image_title} $ {price:,.2f}",
                font_weight="semibold",
                color=COLOR_STYLE["secondary_text"],
            ),
            text_align="center",
            display="row",
            justify_content="center",
            margin_y="10px",
        ),
    )
