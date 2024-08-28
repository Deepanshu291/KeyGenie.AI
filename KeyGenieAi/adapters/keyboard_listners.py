from pynput.keyboard import Listener, Key
from application.text_usecase import TextUseCase

class KeyboardListener:
    def __init__(self):
        self.text_use_case = TextUseCase()

    def on_press(self, key):
        try:
            if key.char == "$":
                self.text_use_case.replace_flag = key.char
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key == Key.esc:
                return False
            if key == Key.f7:
                text = self.text_use_case.copy_text()
                fixed_text = self.text_use_case.process_text(text)
                self.text_use_case.select_text()
                self.text_use_case.keyboard.type(fixed_text)

            if key == Key.f8:
                text = self.text_use_case.copy_text()
                fixed_text = self.text_use_case.process_text(text, paraphrase=True)
                self.text_use_case.select_text()
                self.text_use_case.keyboard.type(fixed_text)

            if key.char in ['.', '?', "!"] and self.text_use_case.replace_flag:
                text = self.text_use_case.copy_text()
                prompt = self.text_use_case.extract_command(text)
                if prompt:
                    generated_text = self.text_use_case.processor.generate(prompt)
                    self.text_use_case.select_text()
                    self.text_use_case.keyboard.type(generated_text)
                self.text_use_case.replace_flag = None
        except AttributeError:
            pass

    def start_listener(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
