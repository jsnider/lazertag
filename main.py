def on_received_number(receivedNumber):
    global life, my_team
    if (receivedNumber == 2 and my_team == 1) or (receivedNumber == 1 and my_team == 2):
        game.remove_life(1)
        life += -1
    basic.pause(500)
    view()
radio.on_received_number(on_received_number)

# block

''' def on_button_pressed_a():
    global block, block_max
    if block_max > 0 and shooting == 0:
        block = 1
        block_max += -1
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        basic.pause(5000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        block = 0
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    basic.pause(500)
    view()
input.on_button_pressed(Button.A, on_button_pressed_a)
'''

def on_button_pressed_ab():
    global my_team
    if my_team == 0:
        my_team = 1
        basic.show_icon(IconNames.DIAMOND)
    elif my_team == 1:
        my_team = 2
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SQUARE)
    basic.pause(500)
    view()


input.on_button_pressed(Button.AB, on_button_pressed_ab)

# shoot

def on_button_pressed_b():
    global shooting, mag, my_team
    if mag > 0 and shooting == 0:
        shooting = 1
        if my_team == 1:
            radio.send_number(1)
            basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
            basic.show_leds("""
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            """)
            basic.show_leds("""
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
            mag += -1
        elif my_team == 2:
            radio.send_number(2)
            basic.clear_screen()
            led.toggle(2, 2)
            led.toggle(2, 1)
            led.toggle(2, 0)
            mag += -1
        else:
            basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
            basic.pause(500)
            view()
        shooting = 0
    else:
        basic.show_leds("""
            . # # # .
            . # . # .
            . # # # .
            . # # . .
            . # . # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    basic.pause(500)
    view()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global mag
    if mag <= 0:
        for index in range(3):
            basic.show_leds("""
                . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # # # .
                """)
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        mag = 3
        basic.pause(500)
        view()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def view():
    global plats, plats2
    basic.clear_screen()
    while plats <= life:
        led.plot(0, plats - 1)
        plats += 1
    while plats2 <= mag:
        led.plot(4, plats2 - 1)
        plats2 += 1
    plats2 = 0
    plats = 0

plats2 = 0
plats = 0
my_team = 0
radio.set_group(128)
life = 5
mag = 3
shooting = 0
game.set_life(life)