import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.components.last_properties.property_card import property_card
from bienes_raices.layout.footer import footer


def properties() -> rx.Component:
    return rx.box(
        navbar_icons(),
        rx.heading(
            "Explore All Available Properties for Sale and Rent",
            font_weight="bold",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
            margin_y="30px",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
            as_="h1",
        ),
        rx.flex(
            # Aquí puedes agregar múltiples property_card() para mostrar las propiedades
            property_card(
                image_src="/media/property_01.jpg",
                image_alt="Foto de Pixabay: https://www.pexels.com/es-es/foto/casa-de-madera-marron-y-blanca-164558/",
                image_title="House for Sale",
                price=250000,
                beds=3,
                baths=2,
                area_sqft=1500,
                has_garage=True,
                property_id="1",
            ),
            property_card(
                image_src="/media/property_02.jpg",
                image_alt="Foto de Pixabay: https://www.pexels.com/es-es/foto/casa-de-lujo-con-piscina-1645581/",
                image_title="Luxury Villa",
                price=750000,
                beds=5,
                baths=4,
                area_sqft=3500,
                has_garage=True,
                property_id="2",
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
                property_id="3",
            ),
            # Propiedad 4
            property_card(
                image_src="/media/property_04.jpg",
                image_alt="Foto de Pixabay: Foto de Scott Webb: https://www.pexels.com/es-es/foto/casa-de-madera-blanca-y-roja-con-valla-1029599/",
                image_title="Cozy Cottage",
                price=300000,
                beds=2,
                baths=1,
                area_sqft=1200,
                has_garage=False,
                property_id="4",
            ),
            # propiedad 5
            property_card(
                image_src="/media/property_05.jpg",
                image_alt="Foto de Pixabay: Foto de apertur2.8: https://www.pexels.com/es-es/foto/casas-bosque-casa-otono-14461716/",
                image_title="Cozy Cottage",
                price=600000,
                beds=3,
                baths=2,
                area_sqft=2000,
                has_garage=True,
                property_id="5",
            ),
            # Propiedad 6
            property_card(
                image_src="/media/property_06.jpg",
                image_alt="Foto de Pixabay: Foto de David Bartus: Foto de Frans van Heerden: https://www.pexels.com/es-es/foto/casas-blancas-de-un-piso-al-lado-del-cuerpo-de-agua-1438832/",
                image_title="Modern House",
                price=1500000,
                beds=4,
                baths=5,
                area_sqft=3100,
                has_garage=True,
                property_id="6",
            ),
            # Propiedades del flex
            direction="row",
            wrap="wrap",
            justify="center",
            align="stretch",
            gap="2em",
            width="100%",
            padding="2em",
        ),
        footer(),
        background_color=COLOR_STYLE["background"],
        margin_x="auto",
        padding_x=rx.breakpoints(initial="0.5em", md="1em"),
    )
