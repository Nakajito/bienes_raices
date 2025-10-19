import reflex as rx

config = rx.Config(
    app_name="bienes_raices",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)