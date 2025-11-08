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
            size="8",
        ),
        rx.flex(
            rx.heading(
                "Meet our dedicated team of professionals who are here to help you find your dream home.",
                color=COLOR_STYLE["background"],
                padding_y="1em",
                text_align="center",
                size="8",
            ),
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
        ),
        rx.text(
            "Our team is committed to providing exceptional service and expertise in the real estate market.",
            color=COLOR_STYLE["background"],
            padding_y="2em",
            text_align="center",
            size="5",
        ),
        background_color=COLOR_STYLE["secondary"],
        min_height="100vh",
    )
