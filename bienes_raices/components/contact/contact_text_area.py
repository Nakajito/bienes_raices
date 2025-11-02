import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def contact_text_area(label: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            label,
            font_weight="medium",
            color=COLOR_STYLE["primary_text"],
            font_size="14px",
            margin_bottom="6px",
        ),
        rx.text_area(
            # Estilo Material Design
            border="1px solid #d1d5db",
            border_radius="4px",
            background_color=COLOR_STYLE["background"],
            # padding="12px 16px",
            width="100%",
            height="120px",
            font_size="16px",
            color=COLOR_STYLE["primary"],
            # Focus state
            _focus={
                "border_color": COLOR_STYLE["primary"],
                "border_width": "2px",
                "outline": "none",
            },
        ),
        width="100%",
        spacing="1",
    )
