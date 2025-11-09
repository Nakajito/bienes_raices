import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def property_image(
    image_src: str, image_alt: str, image_title: str, price: float
) -> rx.Component:
    return rx.box(
        rx.image(
            src=image_src,
            alt=image_alt,
            border_radius="10px",
            loading="lazy",
            height="200px",
            width="100%",
            max_width="300px",
            object_fit="cover",
        ),
        rx.hstack(
            rx.text(
                f"{image_title}",
                font_weight="semibold",
                color=COLOR_STYLE["secondary_text"],
                font_size="16px",
            ),
            text_align="center",
            display="row",
            justify_content="center",
            margin_y="5px",
        ),
        rx.hstack(
            rx.text(
                f"${price:,.0f}",
                font_weight="bold",
                color=COLOR_STYLE["primary"],
                font_size="18px",
            ),
            text_align="center",
            display="row",
            justify_content="center",
            margin_y="5px",
        ),
        width="100%",
        display="flex",
        flex_direction="column",
        align_items="center",
    )
