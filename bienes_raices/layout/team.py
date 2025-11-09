import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE
from bienes_raices.components.team.team_box import team_box


def team() -> rx.Component:
    return rx.box(
        rx.heading(
            "Our Team",
            color=COLOR_STYLE["background"],
            padding_y="2em",
            text_align="center",
            size=rx.breakpoints(initial="6", md="7", lg="8"),
        ),
        rx.vstack(
            rx.heading(
                "Meet our dedicated team of professionals who are here to help you find your dream home.",
                color=COLOR_STYLE["background"],
                padding_y="1em",
                padding_x=rx.breakpoints(initial="1em", md="2em", lg="3em"),
                text_align="center",
                size=rx.breakpoints(initial="4", md="5", lg="6"),
                font_weight="normal",
                line_height="1.6",
            ),
            rx.flex(
                team_box(
                    src="/public/media-webp/avatars/avatar_01-400.webp",
                    alt="Jane Doe",
                    position="CEO",
                    name="Jane Doe",
                ),
                team_box(
                    src="/public/media-webp/avatars/avatar_03-400.webp",
                    alt="John Smith",
                    position="CTO",
                    name="John Smith",
                ),
                team_box(
                    src="/public/media-webp/avatars/avatar_02-400.webp",
                    alt="Emily Johnson",
                    position="CFO",
                    name="Emily Johnson",
                ),
                team_box(
                    src="/public/media-webp/avatars/avatar_04-400.webp",
                    alt="Michael Brown",
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
                "Our team is committed to providing exceptional service and expertise in the real estate market.",
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
