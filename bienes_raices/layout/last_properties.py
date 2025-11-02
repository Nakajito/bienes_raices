import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.last_properties.property_image import property_image
from bienes_raices.components.last_properties.property_icon import property_icon


def last_properties() -> rx.Component:
    return rx.box(
        rx.heading(
            "Latest Properties",
            size="8",
            font_weight="bold",
            margin_y="30px",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
        ),
        rx.flex(
            # Propiedad 1
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
                    spacing="3",
                    justify="center",
                    width="100%",
                    padding="1em",
                ),
                # Estilos similares a testimonials
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
                transition="transform 0.2s ease, box-shadow 0.2s ease",
                _hover={
                    "transform": "translateY(-5px)",
                    "box_shadow": "0 8px 15px rgba(0, 0, 0, 0.15)",
                },
            ),
            # Propiedad 2
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
                transition="transform 0.2s ease, box-shadow 0.2s ease",
                _hover={
                    "transform": "translateY(-5px)",
                    "box_shadow": "0 8px 15px rgba(0, 0, 0, 0.15)",
                },
            ),
            # Propiedad 3
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
                transition="transform 0.2s ease, box-shadow 0.2s ease",
                _hover={
                    "transform": "translateY(-5px)",
                    "box_shadow": "0 8px 15px rgba(0, 0, 0, 0.15)",
                },
            ),
            # Propiedades del flex
            direction="row",
            wrap="wrap",
            justify="center",
            align="stretch",
            gap="2em",
            width="100%",
        ),
        # Estilos del contenedor principal (igual a testimonials)
        background_color=COLOR_STYLE["background"],
        padding="3em",
        margin_x="auto",
        # max_width="1200px",
    )
