import reflex as rx
def create_button():
    return rx.button("Click me")
app = rx.App()
app.add_page(create_button)
