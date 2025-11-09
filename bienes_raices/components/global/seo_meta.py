import reflex as rx


def seo_meta() -> rx.Component:
    """Component that adds common SEO meta tags to all pages."""
    return rx.fragment(
        rx.el.link(rel="icon", type_="image/x-icon", href="/favicon.ico"),
        rx.el.link(rel="apple-touch-icon", href="/logo_2.png"),
        rx.el.link(rel="icon", type_="image/png", sizes="192x192", href="/logo_2.png"),
        rx.el.meta(name="viewport", content="width=device-width, initial-scale=1"),
        rx.el.meta(charset="UTF-8"),
    )
