from pynput import keyboard
from pynput.keyboard import Key,HotKey,Controller,GlobalHotKeys
import pyperclip
import time


controller = Controller()

def on_activate():
    print('Global hotkey activated!')

# def for_canonical(f):
#     rthis is workingthis is working

def fix_text(text):
    pass

def fix_current_line():
    # macOS short cut to select current line: Cmd+Shift+Left
    controller.press(Key.ctrl)
    controller.tap('a')

    # controller.press(Key.ctrl)
    # controller.press(Key.shift)
    # controller.press(Key.left)

    # controller.release(Key.ctrl)
    # controller.release(Key.shift)
    # controller.release(Key.left)


    select_text()

def select_text():
    with controller.pressed(Key.ctrl_r):
        controller.tap('c')
        
    time.sleep(0.1)
    text = pyperclip.paste()
    print(text)
    # fixtext = fix_text(text)
    # fixtext = "this is working"
    # pyperclip.copy(fixtext)
    # time.sleep(0.1)

    # with controller.pressed(Key.ctrl):
    #     controller.tap('v')

def on_f9():
    print("f9 pressed")
    select_text()

def on_f10():
    exit()

def on_f7():
    fix_current_line()


print(Key.f7.value)
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    on_activate)

with GlobalHotKeys(
    {'<120>': on_f9, '<121>': on_f10, '<118>': on_f7}
    ) as g:
  g.join()

# with keyboard.Listener() as l:
#     l.join()