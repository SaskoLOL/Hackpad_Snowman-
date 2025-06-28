import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

led_pins = [board.D10, board.D11, board.D12, board.D13]
leds = []

for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
    leds.append(led)

def toggle_led(index):
    leds[index].value = not leds[index].value

def reset_leds():
    for led in leds:
        led.value = False

keyboard.keymap = [
    [
        KC.MACRO(
            Tap(KC.LCTL(KC.C)),
            Tap(KC.LCTL(KC.A)),
            Tap(KC.DEL),
            Tap(KC.C),
            Tap(KC.L),
            Tap(KC.S),
            Tap(KC.ENTER)
        ),
        KC.MACRO(
            Tap(KC.LCTL(KC.C))
        ),
        KC.MACRO(
            Tap(KC.LCTL(KC.V))
        ),
        KC.MACRO(
            Tap(KC.LCTL(KC.Z))
        ),
        KC.MACRO(Press(lambda: toggle_led(0))),
        KC.MACRO(Press(lambda: toggle_led(1))),
        KC.MACRO(Press(lambda: toggle_led(2))),
        KC.MACRO(Press(lambda: toggle_led(3))),
        KC.MACRO(Press(lambda: reset_leds()))
    ]
]

if __name__ == '__main__':
    keyboard.go()
