import reflex as rx
import json
from pathlib import Path
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.layout.footer import footer


class PropertyDetailState(rx.State):
    """State for property details."""

    property_id: str = ""
    property_title: str = "Propiedad"
    property_price: int = 0
    property_beds: int = 0
    property_baths: int = 0
    property_area: int = 0
    property_garage: bool = False
    property_description: str = ""
    property_address: str = ""
    property_year: int = 2020
    property_type: str = ""
    property_status: str = "En Venta"
    property_image: str = "/public/media-webp/property_01-400.webp"

    @rx.var
    def is_rental(self) -> bool:
        """Check if property is for rent."""
        return "Rent" in self.property_status

    @rx.event
    def on_load(self):
        """Load property data when page loads."""
        # Get property ID from router params (using _page to avoid deprecation warning)
        property_id = self.router._page.params.get("id", "1")
        self.load_property_data(property_id)

    def load_property_data(self, property_id: str):
        """Load property data from JSON file based on ID."""
        self.property_id = property_id
        data_path = Path(__file__).parent.parent / "utils" / "data.json"

        try:
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                properties = data.get("properties", [])

                # Find property by ID
                prop = None
                for p in properties:
                    if str(p.get("id")) == str(property_id):
                        prop = p
                        break

                if prop:
                    self.property_title = prop.get("name", "Property")
                    self.property_price = prop.get("price", 0)
                    self.property_beds = prop.get("bedrooms", 0)
                    self.property_baths = prop.get("bathrooms", 0)
                    self.property_area = prop.get("area", 0)
                    self.property_garage = prop.get("garage", False)
                    self.property_address = prop.get("address", "")
                    self.property_year = prop.get("year_built", 2020)
                    self.property_type = prop.get("property_type", "")
                    self.property_status = prop.get("status", "For Sale")

                    # Set image path
                    self.property_image = (
                        f"/media/property_{str(property_id).zfill(2)}.jpg"
                    )

                    # Generate description
                    self.property_description = (
                        f"Excellent {prop.get('property_type', 'property')} located at {prop.get('address', '')}. "
                        f"This property features {prop.get('bedrooms', 0)} bedrooms and {prop.get('bathrooms', 0)} bathrooms, "
                        f"with a total area of {prop.get('area', 0)} m². "
                        f"{'Includes garage. ' if prop.get('garage') else ''}"
                        f"Built in {prop.get('year_built', 2020)}, this property is {prop.get('status', 'available').lower()}. "
                        f"A unique opportunity in the real estate market."
                    )
        except Exception as e:
            print(f"Error loading property data: {e}")


def property_detail_header(title, price, status) -> rx.Component:
    """Header section with property title, price, and status."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    title,
                    size=rx.breakpoints(initial="7", md="8", lg="9"),
                    font_weight="bold",
                    color=COLOR_STYLE["primary_text"],
                    as_="h1",
                ),
                rx.badge(
                    status,
                    color_scheme="green",
                    size="3",
                ),
                spacing="4",
                align="center",
                width="100%",
                justify="between",
                wrap="wrap",
            ),
            rx.cond(
                PropertyDetailState.is_rental,
                rx.text(
                    f"${price:,.0f}/month",
                    size=rx.breakpoints(initial="7", md="8"),
                    font_weight="bold",
                    color=COLOR_STYLE["secondary"],
                ),
                rx.text(
                    f"${price:,.0f}",
                    size=rx.breakpoints(initial="7", md="8"),
                    font_weight="bold",
                    color=COLOR_STYLE["secondary"],
                ),
            ),
            spacing="3",
            width="100%",
        ),
        padding=rx.breakpoints(initial="1.5em", md="2em"),
        background_color="white",
        border_radius="12px",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
        margin_bottom="2em",
    )


def property_detail_image(image_src, alt) -> rx.Component:
    """Main property image."""
    return rx.box(
        rx.image(
            src=image_src,
            alt=alt,
            width="100%",
            height=rx.breakpoints(initial="300px", md="400px", lg="500px"),
            object_fit="cover",
            border_radius="12px",
        ),
        margin_bottom="2em",
    )


def property_feature_item(icon: str, label: str, value: str) -> rx.Component:
    """Individual feature item with icon."""
    return rx.hstack(
        rx.icon(icon, size=28, color=COLOR_STYLE["primary"]),
        rx.vstack(
            rx.text(
                label,
                font_size="14px",
                color=COLOR_STYLE["secondary_text"],
                font_weight="medium",
            ),
            rx.text(
                value,
                font_size="18px",
                color=COLOR_STYLE["primary_text"],
                font_weight="bold",
            ),
            spacing="1",
            align_items="flex-start",
        ),
        spacing="3",
        align="center",
        padding="1em",
        background_color=COLOR_STYLE["accent"],
        border_radius="8px",
        width=rx.breakpoints(
            initial="100%", md="calc(50% - 0.5em)", lg="calc(25% - 0.75em)"
        ),
    )


def property_features_grid() -> rx.Component:
    """Grid of property features."""
    return rx.flex(
        property_feature_item(
            "bed-double", "Bedrooms", f"{PropertyDetailState.property_beds}"
        ),
        property_feature_item(
            "bath", "Bathrooms", f"{PropertyDetailState.property_baths}"
        ),
        property_feature_item(
            "ruler", "Area", f"{PropertyDetailState.property_area} m²"
        ),
        rx.cond(
            PropertyDetailState.property_garage,
            property_feature_item("circle-parking", "Garage", "Yes"),
            property_feature_item("circle-parking", "Garage", "No"),
        ),
        direction="row",
        wrap="wrap",
        justify="between",
        gap="1em",
        width="100%",
        margin_bottom="2em",
    )


def property_description_section() -> rx.Component:
    """Property description section."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "Description",
                size="6",
                font_weight="bold",
                color=COLOR_STYLE["primary_text"],
                margin_bottom="1em",
                as_="h2",
            ),
            rx.text(
                PropertyDetailState.property_description,
                font_size="16px",
                line_height="1.8",
                color=COLOR_STYLE["secondary_text"],
            ),
            spacing="3",
            align_items="flex-start",
        ),
        padding=rx.breakpoints(initial="1.5em", md="2em"),
        background_color="white",
        border_radius="12px",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
        margin_bottom="2em",
    )


def property_details_section() -> rx.Component:
    """Additional property details section."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "Property Details",
                size="6",
                font_weight="bold",
                color=COLOR_STYLE["primary_text"],
                margin_bottom="1em",
                as_="h2",
            ),
            rx.divider(margin_y="0.5em"),
            rx.hstack(
                rx.text(
                    "Address:", font_weight="bold", color=COLOR_STYLE["primary_text"]
                ),
                rx.text(
                    PropertyDetailState.property_address,
                    color=COLOR_STYLE["secondary_text"],
                ),
                justify="between",
                width="100%",
                padding_y="0.5em",
            ),
            rx.divider(margin_y="0.5em"),
            rx.hstack(
                rx.text(
                    "Property Type:",
                    font_weight="bold",
                    color=COLOR_STYLE["primary_text"],
                ),
                rx.text(
                    PropertyDetailState.property_type,
                    color=COLOR_STYLE["secondary_text"],
                ),
                justify="between",
                width="100%",
                padding_y="0.5em",
            ),
            rx.divider(margin_y="0.5em"),
            rx.hstack(
                rx.text(
                    "Year Built:",
                    font_weight="bold",
                    color=COLOR_STYLE["primary_text"],
                ),
                rx.text(
                    PropertyDetailState.property_year,
                    color=COLOR_STYLE["secondary_text"],
                ),
                justify="between",
                width="100%",
                padding_y="0.5em",
            ),
            rx.divider(margin_y="0.5em"),
            rx.hstack(
                rx.text(
                    "Status:", font_weight="bold", color=COLOR_STYLE["primary_text"]
                ),
                rx.badge(
                    PropertyDetailState.property_status,
                    color_scheme="green",
                ),
                justify="between",
                width="100%",
                padding_y="0.5em",
            ),
            spacing="2",
            align_items="flex-start",
        ),
        padding=rx.breakpoints(initial="1.5em", md="2em"),
        background_color="white",
        border_radius="12px",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
        margin_bottom="2em",
    )


def contact_agent_section() -> rx.Component:
    """Contact agent section."""
    return rx.box(
        rx.vstack(
            rx.heading(
                "Interested in this property?",
                size="6",
                font_weight="bold",
                color=COLOR_STYLE["primary_text"],
                margin_bottom="1em",
                as_="h2",
            ),
            rx.text(
                "Contact our agents to schedule a viewing or get more information.",
                font_size="16px",
                color=COLOR_STYLE["secondary_text"],
                margin_bottom="1.5em",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        rx.icon("phone", size=20),
                        "Call Agent",
                        size="3",
                        background_color=COLOR_STYLE["primary"],
                        color="white",
                        _hover={"background_color": COLOR_STYLE["hover"]},
                    ),
                    href="tel:+1234567890",
                ),
                rx.link(
                    rx.button(
                        rx.icon("mail", size=20),
                        "Send Email",
                        size="3",
                        background_color=COLOR_STYLE["secondary"],
                        color="white",
                        _hover={"opacity": "0.9"},
                    ),
                    href="/contact",
                ),
                spacing="4",
                wrap="wrap",
                width="100%",
            ),
            spacing="3",
            align_items="flex-start",
        ),
        padding=rx.breakpoints(initial="1.5em", md="2em"),
        background_color=COLOR_STYLE["accent"],
        border_radius="12px",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
        margin_bottom="2em",
    )


def property_detail() -> rx.Component:
    """Property detail page."""
    return rx.box(
        navbar_icons(),
        rx.container(
            # Back button
            rx.link(
                rx.hstack(
                    rx.icon("arrow-left", size=20),
                    rx.text("Back to Properties", font_weight="medium"),
                    spacing="2",
                    color=COLOR_STYLE["primary"],
                    _hover={"color": COLOR_STYLE["secondary"]},
                ),
                href="/properties",
                margin_bottom="2em",
                display="inline-flex",
            ),
            # Property content
            property_detail_header(
                PropertyDetailState.property_title,
                PropertyDetailState.property_price,
                PropertyDetailState.property_status,
            ),
            property_detail_image(
                PropertyDetailState.property_image,
                PropertyDetailState.property_title,
            ),
            property_features_grid(),
            property_description_section(),
            property_details_section(),
            contact_agent_section(),
            max_width="1200px",
            padding_x=rx.breakpoints(initial="1em", md="2em"),
            padding_y="2em",
        ),
        footer(),
        background_color=COLOR_STYLE["background"],
        min_height="100vh",
    )
