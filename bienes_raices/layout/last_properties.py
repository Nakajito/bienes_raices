import reflex as rx
import json
from pathlib import Path
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.last_properties.property_card import property_card


def load_properties_data():
    """Load properties from JSON file."""
    data_path = Path(__file__).parent.parent / "utils" / "data.json"
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("properties", [])
    except Exception as e:
        print(f"Error loading properties: {e}")
        return []


def last_properties() -> rx.Component:
    properties_data = load_properties_data()

    # Mostrar solo las primeras 3 propiedades
    featured_properties = properties_data[:3]

    # Crear las tarjetas de propiedades dinámicamente
    property_cards = []
    for prop in featured_properties:
        # Usar el ID del JSON
        prop_id = str(prop.get("id", 1))
        image_num = prop_id.zfill(2)
        image_src = f"/public/media-webp/property_{image_num}-400.webp"

        # Crear descripción del alt basada en el tipo de propiedad
        alt_text = f"{prop['property_type']} - {prop['name']} at {prop['address'].split(',')[0]}"

        property_cards.append(
            property_card(
                image_src=image_src,
                image_alt=alt_text,
                image_title=prop["name"],
                price=prop["price"],
                beds=prop["bedrooms"],
                baths=prop["bathrooms"],
                area_sqft=prop["area"],
                has_garage=prop["garage"],
                property_id=prop_id,
            )
        )

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
            *property_cards,
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
