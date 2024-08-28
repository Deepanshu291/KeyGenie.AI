from string import Template
import ollama as olm

class TextProcessor:
    def __init__(self, model='phi3'):
        self.model = model

    def generate(self, prompt):
        res = olm.generate(model=self.model, prompt=prompt)
        return res["response"]

    def fix_text(self, text, paraphrase=False):
        if paraphrase:
            prompt_template = Template(
                """Paraphrase the following text, correcting any typos, casing, punctuation, and grammar errors, while retaining all original line breaks:
                $text
                Provide only the revised text without any additional preamble."""
            )
        else:
            prompt_template = Template(
                """Fix all typos, casing, punctuation, and grammar in this text, but preserve all new line characters:
                $text
                Return only the corrected text, don't include a preamble."""
            )
        
        prompt = prompt_template.substitute(text=text)
        fix = olm.generate(model=self.model, prompt=prompt)
        return fix['response']
