import reflex as rx
from bienes_raices.pages.properties import properties
from bienes_raices.pages.contact import contact
from bienes_raices.pages.about import about_page
from bienes_raices.pages.property_detail import property_detail
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
    title="Real Estate - Find Your Dream Home | Buy, Sell & Rent Properties",
    description="Discover the best real estate properties for sale and rent. We offer expert guidance in buying, selling, and renting homes with over 500 properties, 15 awards, and 200+ satisfied clients.",
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
            "content": "Real Estate - Find Your Dream Home | Buy, Sell & Rent Properties",
        },
        {
            "property": "og:description",
            "content": "Discover the best real estate properties for sale and rent. Expert guidance with over 500 properties and 200+ satisfied clients.",
        },
        {"property": "og:image", "content": "/logo_2.png"},
    ],
)
app.add_page(
    properties,
    route="/properties",
    title="Properties for Sale and Rent | Real Estate Listings & Homes",
    description="Browse our extensive collection of properties including luxury villas, modern homes, cozy cottages, and family houses. Find your perfect property with detailed information on bedrooms, bathrooms, and pricing.",
    image="/logo_2.png",
    meta=[
        {
            "name": "keywords",
            "content": "properties for sale, homes for rent, luxury villas, modern homes, real estate listings, houses for sale",
        },
        {"property": "og:type", "content": "website"},
        {
            "property": "og:title",
            "content": "Properties for Sale and Rent | Real Estate Listings",
        },
    ],
)
app.add_page(
    property_detail,
    route="/property/[id]",
    title="Property Details | Real Estate - View Property Information",
    description="View detailed information about this property including price, bedrooms, bathrooms, square footage, and amenities. Contact us to schedule a viewing.",
)
app.add_page(
    contact,
    route="/contact",
    title="Contact Us | Real Estate - Get in Touch with Our Expert Agents",
    description="Ready to find your dream home? Contact our expert real estate agents today. We're here to help you with buying, selling, or renting properties. Get personalized service and expert guidance.",
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
    title="About Us | Real Estate - Your Trusted Property Partner Since Years",
    description="Learn about our experienced team of real estate professionals. With 15 awards, 500+ properties, 300+ homes sold, and 200+ satisfied clients, we're committed to helping you find your perfect property.",
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
