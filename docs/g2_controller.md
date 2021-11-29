---
title: Controller
parent: Generation 2
nav_order: 3
---

# Controller

The Controller reads in pattern data from the CF card memory, accepts commands from the PC control program, and sends pattern data to the panels over the TWI bus.

## Controller Hardware {#hardware}

The controller board contains 2 ATmega128 micro controller units (MCU), one is dedicated to reading the pattern data from the CompactFlash card, and the other communicates with the PC and the panels display. The PCB design has been modified, so that connections with a case are rather simple.

- [Controller v2.2 PCB (pdf)](assets/controller_pcb_v2p2.pdf)
- [Controller v2.2 schematic (pdf)](assets/controller_schematic_v2p2.pdf)

## Power supplies

There are 2 options for supplying power to the controller board. An unregulated supply can be connected to the 3-pin header. This power is regulated down to 5 volts and used by the circuitry on the board. An inexpensive DC wall transformer is a good choice, at least 9V and 1-2 A, should be adequate. Use this connector when no panels (or just 1 or 2) are on the controller. The three pins are [`GND` `V+` `GND`], the suggested connector to use is a three pin female: [`GND` `V+` `Blank`]. This way there is no possibility of switching power and ground. The other option is a 5-Pin DIN connector regulated supply. Looking head on at the supply connector, should have (Left to Right): Ground, no connect, Ground, no connect, + 5V. The two pins are not connected, so if a pre-built supply has something on these pins, it will be fine to use this supply, otherwise, modify the connector to this pin-out. The 5V, 10A power supply given in the [parts list](#parts-list) works very well.

## Controller Software

The software running on the Controller is essentially the intermediary between the commands sent from the PControl program detailed in section…, and the panels. The following section explains how and what the code does, read this if you are curious or plan on modifying the code. Hopefully most users can use the system directly from MATLAB and remain blissfully ignorant of these details. The software on the controller has been designed with one goal - making sure patterns are streamed to the panels as quickly as possible, keep this in mind if some of this seems peculiar.

### Programming the Controller

Programming the controller is similar to the process for programming each panel. There is a 6-pin ISP interface for both of the controller board's ATmega128 microprocessors. Let's program the main controller first:

1. Power the Controller board if using the AVR ISP, otherwise power the STK 500, and connect the programming device to the 6 pin Controller ISP header (labeled J7 on the PCB).
2. Open AVR Studio and start the AVR programming tool STK500/AVRISP from the tools menu.
3. Test the connection by selecting the ATmega128 device from the drop-down menu, and then in the advanced tab try to read signature. If these match, move on, otherwise check the connections (rotate connector), restart, etc.
4. Program the fuses - this is done from the __Fuses__ tab - a few options should be set: __ATMega103 compatibility mode__ must be set to OFF, __JTAG interface enable__ must be set to OFF, and clock rate must be set to the last choice: __Ext. Crystal/Resonator High Freq.: Start-up time 16K CK + 64 ms__. It is also a good idea to set __Brown-out detection level at VCC=4.0V__ and __Brown-out detection enabled__.
5. There is no EEPROM file needed for this application.
6. Program the flash on the ATmega128 by selecting the __Program__ tab and selecting the input hex file as: `mainctrl.hex`, and then programming the chip.
7. It is always a good idea to verify both the program and the fuses to make sure these are set correctly.
8. To program the CompactFlash controller, just repeat steps 1-7, except for:
    1. Unplug the CF card if there is one in the socket. Also plug the 6 pin ISP cable into the 6 pin ISP header for the CF controller (labeled J8 on the PCB).
9. program with the file `cfctrl.hex`.

# Parts list {#parts-list}

These parts are required to make 1 controller (compiled around 2006):

| quantity | part description               | source & p/n | price |
|---------:|:-------------------------------|:------------ |------:|
| 2        | [ATmega128](http://www.atmel.com/dyn/resources/prod_documents/doc2467.pdf) microcontroller, 64 TQFP package | Digi-Key, ATMEGA128-16AI-ND | $10 |
| 1        | [CY7C4251V-15AC FIFO](https://datasheet.octopart.com/CY7C4251V-15AC-Cypress-Semiconductor-datasheet-13109.pdf), 32 TQFP package | Digi-Key, 428-1229-ND | $18 |
| 2        | [DAC 8571](http://focus.ti.com/lit/ds/symlink/dac8571.pdf), I2C 16 bit, 8 MSOP package | Digi-Key, 296-14307-1-ND | $5 |
| 1        | [Maxim RS-232 driver](https://datasheet.octopart.com/MAX233ACPP-Maxim-datasheet-3759.pdf) | Digi-Key, MAX233ACPP-ND | $8 |
| 5        | 150Ohm 1/4W resistor, 1206 package | Digi-Key, 311-150ECT-ND | $0.02 |
| 9        | 10kOhm 1/4W resistor, 1206 package | Digi-Key, 311-10KECT-ND | $0.02 |
| 2        | 16 MHz crystal oscillator          | Digi-Key, X192-ND | $0.70 |
| 1        | BNC connector, vertical PCB, mount | Digi-Key, A24504-ND | $1.50 |
| 1        | CF connector                       | Digi-Key, 478-2012-ND | $3.00 |
| 2        | 10-pin ribbon connector            | Digi-Key, M3AAA-1006R-ND | $2.50 |
| 2        | 6-pin male double-row headers      | Digi-Key, | |
| 1        | 7805T, 5 V regulator (optional)    | Jameco, 51262 | $0.30 |
| 1        | 10uH RF choke (inductor)           | Jameco, 208135 | $0.60 |
| 1        | 10µF capacitors, tantalum          | Jameco, 33689 | $0.60 |
| 8        | 0.1µF coupling caps, tant.         | Jameco, 332110 | $0.20 |
| 2        | 20-pin DIP socket                  | Jameco, 38607CL | $0.10 |
| 5        | rt. Angle, PCB mount LEDs          | Jameco, 104256(gr.), 104248(red) | $0.25 |
| 2        | push button switches               | Jameco | |
| 4        | 22pF (20%) capacitors              | Jameco, 15405 | $0.05 |
| 3        | 9 pin fem. rt. angle D-sub         | Jameco, 104951 | $0.50 |
| 1        | 5 pin fem. DIN connector           | Jameco, 29399 | $0.50 |
| 12       | male single row 0.1" header        | Jameco, 160881 | $0.40 |
| 4        | fem. single row header, 8 pin      | Jameco, 70754 | $0.40 |
| 2        | TWI resistors – std. 1k Ohm        | Jameco, 29663 | peanuts |
| 1        | SPST toggle switch                 | Jameco, 76523 | $1.00 |
| 1        | power supply, 5V, min. 2A          | Jameco, 221487 (w DIN conn.) | $35 |
| 1        | Controller PCB                     | ordered from Advanced Circuits | |

__Notes__: male single row headers are needed in sizes of 2 and 3 - easiest thing to do is cut these from a larger strip. Female single row headers are needed in 8 row size, so easiest thing is to order these as a pre-sized piece from Jameco (also needed for flight arenas).
