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
    property_id: str = "1",
) -> rx.Component:
    """Create a property card component."""

    icons = [
        property_icon(icon="bed-double", label=f"{beds} Beds"),
        property_icon(icon="bath", label=f"{baths} Baths"),
        property_icon(icon="ruler", label=f"{area_sqft} sqft"),
    ]
    if has_garage:
        icons.append(property_icon(icon="circle-parking", label="Garage"))

    return rx.link(
        rx.box(
            property_image(
                image_src=image_src,
                image_alt=image_alt,
                image_title=image_title,
                price=price,
            ),
            rx.flex(
                *icons,
                spacing="3",
                justify="center",
                align="center",
                width="100%",
                padding="1em",
                wrap="wrap",
                direction="row",
            ),
            rx.button(
                "View Details",
                size="2",
                width="100%",
                background_color=COLOR_STYLE["primary"],
                color="white",
                _hover={"background_color": COLOR_STYLE["hover"]},
            ),
            padding="1.5em",
            margin="1em",
            background_color="white",
            border_radius="12px",
            box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
            border="1px solid #e2e8f0",
            width=rx.breakpoints(initial="100%", md="calc(50% - 1em)", lg="350px"),
            max_width="400px",
            min_width="250px",
            display="flex",
            flex_direction="column",
            justify_content="space-between",
            align_items="center",
            transition="transform 0.2s, box-shadow 0.2s",
            _hover={
                "transform": "translateY(-5px)",
                "box_shadow": "0 8px 16px rgba(0, 0, 0, 0.15)",
            },
        ),
        href=f"/property/{property_id}",
        text_decoration="none",
        aria_label=f"View details for {image_title} - ${price:,}",
    )
