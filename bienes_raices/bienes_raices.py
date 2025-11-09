import reflex as rx
import json
from pathlib import Path
from bienes_raices.pages.properties import properties
from bienes_raices.pages.contact import contact
from bienes_raices.pages.about import about_page
from bienes_raices.pages.property_detail import property_detail, PropertyDetailState
from bienes_raices.layout.navbar import navbar_icons
from bienes_raices.layout.heading import heading
from bienes_raices.layout.about import about
from bienes_raices.layout.footer import footer
from bienes_raices.layout.last_properties import last_properties
from bienes_raices.layout.testimonials import testimonials
from bienes_raices.layout.contact import contact_section
from bienes_raices.pages.not_found import not_found
from bienes_raices.styles.styles import COLOR_STYLE

from rxconfig import config


class State(rx.State):
    """The app state."""

    properties_data: list[dict] = []

    def load_properties(self):
        """Load properties from JSON file."""
        data_path = Path(__file__).parent / "utils" / "data.json"
        try:
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.properties_data = data.get("properties", [])
        except Exception as e:
            print(f"Error loading properties: {e}")
            self.properties_data = []

    def on_load(self):
        """Called when page loads."""
        self.load_properties()


def index() -> rx.Component:
    """The main page of the app."""
    return rx.box(
        navbar_icons(),
        heading(),
        about(),
        last_properties(),
        testimonials(),
        contact_section(),
        footer(),
        bg=COLOR_STYLE["background"],
    )


app = rx.App()
app.add_page(
    index,
    title="Real Estate - Buy, Sell & Rent Properties",
    description="Discover the best properties for sale and rent. Expert guidance with 500+ properties, 15 awards, and 200+ satisfied clients.",
    image="/logo_2.png",
    meta=[
        {
            "name": "keywords",
            "content": "real estate, properties for sale, homes for rent, buy house, sell property, real estate agent, dream home, luxury homes",
        },
        {"name": "author", "content": "Real Estate"},
        {"property": "og:type", "content": "website"},
        {
            "property": "og:title",
            "content": "Real Estate - Buy, Sell & Rent Properties",
        },
        {
            "property": "og:description",
            "content": "Discover the best properties for sale and rent. Expert guidance with 500+ properties and 200+ satisfied clients.",
        },
        {"property": "og:image", "content": "/logo_2.png"},
    ],
)
app.add_page(
    properties,
    route="/properties",
    title="Properties for Sale & Rent | Real Estate",
    description="Browse luxury villas, modern homes, and cozy cottages. Find your perfect property with detailed info on beds, baths, and pricing.",
    image="/logo_2.png",
    meta=[
        {
            "name": "keywords",
            "content": "properties for sale, homes for rent, luxury villas, modern homes, real estate listings, houses for sale",
        },
        {"property": "og:type", "content": "website"},
        {
            "property": "og:title",
            "content": "Properties for Sale & Rent | Real Estate",
        },
    ],
)
app.add_page(
    property_detail,
    route="/property/[id]",
    title="Property Details | Real Estate",
    description="View property details: price, bedrooms, bathrooms, square footage, and amenities. Contact us to schedule a viewing today.",
    on_load=PropertyDetailState.on_load,
)
app.add_page(
    contact,
    route="/contact",
    title="Contact Real Estate Agents | Get Expert Help",
    description="Contact our expert agents today. We help with buying, selling, and renting properties. Get personalized service now.",
    image="/logo_2.png",
    meta=[
        {
            "name": "keywords",
            "content": "contact real estate agent, property consultation, real estate services, schedule viewing",
        },
    ],
)
app.add_page(
    about_page,
    route="/about_page",
    title="About Us | Real Estate - Trusted Partner",
    description="Meet our professional team. 15 awards, 500+ properties, 300+ homes sold, 200+ satisfied clients. Your trusted real estate partner.",
    image="/logo_2.png",
    meta=[
        {
            "name": "keywords",
            "content": "about real estate company, experienced agents, trusted property partner, real estate team",
        },
    ],
)
app.add_page(
    not_found,
    route="/404",
)
