**Enclosure Module
Control loop is implemented within each enclosure peripheral so that if communications with the controller fails the functionality of the enclosure is still maintained. Setpoints should have defaults but can be overriden by the controller.

***Requirements
- Provide 5v power for enclosure electronics and overhead light
- Switch Mains power UTH (Under Tank Heater) around setpoint
- Switch Mains power Aux device around setpoint
- Switch 5v power for Overhead Light around time intervals
- Read UTH Temp probe (DS18S20 Probe)
- Accept measurement setpoints to turn UTH on/off
- Accept time updates from Base Controller
- Communicate Measurements to Base Controller

- Warning Buzzer when measurements are outside of range
- Read Enclosure Ambient Temp and Humidity
- Accept datetime tuples to turn on Overhead Light
- Monitor power usage of UTH and Lights

***Components
****Power
- 120V AC In
- 5V DC Out
- 5V DC Switched Out
- 120V Switched Out (Relay)
****Controller
- OUTPUT - Relay x3 (UTH, Overhead Light, Aux)
- INPUT - I2C Sensor x3 (UTH Temp, Amb Temp, Amb Hum)
- COMMS - I2C Peripheral for Controller Comms


**Base Controller

***Requirements
- Accept UTC Temp, Amb Temp, Amb Hum measurements from periferal modules
- Display current value of selected measurement from each peripheral
- Display setpoint value of selected measurement from each peripheral
- Display current values of all measurements from selected peripheral
- Display setpoint values of all measurements from selected peripheral
- Send measurements via WiFi to IOT service (Adafruit.io)
- Receive setpoints via WiFi from IOT service
- Send setpoints to Peripheral Modules
- 