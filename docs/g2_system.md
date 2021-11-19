---
title: Generation 2
has_children: true
has_toc: false
nav_order: 20
---

# Panels System

For a long time and since [Michael Reiser](https://www.janelia.org/people/michael-reiser) started an online documentation of the Modular LED Displays more than a decade ago, this introductory text had emphasized the community aspect of this endeavor. It is no small feat to design and produce electrical systems with high temporal and spatial precision that work reliably in many different scientific settings. Many labs have taken this task upon themselves and are building and using these systems. By now, the [Generation 2](g2_system.md) and [3]({{site.baseurl}}/Generation%203/) Modular LED Displays have a large user basis across many scientific labs. We are also confident that the additional capabilities of the [Generation 4]({{site.baseurl}}/docs/g4_system.html) system will further the spread of this new stimulus presentation systems, especially once we had the chance to explain the advantages in the upcoming methods paper. Through all this, the exchange of experiences coupled with suggestions and improvements has benefited the system. Please [keep sending]({{site.baseurl}}/Contact) updates, improvements, and troubleshooting suggestions -- this is invaluable support for us in making the current and future systems better, but also for any future scientist who wants to replicate one of the systems in their setup.

To get started with [Generation 2](g2_system.md) or even a [Generation 3]({{site.baseurl}}/Generation%203/) system, please have a look at this current page where we show some technical details of the system. A more general [user guide](g2_user-guide.md), written by Mark Frye, Michael Dickinson, and Michael Reiser, gives a nice and informal introduction to this system and its use as a flight arena for flies. Finally, we still consider the dated but [timeless paper](https://doi.org/10.1016/j.jneumeth.2007.07.019) that introduced the Modular LED Display back in 2007 a useful reference.

__Note__: For historical reasons we provide some information on how to [install](g2_prerequisites.md) a Generation 2 system, although we would strongly discourage anyone from doing this at this point. Follow the documentation of [Generation 4]({{site.baseurl}}/docs/g4_system.html) system instead or, if you want to use a less expensive system, have a look at the [Generation 3]({{site.baseurl}}/Generation%203/) Modular LED Display instead.
{:.info}

# System Overview

The system has been designed to allow for rapid development of behavioral (visual) stimuli. There are three components to the system:

- __The displays__: These are 8×8 dot matrix displays of LEDs (either ready-made components or custom made [__LED matrices__]({{site.baseurl}}/Generation%202/LED-Arrays/docs/)) with the [__panel__]({{site.baseurl}}/Generation%202/Panels/docs/) electronics to turn individual LEDs on and off.
- __The controller__: a custom designed microprocessor circuit that communicates with a PC via the serial port and to the panels using a rapid serial interface (TWI). Note that TWI is Atmel's name for their own implementation of the I2C bus, a standard developed by Phillips.
- __PC software__: written in MATLAB, there are tools for generating patterns and sending commands to the controller.

In all the documentation that follows, we will try to use this terminology consistently:

- __The system__: refers to all of the components: displays, panels, controller, etc.
- __Setup__: refers to your particular configuration. This is mostly used in the context of the particular way in which you have the panels connected to the controller.
- __The Controller__: refers to the controller circuit board that is described in Section controller. This can be somewhat confusing, because the panels and controller boards both have microcontrollers on them, which both act as controllers. Furthermore, the MATLAB program is also controlling the controller. However, *the controller* will always refer to the controller circuit.
- __A Panel__: - refers to the module that is composed of both the circuit board and the LED display.
- __PControl__: - is the name of the MATLAB gui.

# TODO & Wish List

__Note__: This is the initial wish list published in 2006 with some additional comments on the status.
{:.info}

As presented the system is fully functional and has been in regular use for more than two years. However, there are many features that will improve the system. Here is a list of suggested projects. Some of these will be completed by the time you read this, (many will certainly not be). If anyone is interested in tackling these or suggesting other projects, please get in [contact]({{site.baseurl}}/Contact).

- programming of the panels from the MATLAB GUI, maybe even address them during programming. This would be done using the command line interface to the AVR Studio, or similar. *Possible but not yet implemented in Generation 3*
- A small box that converts ±5 V to two distinct 0-5 V lines, mapping positive voltage to one and negative to the other. This would really simplify using certain signals with controller. Ideally, put 2 of these in one box (will need independent power). __Not necessary with Generation 3, since inputs and outputs can go ±5 V.__
- program panels when they are plugged in, so they don't need to be programmed independently. Apparently this is possible, especially since the panels are set up to communicate with the TWI interface. Look at __Boot Loader Support__ section in the AVR documentation. __Generation 3 and more recent software development supports this.__
- re-mapable greenscales – the idea here is to be able to use binary, 2 level, patters and then be able to arbitrarily map the 0 and 1 values to any of the 8 greenscale levels. This scheme has basically been worked out (is in the distributed panels code, but commented out). This system needs to be tested, etc.
- more efficient CF reading – that would start moving the bytes from the FIFO before the pattern is completely dumped – this should provide at least 10% faster frame rates. __Superseded by faster SD card reading in Generation 3__
- more user-friendly installation that checks the CF card location, makes a temp folder if necessary, etc.
- Some buttons on the PControl GUI for quickly linking to experiment scripts.
- Move storage of internal function generator functions onto the CF card, maybe increase the temporal resolution (100 Hz seems reasonable), and allow the function buffer length to vary. __Implemented in Generation 3__
