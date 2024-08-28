import time
from pynput.keyboard import Key, Listener, Controller
import pyperclip
import ollama as olm
from string import Template
# Initialize the keyboard controller
keyboard = Controller()

# Flag to track whether "$gen" or "$ai" was detected
replace_flag = None
aicmd = ["$gen","$ai","$phi3","$fix"]

def genrate(prompt):
    res = olm.generate(model='phi3',prompt=prompt)
    return res["response"]

def Fixtext(text, paraphase=False):
    PROMPT_TEMPLATE=""
    if paraphase is True:
        PROMPT_TEMPLATE = Template(
    """Paraphrase the following text, correcting any typos, casing, punctuation, and grammar errors, while retaining all original line breaks:

    $text

    Provide only the revised text without any additional preamble.
    """
      )
    else:
        PROMPT_TEMPLATE = Template(
        """Fix all typos and casing and punctuation and grammer in this text, but preserve all new line characters:

        $text

        Return only the corrected text, don't include a preamble.
        """
     )
    prompt = PROMPT_TEMPLATE.substitute(text=text)

    fix = olm.generate(model="phi3",prompt=prompt)
    # print(fix)
    return fix['response']
    

def selectText():
    keyboard.tap(Key.home)
    with keyboard.pressed(Key.shift):
        keyboard.tap(Key.end)
        # keyboard.tap(Key.backspace)

def CopyText():
    selectText()

    with keyboard.pressed(Key.ctrl):
         keyboard.tap('c')
    time.sleep(0.1)
    text = pyperclip.paste()
    print(text)
    selectText()
    return text
    # keyboard.tap(Key.backspace)
    # keyboard.release(Key.end)
    # keyboard.release(Key.shift)

def processingText():
    selectText()
    time.sleep(0.1)
    keyboard.type("generating....")
    selectText()

def extractText(st):
# Initialize variables
    start_index = None
    end_index = None

# Find the first occurrence of any command in the string
    for cmd in aicmd:
        if cmd in st:
            start_index = st.find(cmd)
            break

# Find the index of the first period (".") after the command
    if start_index is not None:
        for end in ['.','?','!']:
            if end in st:
                end_index = st.find(end, start_index)

# Extract the desired substring
    if start_index is not None and end_index != -1:
        extracted_line = st[start_index + len(cmd):end_index].strip()
        print(extracted_line)
        return extracted_line
    else:
        print("No relevant line found.")



def on_press(key):
    global replace_flag

    try:
        # Check if "$gen" or "$ai" was pressed
        if key.char == "$":
            print("Yes its working")
            replace_flag = key.char
        
        

        # if key == Key.esc:
        #     exit()

    except AttributeError:
        pass

def on_release(key):
    global replace_flag

    try:
        if key == Key.esc:
            return False
        # Check if F9 key was pressed and "$gen" or "$ai" was detected
        if key == Key.f7:
            text = CopyText()
            processingText()
            fix = Fixtext(text)
            print("Yes its press f7")
            print(fix)
            selectText()
            keyboard.type(fix)
            
        
        if key == Key.f8:
            with keyboard.pressed(Key.ctrl):
                keyboard.tap('a')
            with keyboard.pressed(Key.ctrl):
                keyboard.tap('c')
            time.sleep(0.1)
            text = pyperclip.paste()
            processingText()
            fix = Fixtext(text,paraphase=True)
            selectText()
            print(fix)
            keyboard.type(fix)
            # keyboard.type("its replaced whole paragraph.")

        if key.char in ['.','?',"!"] and replace_flag:
            print("its f9")
            # Delete the existing line (move cursor to the beginning of the line)
            text = CopyText()
            for cmd in aicmd:
                if cmd in text:
                    prompt = extractText(text)
                    print('yes there is $gen ')
                # res = genrate(prompt)
                # print(res)
                    processingText()
                    res = genrate(prompt=prompt)
                    print(res)
                    selectText()
                    keyboard.type(res)
                # pyperclip.copy(res)
                # time.sleep(0.1)

                # with keyboard.pressed(Key.ctrl):
                #     keyboard.tap('v')

            # Reset the flag
            replace_flag = None

        
    except AttributeError:
        pass

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
