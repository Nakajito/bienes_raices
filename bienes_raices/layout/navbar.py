import reflex as rx
from bienes_raices.styles.styles import COLOR_STYLE


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
        color=COLOR_STYLE["background"],
        text_decoration="none",
        _hover={"color": COLOR_STYLE["secondary"]},
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
        ),
        href=url,
    )


def navbar_icons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo_2.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Real Estate",
                        size="7",
                        weight="bold",
                        color=COLOR_STYLE["background"],
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_icons_item("Home", "home", "/#"),
                    navbar_icons_item("Properties", "building", "/#"),
                    navbar_icons_item("Contact", "mail", "/#"),
                    spacing="6",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo_2.svg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Real Estate", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        navbar_icons_menu_item("Home", "home", "/#"),
                        navbar_icons_menu_item("Properties", "building", "/#"),
                        navbar_icons_menu_item("Contact", "mail", "/#"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        background_color=COLOR_STYLE["primary"],
    )
