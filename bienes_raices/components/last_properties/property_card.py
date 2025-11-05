import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.last_properties.property_image import property_image
from bienes_raices.components.last_properties.property_icon import property_icon


def property_card(
    image_src: str,
    image_alt: str,
    image_title: str,
    price: float,
    beds: int,
    baths: int,
    area_sqft: int,
    has_garage: bool,
) -> rx.Component:
    """Create a property card component."""

    icons = [
        property_icon(icon="bed-double", label=f"{beds} Beds"),
        property_icon(icon="bath", label=f"{baths} Baths"),
        property_icon(icon="ruler", label=f"{area_sqft} sqft"),
    ]
    if has_garage:
        icons.append(property_icon(icon="circle-parking", label="Garage"))

    return rx.box(
        property_image(
            image_src=image_src,
            image_alt=image_alt,
            image_title=image_title,
            price=price,
        ),
        rx.hstack(
            *icons,
            spacing="3",
            justify="center",
            width="100%",
            padding="1em",
        ),
        padding="1.5em",
        margin="1em",
        background_color="white",
        border_radius="12px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        border="1px solid #e2e8f0",
        width="350px",
        max_width="400px",
        display="flex",
        flex_direction="column",
        justify_content="space-between",
        align_items="center",
    )
