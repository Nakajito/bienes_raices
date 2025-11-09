import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def contact_input(label: str, type: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            label,
            font_weight="medium",
            color=COLOR_STYLE["primary_text"],
            font_size=["13px", "13px", "14px"],  # Tamaño responsive
            margin_bottom="6px",
        ),
        rx.input(
            type=type,
            name=f"{label}_input",
            required=True,
            # Estilo Material Design (igual al text_area)
            border="1px solid #d1d5db",
            border_radius="4px",
            background_color=COLOR_STYLE["background"],
            width="100%",
            font_size=["15px", "15px", "16px"],  # Tamaño responsive
            height=["44px", "46px", "48px"],  # Altura responsive
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
