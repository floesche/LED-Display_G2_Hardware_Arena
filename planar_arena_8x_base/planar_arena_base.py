from py2scad import *

includePcbs = True 
includePanels = True

# Parameters
xPcb = 12.0*INCH2MM
yPcb = 1.5*INCH2MM
zPcb = 0.0625*INCH2MM
xPanel = 32.0
yPanel = 32.0
zPanel = 10.0

xPanelDisplay = xPanel - 1.0
yPanelDisplay = yPanel - 1.0

mountThruHoleDiam = 0.2570*INCH2MM
mountHoleSpacing = 1.0*INCH2MM
mountHoleInset = 0.5*INCH2MM

pcbThruHoleDiam = 0.2570*INCH2MM
pcbTapHoleDiam = 0.20*INCH2MM
panel2PcbMountHoleGap = 0.65*INCH2MM
pcbHoleSpacing = 3.0*INCH2MM
pcbHoleYPos = 0.75*INCH2MM

xBase = xPcb
yBase = 17.0*INCH2MM
zBase = 0.25*INCH2MM
rBase = 0.25*INCH2MM


# Create arena base plate
# -----------------------------------------------------------------------------
baseHoleList = []

# Create arena mount holes
pcbMountHoleYPos = 0.5*(yPcb + 8*yPanel + 2*panel2PcbMountHoleGap)
for j in (-1,1):
    for i in (-1,0,1):
        xPos = i*pcbHoleSpacing
        yPos = j*pcbMountHoleYPos
        baseHoleList.append((xPos, yPos, pcbTapHoleDiam))

# Add outer mount holes
for j in (-1,1):
    for i in range(-5,6):
        xPos = i*mountHoleSpacing
        yPos = j*(0.5*yBase - mountHoleInset)
        baseHoleList.append((xPos,yPos,mountThruHoleDiam))

base = plate_w_holes(xBase, yBase, zBase, holes=baseHoleList, radius=rBase)

# Create arena pcbs
# -----------------------------------------------------------------------------
pcbHoleList = []

for i in (-1,0,1):
    xPos = i*pcbHoleSpacing
    yPos = -0.5*yPcb + pcbHoleYPos
    pcbHoleList.append((xPos, yPos, pcbThruHoleDiam))

pcb = plate_w_holes(xPcb,yPcb,zPcb, holes=pcbHoleList)
zShift = 0.5*zBase + 0.5*zPcb + 2.0
yShift = pcbMountHoleYPos - (-0.5*yPcb + pcbHoleYPos)
pcb0 = Translate(pcb, v=(0,yShift,zShift))
pcb0 = Color(pcb0,rgba=(0,0,0.9,1))

pcb1 = Rotate(pcb,a=180,v=(0,0,1))
pcb1 = Translate(pcb1,v=(0,-yShift,zShift))
pcb1 = Color(pcb1,rgba=(0,0,0.9,1))

# Create panels
# -----------------------------------------------------------------------------
panel = Cube(size=(xPanelDisplay, yPanelDisplay, zPanel))

zShift = 0.5*zBase + 0.5*zPanel + zPcb
panel = Translate(panel,v=(0,0,zShift))
panel = Color(panel,rgba=(0.0,0.9,0,1.0))

panelList = []
for i in range(-4,5):
    for j in range(-4,5):
        xPos = xPanel*j
        yPos = yPanel*i
        panelTemp = Translate(panel,v=(xPos,yPos,0))
        panelList.append(panelTemp)



# Write open scad programs
# -----------------------------------------------------------------------------

# 3D assembly
prog = SCAD_Prog()
prog.fn = 50
prog.add(base)
if includePcbs:
    prog.add([pcb0,pcb1])
if includePanels:
    prog.add(panelList)
prog.write('planar_arena_base.scad')

# 2D projection
projBase = Projection(base)
prog = SCAD_Prog()
prog.fn = 50
prog.add(projBase)
prog.write('planar_arena_base_proj.scad')





