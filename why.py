from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class CalculatorApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        self.solution = TextInput(font_size=32, multiline=False, readonly=True)
        root.add_widget(self.solution)
        buttons = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', ''],
            ['1', '2', '3', '-', ''],
            ['0', '.', '=', '+', ''],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                if label == '':
                    h_layout.add_widget(Button())
                else:
                    button = Button(text=label, font_size=24)
                    if label == 'C':
                        button.bind(on_press=self.clear)
                    else:
                        button.bind(on_press=self.add_operation)
                    h_layout.add_widget(button)

            root.add_widget(h_layout)
        return root
    def add_operation(self, instance):
        operation = instance.text
        if operation == '=':
            try:
                self.solution.text = str(eval(self.solution.text))
            except Exception:
                self.solution.text = 'Error'
        else:
            self.solution.text += operation
    def clear(self, instance):
        self.solution.text = ''
if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
