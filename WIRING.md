# 6-Wheel Rover Wiring & Pin Connections

This document outlines the hardware connections required to link your Raspberry Pi 4 Model B to the Motor Driver and Camera for the HexaRover project. 

The configuration in the code (`config.py`) matches the pinout described below.

## 1. Motor Driver Connections

We are using a dual-channel motor driver (like an L298N or Cytron). Because this is a skid-steer 6-wheel rover, you will wire the **three left motors in parallel** to Channel A, and the **three right motors in parallel** to Channel B.

### Raspberry Pi GPIO to Motor Driver (Logic)
| Motor Driver Pin | Raspberry Pi 4 Pin | BCM / GPIO Number | Function |
| :--- | :--- | :--- | :--- |
| **IN1** (Left Forward) | Physical Pin 11 | **GPIO 17** | Drives the left wheels forward |
| **IN2** (Left Backward)| Physical Pin 13 | **GPIO 27** | Drives the left wheels backward |
| **IN3** (Right Forward)| Physical Pin 15 | **GPIO 22** | Drives the right wheels forward |
| **IN4** (Right Backward)| Physical Pin 16 | **GPIO 23** | Drives the right wheels backward |

> **Note:** If your motor driver requires PWM for speed control (like ENA and ENB pins on an L298N), you should connect them to a 5V source (or use jumper caps) to keep them running at full speed, as `gpiozero.Robot` can control speed via PWM on the standard IN pins.

### Motor Driver to Motors (Power)
- **Motor A (Out 1 & Out 2):** Connect the positive and negative terminals of all 3 Left Motors here.
- **Motor B (Out 3 & Out 4):** Connect the positive and negative terminals of all 3 Right Motors here.

*(If the motors spin the wrong way during testing, simply flip the positive and negative wires for that specific side).*

## 2. Power Connections

> [!WARNING] 
> **Never** power the motors directly from the Raspberry Pi's 5V pins. The motors will draw too much current and instantly destroy the Pi.

1. **Battery to Motor Driver:** Connect your main battery pack (e.g., 7.4V LiPo or 12V battery depending on your motors) to the `12V` (or `VCC`) and `GND` inputs on the motor driver.
2. **Motor Driver to Pi (Optional):** If your motor driver has a built-in 5V regulator (like L298N), you can power the Raspberry Pi by running a wire from the driver's `5V Out` to the Pi's `5V Pin` (Physical Pin 2 or 4), and sharing the ground. Alternatively, use a dedicated power bank for the Pi.
3. **Common Ground:** **CRITICAL!** You must connect a wire from the Motor Driver's `GND` to any `GND` pin on the Raspberry Pi (e.g., Physical Pin 6). If they do not share a common ground, the control signals will not work.

## 3. Camera Connection

1. Locate the **CSI Camera Port** on the Raspberry Pi 4 (located between the HDMI port and the audio jack).
2. Gently pull up the plastic tab on the port.
3. Insert the ribbon cable of the Pi Camera. Make sure the **blue marking** on the cable faces the Ethernet port/USB ports (away from the HDMI ports), and the bare silver contacts face the HDMI ports.
4. Push the plastic tab back down to lock the cable in place.
