---
title: Prerequisites
parent: Generation 2
nav_order: 2
---

# Installation and Prerequisites

There are some basic tools needed to use the system:

- A PC running a recent version of Windows. The PC must have at least 1 serial port, although 2 (or even 3) would be useful. To easily add serial ports to your computer, consider a USB to Serial converter. [Here are some](http://www.usbgear.com/USB-Serial.html).
- [MATLAB](https://www.mathworks.com ) installed on this PC - the code should work on all MATLAB releases, but is currently only tested on releases from 2009 onwards.
- A Programming device for the Atmel microcontrollers. Either the [AVR ISP mkII](http://www.atmel.com/dyn/products/tools_card.asp?tool_id=3808&category_id=163&family_id=607&subfamily_id=760) or the [AVR STK500](http://www.atmel.com/dyn/products/tools_card.asp?tool_id=2735). The AVR ISP [Digi-Key p/n ATAVRISP2-ND](https://www.digikey.com/products/en?keywords=ATAVRISP2-ND) is a stand alone programmer that connects to a PC via USB on one end, and has the 6 pin programming interface which is used to program the controller and the panels. The [AVR STK500](https://www.digikey.com/short/z9zd3h) has the programming interface, but is also a starter kit and development system for Atmel microcontrollers.
- AVR studio or other set of AVR tools - this is useful if you plan to make any modifications to the software running on either the controller or the panels. The AVR studio has a nice GUI for programming Atmel microcontrollers through either the AVR ISP or AVR STK500. More information at www.atmel.com and www.avrfreaks.net.
- Power supplies - see [Controller Hardware](g2_controller.md#hardware) for details.
- Compact Flash (CF) card and reader. Any USB-based CF (or multi-format) reader will work. Even large patterns only require space measured in kilobytes, so any available CF card will be large enough, but it is advisable to get a high speed card. The fastest card we measured was a 128 MB Dane-Elec 45X card.
- Many experiments can be made simpler by generating signals from MATLAB that can be used to encode some information about the current trial (this signal is then acquired along with any other experimental data). An inexpensive and reliable product for doing this is one of the USB DAQ modules from <http://www.mccdaq.com/>. We have been using the 1208 series that has 2 analog output signals and is supported by the MATLAB DAQ toolbox.

__Note__: currently the system seems not to work with cards that are larger than 128 MB. This is certainly a solvable problem, but buying 128 MB cards is the best option currently. These cards are increasingly harder to find, one reason that PDC v3 uses SD cards. One vendor that still carries these is <http://www.flash-memory-store.com/>.
{:.info}

# Download Code & PCB files

This code is no longer officially supported or maintained, but has been used for years by at least 10 labs. The code is distributed _as is_; it works for me and I hope it works for you. __Michael Reiser and the Dickinson Lab are not liable for any damage caused by using (or misusing) this code.__ Remember, programming microcontrollers is not as safe as PC programming, extreme caution must be taken to ensure that all connections are correct, and that the circuit boards are functioning – if anything smells like it is burning or gets hot – turn off immediately and recheck everything.

- [Panel Files Release 2](assets/panels_r2.zip)

There are many changes that are included in the second release:

- New control modes, numeric position control. This uses the function generator to numerically specify the current position. Implemented as a (signed) offset to the position specified by `Panel_com('set_position', [X,Y])`.
- System can now support much larger patterns – previously a frame was limited to one block of the CF memory – 512 bytes. Now multi-block frames are supported. Tested with 48 display gscale patterns (1152 bytes per frame).
- CF reading is slightly faster, no longer reads entire block, but stops once the number of bytes in the frame have been read.
- Row compression: for patterns that consist of identical data for all rows of the pattern. RC is enabled by setting pattern.row_compression = 1; in  the pattern-making script. An RC pattern will just consist of one row instead of 8, resulting is a speedup factor of at least 5. This feature required modification to the code on the main and CF controllers, the panel code, and a few of the MATLAB pattern making and displaying routines.
- Identity compression: For patterns that contain large swaths of pixels that are simply on or off. The controller can check to see if this is the case, and then just send the row-compressed version of the display data for a display that corresponds to a pattern piece that is all one value (works for grayscale too!). This feature is not used at pattern making time, but rather while the pattern is running. Identity compression can be enabled by invoking: `Panel_com('ident_compress_on')` from MATLAB.
- New (simpler) serial port interface from MATLAB. Fixes previous problem sending certain values (byte values above 127) over the serial port.
- Two new digital outputs: pulse to trigger a laser depending on pattern position, and an adjustable clock signal to trigger a camera. These are supported by commands in the `panel_com` function.
- Most of the C code (controller programs and the G3 panel code) is now compatible with newest version of GCC compiler. This required including a legacy.h file.
- Now releasing code for 3 generations of panels. The code in the previous release is now considered Generation 2 (G2) code. Generation 3 (G3) code is only slightly modified from Generation 2 to support a new chip – the ATmega168 (slightly faster, bigger flash), using the same panel PCB. Generation 1 code is included for the convenience of Dickinson Lab members who are still using the original design. All controller code is compatible with all 3 generations of panels.
- The distribution includes PCB files for a 12 display ring, the typical configuration of a flight arena.

All files are being distributed in a single .zip file. This file contains 3 folders:

- `c code` - code for the panels and the controller board. Each subfolder also contains the .hex file needed to program the individual microcontrollers. If no modification will be made to the c code, then the compiled .hex files are sufficient to build the system. To edit and compile the AVR c code, you will need to install a GCC compiler for the Atmel AVRs. We recommend the [WinAVR](http://winavr.sourceforge.net/ ) package, but there are others out there. Some of the modules used in the AVR c code, are taken from the Procyon AVRlib (link broken) package written by Pascal Stang. The code from the AVRlib is included in the distributed .zip file above, so you will not need to download this package, but you are encouraged to do so if you plan to do any serious Atmel programming.
- `schematics` – schematic and PCB files for the panels and the controller. These files were created in Protel 99 SE. Each folder also contains a subfolder with all of the CAD files that are needed to order the PCBs.
- `MATLAB panels code` – contains a folder called `matlabroot` that contains a series of subfolders. To set this up on a new system, the folder should be copied to the `C:\` drive (you want the subfolders to reside under `C:\matlabroot`). It is important to add these new folders and all subfolders to the MATLAB path. There is a file called `panel_control_paths.m` that should be updated with the appropriate paths for the specified files, so that the installation will function on your PC. You will also need to the file [dd.exe](http://www.chrysocome.net/dd) (*Note: the original documentation linked to <http://uranus.it.swin.edu.au/~jn/linux/rawwrite/dd-0.3.zip> which is broken. The file is included in the zip, but should you require a different version, the above link might help you to get started*), but this is included in the folder of other files. This file is necessary to burn images onto the CompactFlash cards (from Windows). In `matlabroot\Panels\IO_tools\` there is a file called `get_CF_drive.m`, this file contains a hard-coded drive letter for the CF drive - you should update this letter to reflect your system.
