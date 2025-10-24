import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def testimonial_text(testimonial: str, rate: int, author: str) -> rx.Component:
    return (
        rx.vstack(
            rx.text(testimonial, color=COLOR_STYLE["primary_text"]),
            rx.text(f"{'⭐' * rate}"),
            rx.text(author, color=COLOR_STYLE["secondary_text"]),
        ),
    )
