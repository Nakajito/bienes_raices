import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.last_properties.property_card import property_card


def last_properties() -> rx.Component:
    return rx.box(
        rx.heading(
            "Featured Properties - Latest Listings for Sale and Rent",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
            font_weight="bold",
            margin_y="30px",
            color=COLOR_STYLE["primary_text"],
            text_align="center",
            as_="h2",
        ),
        rx.flex(
            # Propiedad 1
            property_card(
                image_src="/public/media-webp/property_01-400.webp",
                image_alt="Beautiful wooden brown and white house with garden - Photo from Pixabay",
                image_title="House for Sale",
                price=250000,
                beds=3,
                baths=2,
                area_sqft=1500,
                has_garage=True,
                property_id="1",
            ),
            # Propiedad 2
            property_card(
                image_src="/public/media-webp/property_02-400.webp",
                image_alt="Luxury villa with swimming pool and modern architecture - Photo from Pixabay",
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
                image_src="/public/media-webp/property_03-400.webp",
                image_alt="Modern two-story home with contemporary design - Photo from Pixabay",
                image_title="Modern Home",
                price=450000,
                beds=4,
                baths=3,
                area_sqft=2500,
                has_garage=True,
                property_id="3",
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
        padding_x=rx.breakpoints(initial="1em", md="2em", lg="3em"),
        margin_x="auto",
    )
