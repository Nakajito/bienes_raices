import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.team.team_box import team_box


def team() -> rx.Component:
    return rx.box(
        rx.heading(
            "Meet Our Expert Real Estate Team",
            color=COLOR_STYLE["background"],
            padding_y="2em",
            text_align="center",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
            as_="h2",
        ),
        rx.vstack(
            rx.heading(
                "Our dedicated team of professionals is here to help you find your dream home and make your real estate goals a reality",
                color=COLOR_STYLE["background"],
                padding_y="1em",
                padding_x=rx.breakpoints(initial="1em", md="2em", lg="3em"),
                text_align="center",
                size=rx.breakpoints(initial="4", md="5", lg="6"),
                font_weight="normal",
                line_height="1.6",
                as_="h3",
            ),
            rx.flex(
                team_box(
                    src="/public/media-webp/avatars/avatar_01-400.webp",
                    alt="Professional portrait of Jane Doe, CEO of Real Estate company",
                    position="CEO",
                    name="Jane Doe",
                ),
                team_box(
                    src="/public/media-webp/avatars/avatar_03-400.webp",
                    alt="Professional portrait of John Smith, Chief Technology Officer",
                    position="CTO",
                    name="John Smith",
                ),
                team_box(
                    src="/public/media-webp/avatars/avatar_02-400.webp",
                    alt="Professional portrait of Emily Johnson, Chief Financial Officer",
                    position="CFO",
                    name="Emily Johnson",
                ),
                team_box(
                    src="/public/media-webp/avatars/avatar_04-400.webp",
                    alt="Professional portrait of Michael Brown, Chief Operating Officer",
                    position="COO",
                    name="Michael Brown",
                ),
                direction="row",
                wrap="wrap",
                justify="center",
                align="stretch",
                gap="2em",
                width="100%",
                padding="2em",
            ),
            rx.text(
                "Our team is committed to providing exceptional service and expertise in the real estate market. "
                "With combined decades of experience, we bring deep market knowledge, professional integrity, "
                "and a client-first approach to every transaction. We stay ahead of market trends and leverage "
                "the latest technology to ensure you receive the best possible service.",
                color=COLOR_STYLE["background"],
                padding_y="2em",
                padding_x=rx.breakpoints(initial="1em", md="2em", lg="3em"),
                text_align="center",
                size=rx.breakpoints(initial="3", md="4", lg="5"),
                line_height="1.6",
            ),
            spacing="5",
            width="100%",
        ),
        background_color=COLOR_STYLE["secondary"],
        min_height="100vh",
        padding="2em",
    )
