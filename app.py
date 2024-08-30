from  KeyGenieAi.adapters.keyboard_listners import KeyboardListener
from KeyGenieAi.application.text_usecase import TextUseCase
import ollama as olm

def get_model_choice():
    models = olm.list()['models']
    model_names = [model['name'] for model in models]
    
    print("Available models:")
    for i, model in enumerate(model_names, start=1):
        print(f"{i}. {model}")
    
    choice = int(input("Select the model number you want to use: ")) - 1
    return model_names[choice]

if __name__ == "__main__":
    model = get_model_choice()
    listener = KeyboardListener(model=model)
    listener.start_listener()
