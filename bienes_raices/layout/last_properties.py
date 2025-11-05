import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.last_properties.property_card import property_card


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
            property_card(
                image_src="/media/property_01.jpg",
                image_alt="Foto de Pixabay: https://www.pexels.com/es-es/foto/casa-de-madera-marron-y-blanca-164558/",
                image_title="House for Sale",
                price=250000,
                beds=3,
                baths=2,
                area_sqft=1500,
                has_garage=True,
            ),
            # Propiedad 2
            property_card(
                image_src="/media/property_02.jpg",
                image_alt="Foto de Pixabay: https://www.pexels.com/es-es/foto/casa-de-lujo-con-piscina-1645581/",
                image_title="Luxury Villa",
                price=750000,
                beds=5,
                baths=4,
                area_sqft=3500,
                has_garage=True,
            ),
            # Propiedad 3
            property_card(
                image_src="/media/property_03.jpg",
                image_alt="Foto de Pixabay: https://www.pexels.com/es-es/foto/casa-moderna-de-dos-pisos-1645582/",
                image_title="Modern Home",
                price=450000,
                beds=4,
                baths=3,
                area_sqft=2500,
                has_garage=True,
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
