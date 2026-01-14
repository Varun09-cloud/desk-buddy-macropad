# Desktop Buddy Macropad
# Hardware: Seeed XIAO RP2040
# 3 keys + 1 rotary encoder

# Import board IOs
import board

# KMK imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

# ==============================================================================
# CONFIGURATION
# ==============================================================================

# Key pins
KEY_PINS = [
    board.D0,  # Key 1
    board.D1,  # Key 2
    board.D2,  # Key 3
]

# Rotary encoder pins
ENCODER_PIN_A = board.D3
ENCODER_PIN_B = board.D4
ENCODER_BUTTON = board.D5

# ==============================================================================
# KEYBOARD SETUP
# ==============================================================================

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

encoder = EncoderHandler()
keyboard.modules.append(encoder)

keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
)

# ==============================================================================
# ENCODER CONFIGURATION
# ==============================================================================

encoder.pins = (
    (ENCODER_PIN_A, ENCODER_PIN_B, ENCODER_BUTTON, False),
)

encoder.map = [
    ((KC.VOLU,), (KC.VOLD,), KC.MUTE),
]

# ==============================================================================
# MACROS
# ==============================================================================

def open_run_dialog():
    return KC.LGUI(KC.R)

def launch_app(app_name, delay=250):
    return KC.MACRO(
        open_run_dialog(),
        KC.MACRO_SLEEP_MS(delay),
        app_name,
        KC.ENTER,
    )

# Application shortcuts
SPOTIFY = launch_app("spotify")
VSCODE = launch_app("code")  
CHROME = launch_app("chrome")

# Keyboard shortcuts
SCREENSHOT = KC.LGUI(KC.LSFT(KC.S))
TASK_MANAGER = KC.LCTL(KC.LSFT(KC.ESC))
EMOJI_PICKER = KC.LGUI(KC.DOT)

# Media controls
PLAY_PAUSE = KC.MEDIA_PLAY_PAUSE
NEXT_TRACK = KC.MEDIA_NEXT_TRACK
PREV_TRACK = KC.MEDIA_PREV_TRACK

# Productivity
VIRTUAL_DESKTOP_LEFT = KC.LCTL(KC.LGUI(KC.LEFT))
VIRTUAL_DESKTOP_RIGHT = KC.LCTL(KC.LGUI(KC.RIGHT))
LOCK_SCREEN = KC.LGUI(KC.L)

# Text macros
HELLO_WORLD = KC.MACRO("Hello, World!")
EMAIL_SIGNATURE = KC.MACRO("Best regards,\nYour Name\nyour.email@example.com")
CURRENT_DATE = KC.MACRO("2026-01-13")

# ==============================================================================
# KEYMAP
# ==============================================================================

# Option 1: Application Launchers (Default)
keyboard.keymap = [
    [SPOTIFY, VSCODE, CHROME]
]

# Option 2: Media Controls
# keyboard.keymap = [
#     [PREV_TRACK, PLAY_PAUSE, NEXT_TRACK]
# ]

# Option 3: Productivity Tools
# keyboard.keymap = [
#     [SCREENSHOT, TASK_MANAGER, EMOJI_PICKER]
# ]

# Option 4: Desktop Navigation
# keyboard.keymap = [
#     [VIRTUAL_DESKTOP_LEFT, LOCK_SCREEN, VIRTUAL_DESKTOP_RIGHT]
# ]

# Option 5: Text Macros
# keyboard.keymap = [
#     [HELLO_WORLD, EMAIL_SIGNATURE, CURRENT_DATE]
# ]

# ==============================================================================
# START KEYBOARD
# ==============================================================================

if __name__ == '__main__':
    keyboard.go()