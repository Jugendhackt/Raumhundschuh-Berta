def on_button_a_down():
    serial.write_string("ente\n")
    
input.on_button_event(Button.A, ButtonEvent.DOWN, on_button_a_down)

def lichtAn():
    if modus == 0:
        strip.clear()
        strip.show_color(neopixel.rgb(rot, grün, blau))
        strip.show()
    else:
        lauflicht()

def on_button_b():
    global modus
    if modus == 0:
        modus = 1
    else:
        modus = 0
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def umwandeln(zahl: number):
    return abs(zahl) * 255 / 1000
def lauflicht():
    index = 0
    while index <= led_anzahl:
        strip.clear()
        strip.set_pixel_color(index, neopixel.rgb(rot, grün, blau))
        strip.set_pixel_color(index + 1, neopixel.rgb(rot, grün, blau))
        strip.set_pixel_color(index + 2, neopixel.rgb(rot, grün, blau))
        strip.show()
        basic.pause(25)
        index += 1
z = 0
y = 0
x = 0
blau = 0
grün = 0
rot = 0
modus = 0
strip: neopixel.Strip = None
led_anzahl = 0
led_anzahl = 56
schwelle = 1100
Helligkeit = 250
strip = neopixel.create(DigitalPin.P0, led_anzahl, NeoPixelMode.RGB)

def on_forever():
    global x, y, z, rot, blau, grün
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    serial.write_number(x)
    serial.write_string(",")
    serial.write_number(y)
    serial.write_string(",")
    serial.write_number(z)
    serial.write_string("\n")
    rot = umwandeln(x)
    blau = umwandeln(y)
    grün = umwandeln(z)
    if y > schwelle:
        lichtAn()
    if y < schwelle * -1:
        lichtAn()
    if x > schwelle:
        lichtAn()
    if x < schwelle * -1:
        lichtAn()
    if z > schwelle:
        lichtAn()
    if z < schwelle * -1:
        lichtAn()
    basic.pause(100)
basic.forever(on_forever)
