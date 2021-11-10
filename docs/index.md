---
title: Arena PCBs
parent: Generation 2
---

# Arena 12-20
{:.clear}

![Front side of the Arena 12-20](assets/arena_12-20_front.png){:.ifr .pop .clear}
![Back side of the Arena 12-20](assets/arena_12-20_back.png){:.ifr .pop .clear}

The Arena 12-20 is an arena board for the Generation 2 of the Modular LED Display system. This is the board all panels are connected to.

Find the KiCad PCB for a 12-20 arena inside the `arena_12-20` project folder. Have a preview of the [schematic](assets/arena_12-20_schematic.pdf) or the [PCB layout](assets/arena_12-20_pcb.pdf).

This PCB was last ordered around 2011 from <https://protoexpress.com> under the name *panels_arena_12-20 2.0* reference number *192373-IRW* for about $75. Most likely, the content of `arena_12-20/production_v2/arena_12-20_v2p1.zip` was used for this order.

# Arena 12-20 TOP
{:.clear}

![Front side of the Arena 12-20 TOP](assets/arena_12-20_top_front.png){:.ifr .pop .clear}
![Back side of the Arena 12-20 TOP](assets/arena_12-20_top_back.png){:.ifr .pop .clear}

The Arena 12-20 TOP board for the Generation 2 of the Modular LED DIsplay system is only used for mechanical stability. Except for the grounds, there are no other electrical connections between components.

Find the KiCad PCB for a 12-20 arena inside the `arena_12-20_top` project folder. Have a preview of the [schematic](assets/arena_12-20_top_schematic.pdf).

This PCB was last ordered around 2011 from <https://protoexpress.com> under the name *panels_arena_12-20_top 2.0* reference number *192373-IRW* for about $75. Most likely, the content of `arena_12-20_top/production_v1/arena_12-20_top_v1p0.zip` was used for this order.

# Arena 1-1
{:.clear}

![Front side of the Arena 1-1](assets/arena_1-1_front.png){:.ifr .pop .clear}
![Back side of the Arena 1-1](assets/arena_1-1_back.png){:.ifr .pop .clear}

The Arena 1-1 is a single panel arena board for the Generation 2 of the Modular LED Display system. It's primary use is development and debugging.

Find the KiCad PCB for a 1-1 arena inside the `arena_1-1` project folder. Have a preview of the [schematic](assets/arena_1-2_schematic.pdf).

This PCB was last ordered around 2011 from <https://protoexpress.com> under the name *panels_arena_mini 1.0 1.0* reference number *192719-INTJ* for about $2. Most likely, the content of `arena_1-1/production_v1/arena_1-1_v1p0.zip` was used for this order.

# Arena 8-inf
{:.clear}

![Front side of the Arena 8-inf](assets/arena_8-inf_front.png){:.ifr .pop .clear}
![Back side of the Arena 8-inf](assets/arena_8-inf_back.png){:.ifr .pop .clear}

The Arena 8-inf is a planar arena board with 8 panel connectors for the Generation 2 of the Modular LED Display system. It is sometimes referred to as a hallway arena.

Find the KiCad PCB for a 8-inf arena inside the `arena_8-inf` project folder. Have a preview of the [schematic](assets/arena_8-inf_schematic.pdf). In addition the project folder contains a folder named `enclosure`. These files were apparently used to produce some kind of mounting base or enclosure for the 8-inf arena. Based on the vector file format the parts were probably laser cut. There is also a python file to generate a OpenSCAD file.

---
{:.clear}

## Project content

```
├── arena_12_20
│   ├── gerber_v1
│   ├── gerber_v2
│   ├── pdf
│   └── svg
├── arena_12_20_top
│   └── gerber_v1
├── arena_mini
│   ├── gerber_v1
│   └── pdf
├── full
│   ├── 12-ring
│   └── 24-ring
├── mod
├── pdfs
├── planar_arena_8x
│   └── gerber_v0p1
└── planar_arena_8x_base
    ├── v0p1
    └── v0p2
```