from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label, Input, Button


class MyApp(App):

    def compose(self) -> ComposeResult:
        yield Header()

        yield Label("Simple Python UI in Termux")
        yield Input(placeholder="Enter your name", id="name")
        yield Button("Submit", id="submit")
        yield Label("", id="result")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        name_input = self.query_one("#name", Input)
        result_label = self.query_one("#result", Label)

        name = name_input.value

        if name:
            result_label.update(f"Welcome, {name}!")
        else:
            result_label.update("Please enter your name.")


MyApp().run()