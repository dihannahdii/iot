# Simon Says Game with High Score System

A modern implementation of the classic Simon Says memory game with an integrated high score system. This project combines hardware and software to create an engaging gaming experience with online score tracking.

## Features

- Classic Simon Says gameplay with 4 colored buttons and LEDs
- Two game modes:
  - Memory Mode: Single player mode where you need to remember and repeat sequences
  - Battle Mode: Two-player mode where players take turns adding to the sequence
- Easter Egg: Hidden BeeGees music mode
- WiFi connectivity for online score tracking
- Real-time high score display through web interface
- Modern, responsive web dashboard for viewing scores

## Hardware Requirements

- ESP8266 (NodeMCU or similar)
- 4 LEDs (Red, Green, Blue, Yellow)
- 4 Push Buttons
- 2 Buzzers
- Jumper Wires
- Breadboard (optional)

## Pin Connections

```
LED Connections:
- Red LED: Pin 10
- Green LED: Pin 3
- Blue LED: Pin 13
- Yellow LED: Pin 5

Button Connections:
- Red Button: Pin 9
- Green Button: Pin 2
- Blue Button: Pin 12
- Yellow Button: Pin 6

Buzzer Connections:
- Buzzer 1: Pin 4
- Buzzer 2: Pin 7
```

## Software Requirements

- Arduino IDE
- Required Libraries:
  - ESP8266WiFi
  - ESP8266HTTPClient
  - ArduinoJson

## Setup Instructions

1. Hardware Setup:
   - Connect the LEDs, buttons, and buzzers according to the pin connections above
   - Make sure to use appropriate resistors for the LEDs

2. Software Setup:
   - Install Arduino IDE
   - Install required libraries through Arduino Library Manager
   - Open `Base.c` in Arduino IDE
   - Update WiFi credentials in the code:
     ```cpp
     const char* ssid = "YOUR_WIFI_SSID";
     const char* password = "YOUR_WIFI_PASSWORD";
     const char* serverUrl = "http://YOUR_SERVER_IP:5000/api/scores";
     ```
   - Upload the code to your ESP8266

3. Server Setup:
   - Install Python 3.x
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Flask server:
     ```bash
     python app.py
     ```
   - Access the high scores dashboard at `http://localhost:5000`

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

## High Score System

- Scores are automatically uploaded when winning the game
- View top scores in real-time through the web dashboard
- Scores include:
  - Player name
  - Score (number of rounds completed)
  - Date and time of achievement

## Troubleshooting

1. WiFi Connection Issues:
   - Verify WiFi credentials
   - Check if ESP8266 is within range of the network
   - Ensure server is running and accessible

2. Hardware Issues:
   - Verify all connections are secure
   - Check if LEDs are properly connected with resistors
   - Ensure buttons are properly connected with pull-up resistors

3. Server Issues:
   - Check if Flask server is running
   - Verify port 5000 is not in use
   - Check server logs for error messages

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original Simon Says game code by SparkFun Electronics
- Modified and enhanced with WiFi capabilities and high score system
- Web interface built with Flask and Bootstrap 