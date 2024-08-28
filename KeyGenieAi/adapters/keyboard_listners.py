from pynput.keyboard import Listener, Key
from KeyGenieAi.application.text_usecase import TextUseCase

class KeyboardListener:
    def __init__(self):
        self.text_use_case = TextUseCase()

    def on_press(self, key):
        try:
            if key.char == "$":
                self.text_use_case.replace_flag = key.char
                print("its working")
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            if key == Key.esc:
                return False
            if key == Key.f7:
                text = self.text_use_case.copy_text()
                self.text_use_case.process_text()
                fixed_text = self.text_use_case.processor.fix_text(text)
                self.text_use_case.select_text()
                self.text_use_case.keyboard.type(fixed_text)

            if key == Key.f8:
                text = self.text_use_case.copy_text()
                self.text_use_case.process_text()
                fixed_text = self.text_use_case.processor.fix_text(text,paraphrase=True)
                self.text_use_case.select_text()
                self.text_use_case.keyboard.type(fixed_text)

            if key.char in ['.', '?', "!"] and self.text_use_case.replace_flag:
                text = self.text_use_case.copy_text()
                prompt = self.text_use_case.extract_command(text)
                if prompt and any(cmd in text for cmd in ['$gen', '$ai']):
                    self.text_use_case.process_text()
                    generated_text = self.text_use_case.processor.generate(prompt)
                    self.text_use_case.select_text()
                    self.text_use_case.keyboard.type(generated_text)
                elif prompt and '$fix' in text:
                    self.text_use_case.process_text()
                    generated_text = self.text_use_case.processor.fix_text(prompt)
                    self.text_use_case.select_text()
                    self.text_use_case.keyboard.type(generated_text)
                if prompt and '$para' in text:
                    self.text_use_case.process_text()
                    generated_text = self.text_use_case.processor.fix_text(text=prompt, paraphrase=True)
                    self.text_use_case.select_text()
                    self.text_use_case.keyboard.type(generated_text)
                self.text_use_case.replace_flag = None
        except AttributeError:
            pass

    def start_listener(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
