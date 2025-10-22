import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.last_properties.property_image import property_image
from bienes_raices.components.last_properties.property_icon import property_icon


def last_properties() -> rx.Component:
    return rx.box(
        rx.heading(
            "Latest Properties",
            size="6",
            font_weight="bold",
            margin_y="30px",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
        ),
        rx.grid(
            rx.box(
                property_image(
                    image_src="/media/property_01.jpg",
                    image_alt="Foto de Pixabay: https://www.pexels.com/es-es/foto/casa-de-madera-marron-y-blanca-164558/",
                    image_title="House for Sale",
                    price=250000,
                ),
                rx.hstack(
                    property_icon(
                        icon="bed-double",
                        label="3 Beds",
                    ),
                    property_icon(
                        icon="bath",
                        label="2 Baths",
                    ),
                    property_icon(
                        icon="ruler",
                        label="1,500 sqft",
                    ),
                    property_icon(
                        icon="circle-parking",
                        label="Garage",
                    ),
                ),
                display="flex",
                flex_direction="column",
                justify_content="space-around",
                align_items="center",
            ),
            rx.box(
                property_image(
                    image_src="/media/property_02.jpg",
                    image_alt="Foto de Pixasquare Studio: https://www.pexels.com/es-es/foto/casa-blanca-de-2-plantas-cerca-de-arboles-1115804/",
                    image_title="Apartment for Rent",
                    price=1200,
                ),
                rx.hstack(
                    property_icon(
                        icon="bed-double",
                        label="3 Beds",
                    ),
                    property_icon(
                        icon="bath",
                        label="2 Baths",
                    ),
                    property_icon(
                        icon="ruler",
                        label="1,500 sqft",
                    ),
                    property_icon(
                        icon="circle-parking",
                        label="Garage",
                    ),
                ),
                display="flex",
                flex_direction="column",
                justify_content="space-around",
                align_items="center",
            ),
            rx.box(
                property_image(
                    image_src="/media/property_03.jpg",
                    image_alt="Foto de Pixabay: https://www.pexels.com/es-es/foto/casa-de-madera-marron-y-beige-bajo-un-cielo-azul-221540/",
                    image_title="Country House",
                    price=300000,
                ),
                rx.hstack(
                    property_icon(
                        icon="bed-double",
                        label="3 Beds",
                    ),
                    property_icon(
                        icon="bath",
                        label="2 Baths",
                    ),
                    property_icon(
                        icon="ruler",
                        label="1,500 sqft",
                    ),
                    property_icon(
                        icon="circle-parking",
                        label="Garage",
                    ),
                ),
                display="flex",
                flex_direction="column",
                justify_content="space-around",
                align_items="center",
            ),
            columns="3",
            spacing="4",
            margin_bottom="20px",
            align_items="center",
            justify_content="center",
        ),
    )
