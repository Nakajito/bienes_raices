import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def testimonial_text(testimonial: str, rate: int, author: str) -> rx.Component:
    return (
        rx.vstack(
            rx.text(
                testimonial,
                color=COLOR_STYLE["primary_text"],
                font_size="16px",
                text_align="center",
                line_height="1.6",
            ),
            rx.text(
                f"{'⭐' * rate}",
                font_size="20px",
            ),
            rx.text(
                author,
                color=COLOR_STYLE["secondary_text"],
                font_size="15px",
                font_weight="medium",
            ),
            spacing="3",
            align_items="center",
        ),
    )
