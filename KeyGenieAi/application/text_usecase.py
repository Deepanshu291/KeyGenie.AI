import time
from pynput.keyboard import Controller, Key
import pyperclip
from KeyGenieAi.services.text_processor import OllamaProcessor

class TextUseCase:
    model =""
    def __init__(self,model):
        self.model = model
        self.keyboard = Controller()
        self.llm = OllamaProcessor(model=model)
        self.replace_flag = None
        self.aicmd = ["$gen", "$ai", "$phi3", "$fix","$para"]

    def copy_text(self):
        self.select_text()
        with self.keyboard.pressed(Key.ctrl):
            self.keyboard.tap('c')
        time.sleep(0.1)
        text = pyperclip.paste()
        self.select_text()
        return text

    def select_text(self):
        self.keyboard.tap(Key.home)
        with self.keyboard.pressed(Key.shift):
            self.keyboard.tap(Key.end)

    def process_text(self):
        self.select_text()
        time.sleep(0.1)
        model_name = str(self.llm.model).split(':')[0]
        self.keyboard.type(f"{model_name} is generating....")
        self.select_text()
        # fixed_text = self.processor.fix_text(text, paraphrase)
        # return fixed_text

    def extract_command(self, text):
        start_index = end_index = None
        for cmd in self.aicmd:
            if cmd in text:
                start_index = text.find(cmd)
                break
        if start_index is not None:
            for end in ['.', '?', '!']:
                if end in text:
                    end_index = text.find(end, start_index)
        if start_index is not None and end_index != -1:
            return text[start_index + len(cmd):end_index].strip()
        return None
