import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.layout.footer import footer


class PropertyDetailState(rx.State):
    """State for property details."""

    property_id: str = ""
    property_title: str = "Luxury Modern Home"
    property_price: int = 450000
    property_beds: int = 4
    property_baths: int = 3
    property_area: int = 2500
    property_garage: bool = True
    property_description: str = (
        "Beautiful modern home in a quiet neighborhood. Features spacious rooms, modern kitchen, and large backyard perfect for entertaining."
    )
    property_address: str = "123 Main Street, City, State 12345"
    property_year: int = 2020
    property_type: str = "Single Family Home"
    property_status: str = "For Sale"


def property_detail_header(title: str, price: int, status: str) -> rx.Component:
    """Header section with property title, price, and status."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    title,
                    size=rx.breakpoints(initial="7", md="8", lg="9"),
                    font_weight="bold",
                    color=COLOR_STYLE["primary_text"],
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
            rx.text(
                f"${price:,.2f}",
                size=rx.breakpoints(initial="7", md="8"),
                font_weight="bold",
                color=COLOR_STYLE["secondary"],
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


def property_detail_image(image_src: str, alt: str) -> rx.Component:
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
            "ruler", "Area", f"{PropertyDetailState.property_area} sqft"
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
                    "Year Built:", font_weight="bold", color=COLOR_STYLE["primary_text"]
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
                "/public/media-webp/property_03-400.webp",
                "Modern Home",
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
