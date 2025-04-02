# Simon Says Game

A modern implementation of the classic Simon Says memory game. This project uses an Arduino UNO to create an engaging memory game with lights and sounds.

## Features

- Classic Simon Says gameplay with 4 colored buttons and LEDs
- Two game modes:
  - Memory Mode: Single player mode where you need to remember and repeat sequences
  - Battle Mode: Two-player mode where players take turns adding to the sequence
- Easter Egg: Hidden BeeGees music mode
- Interactive LED and sound feedback
- Supports up to 13 rounds of gameplay

## Hardware Requirements

- Arduino UNO
- 4 LEDs:
  - 1x Red LED
  - 1x Blue LED
  - 1x Green LED
  - 1x Yellow LED
- 4 Push Buttons
- 1 Piezo Buzzer
- 4x 220Ω Resistors (for LEDs)
- 4x 10kΩ Resistors (for buttons)
- Jumper Wires
- Breadboard

## Pin Connections

```
LED Connections:
- Red LED: Pin 13
- Green LED: Pin 12
- Blue LED: Pin 11
- Yellow LED: Pin 10

Button Connections:
- Red Button: Pin 9
- Green Button: Pin 8
- Blue Button: Pin 7
- Yellow Button: Pin 6

Buzzer Connection:
- Buzzer: Pin 5
```

## Wiring Instructions

1. LED Setup:
   - Connect the anode (longer leg) of each LED through a 220Ω resistor to its corresponding Arduino pin
   - Connect all LED cathodes (shorter legs) to GND

2. Button Setup:
   - Connect one side of each button to its corresponding Arduino pin
   - Connect the other side of each button to GND
   - Connect a 10kΩ pull-up resistor from each button pin to 5V

3. Buzzer Setup:
   - Connect the positive (red) wire of the buzzer to pin 5
   - Connect the negative (black) wire to GND

## Software Setup

1. Install Arduino IDE from [arduino.cc](https://www.arduino.cc/en/software)
2. Open `Base.c` in Arduino IDE
3. Select "Arduino UNO" from Tools > Board menu
4. Select the correct COM port from Tools > Port menu
5. Click the Upload button to program the Arduino

## Game Modes

### Memory Mode (Default)
- Press any button to start
- Watch and remember the sequence of lights
- Repeat the sequence by pressing the buttons in the same order
- Each successful round adds one more step to the sequence
- Win by completing 13 rounds
- Lose by making a mistake or taking too long

### Battle Mode
- Hold the green button during startup to enter battle mode
- Players take turns adding one step to the sequence
- Each player must repeat the entire sequence before adding their step
- First player to make a mistake loses

### Easter Egg Mode
- Hold the yellow button during startup to activate BeeGees mode
- Watch the LEDs light up in sequence while listening to the BeeGees melody

## Troubleshooting

1. LEDs not lighting up:
   - Check LED polarity (longer leg should go to Arduino pin through resistor)
   - Verify resistor connections
   - Test different pins

2. Buttons not responding:
   - Verify button connections
   - Check pull-up resistor connections
   - Test button continuity

3. No sound:
   - Check buzzer polarity
   - Try different pins
   - Verify buzzer is not damaged

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original Simon Says game code by SparkFun Electronics
- Modified for Arduino UNO with improved game modes 