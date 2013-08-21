from py2scad import *

includePcbs = True 
includePanels = True 
includeLowerSupport = True
includeUpperSupport = True 

# Parameters
xPcb = 12.0*INCH2MM
yPcb = 1.5*INCH2MM
zPcb = 0.0625*INCH2MM
xPanel = 32.0
yPanel = 32.0
zPanel = 10.0
yBaseExtra = 1.5*INCH2MM

yPanelNum = 8
xPanelNum = 8
xPanelDisplay = xPanel - 1.0
yPanelDisplay = yPanel - 1.0

mountThruHoleDiam = 0.2570*INCH2MM
mountHoleSpacing = 1.0*INCH2MM
mountHoleInset = 0.5*INCH2MM

pcbThruHoleDiam = 0.2570*INCH2MM
pcbTapHoleDiam = 0.20*INCH2MM
panel2PcbMountHoleGap = 0.15*INCH2MM 
pcbHoleSpacing = 3.0*INCH2MM
pcbHoleYPos = 0.75*INCH2MM
zHeightPcb = 0.25*INCH2MM

xBase = xPcb - 0.25*INCH2MM
yBase = 2*yPcb + yPanelNum*yPanel + panel2PcbMountHoleGap  + 2*yBaseExtra
zBase = 0.25*INCH2MM
rBase = 0.25*INCH2MM

xSupport = xBase
ySupport = yPanelNum*yPanel
zSupport = 0.125*INCH2MM
rSupport = 0.25*INCH2MM
supportStandoffDiam = 0.5*INCH2MM
supportStandoffThruHoleDiam = 0.62*INCH2MM
supportThruHoleDiam = 0.2570*INCH2MM
supportHoleInset = supportStandoffDiam + 0.05*INCH2MM
supportUpperHolePosList = []
supportLowerHolePosList = []
for i in (-1,1):
    for j in (-1,1):
        xPosUpper = i*(0.5*xSupport - supportHoleInset)
        yPosUpper = j*(0.5*ySupport - supportHoleInset)
        supportUpperHolePosList.append((xPosUpper,yPosUpper))
        xPosLower = i*(0.5*xSupport - supportHoleInset)
        yPosLower = j*(0.5*ySupport - 3*supportHoleInset)
        supportLowerHolePosList.append((xPosLower,yPosLower))


# Create arena base plate
# -----------------------------------------------------------------------------
holeList = []

# Create arena mount holes
pcbMountHoleYPos = 0.5*(yPcb + yPanelNum*yPanel + panel2PcbMountHoleGap)
for j in (-1,1):
    for i in (-1,0,1):
        xPos = i*pcbHoleSpacing
        yPos = j*pcbMountHoleYPos
        holeList.append((xPos, yPos, pcbThruHoleDiam))

# Add outer mount holes
for j in (-1,1):
    for i in range(-5,6):
        xPos = i*mountHoleSpacing
        yPos = j*(0.5*yBase - mountHoleInset)
        holeList.append((xPos,yPos,mountThruHoleDiam))

# Add support plate mount holes
for xPos,yPos in supportLowerHolePosList:
    holeList.append((xPos,yPos,supportThruHoleDiam))

for xPos,yPos in supportUpperHolePosList:
    holeList.append((xPos,yPos,supportThruHoleDiam))

base = plate_w_holes(xBase, yBase, zBase, holes=holeList, radius=rBase)

# Create arena pcbs
# -----------------------------------------------------------------------------
pcbHoleList = []

for i in (-1,0,1):
    xPos = i*pcbHoleSpacing
    yPos = -0.5*yPcb + pcbHoleYPos
    pcbHoleList.append((xPos, yPos, pcbThruHoleDiam))

pcb = plate_w_holes(xPcb,yPcb,zPcb, holes=pcbHoleList)
zShift = 0.5*zBase + 0.5*zPcb + zHeightPcb
yShift = pcbMountHoleYPos - (-0.5*yPcb + pcbHoleYPos) 
pcb0 = Translate(pcb, v=(0,yShift,zShift))
pcb0 = Color(pcb0,rgba=(0,0,0.9,1))

pcb1 = Rotate(pcb,a=180,v=(0,0,1))
pcb1 = Translate(pcb1,v=(0,-yShift,zShift))
pcb1 = Color(pcb1,rgba=(0,0,0.9,1))

# Create panels
# -----------------------------------------------------------------------------
panel = Cube(size=(xPanelDisplay, yPanelDisplay, zPanel))

zShift = 0.5*zBase + 0.5*zPanel + zPcb + zHeightPcb 
panel = Translate(panel,v=(0,0,zShift))
panel = Color(panel,rgba=(0.0,0.9,0,1.0))

panelList = []
for i in range(0,xPanelNum):
    for j in range(0,yPanelNum):
        xPos = xPanel*j - 3.5*xPanel
        yPos = yPanel*i - 3.5*yPanel
        panelTemp = Translate(panel,v=(xPos,yPos,0))
        panelList.append(panelTemp)



# Create upper support plate
# -----------------------------------------------------------------------------
holeList = []
for xPos,yPos in supportUpperHolePosList:
    holeList.append((xPos,yPos,supportThruHoleDiam))
upperSupport = plate_w_holes(xSupport,ySupport,zSupport, holes=holeList, radius=rSupport)

# Create lower support plate
# ----------------------------------------------------------------------------
holeList = []
for xPos,yPos in supportLowerHolePosList:
    holeList.append((xPos,yPos,supportThruHoleDiam))
for xPos,yPos in supportUpperHolePosList:
    holeList.append((xPos,yPos,supportStandoffThruHoleDiam))

lowerSupport = plate_w_holes(xSupport,ySupport,zSupport, holes=holeList, radius=rSupport)

# Write open scad programs
# -----------------------------------------------------------------------------

# 3D assembly
prog = SCAD_Prog()
prog.fn = 50
prog.add(base)
if includeLowerSupport: 
    zShift = -0.5*zSupport + 0.5*zBase+zHeightPcb
    tempPart = Translate(lowerSupport,v=[0,0,zShift])
    prog.add(tempPart)
if includeUpperSupport:
    zShift = +0.5*zSupport + 0.5*zBase + zHeightPcb + zPanel
    tempPart = Translate(upperSupport,v=[0,0,zShift])
    prog.add(tempPart)
if includePcbs:
    prog.add([pcb0,pcb1])
if includePanels:
    prog.add(panelList)
prog.write('planar_arena_base.scad')

# 2D projection of base plate
projBase = Projection(base)
prog = SCAD_Prog()
prog.fn = 50
prog.add(projBase)
prog.write('planar_arena_base_proj.scad')

# 2D projection of lower support plate
projLowerSupport = Projection(lowerSupport)
prog = SCAD_Prog()
prog.fn = 50
prog.add(projLowerSupport)
prog.write('planar_arena_lower_support_proj.scad')

# 2D projection of upper support plate
projUpperSupport = Projection(upperSupport)
prog = SCAD_Prog()
prog.fn = 50
prog.add(projUpperSupport)
prog.write('planar_arena_upper_support_proj.scad')





