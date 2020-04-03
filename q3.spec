# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
pick_up, 1
drop, 1

CompileOptions:
convexify: True
parser: structured
symbolic: False
use_region_bit_encoding: True
synthesizer: jtlv
fastslow: False
decompose: True

CurrentConfigName:
Untitled configuration

Customs: # List of custom propositions
carrying_cup

RegionFile: # Relative path of region description file
q3.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
empty_cup, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
r4 = p6
r5 = p5
r6 = p4
r7 = p3
r1 = p9
r2 = p8
r3 = p7
others = p1
hall4 = p10
Kitchen = p14
hall2 = p15, p16
hall3 = p11
hall1 = p13

Spec: # Specification in structured English
# Initial conditions
Env starts with false
Robot starts in Kitchen with false

# Assumptions about the environment
If you are in Kitchen then do not empty_cup
If you are in (hall1 or hall2 or hall3 or hall4) then do not empty_cup
# Define robot safety including how to pick up
Do pick_up if and only if you are sensing empty_cup and you are not activating carrying_cup
#If you are activating pick_up then stay there
carrying_cup is set on pick_up and reset on drop
Do drop if and only if you are in Kitchen and you are activating carrying_cup

If you did not activate carrying_cup then always not Kitchen
If you are not activating carrying_cup then always not Kitchen


# Patrol goals
Group rooms is r1, r2, r3, r4, r5, r6, r7
If you are not activating carrying_cup then visit all rooms
if you are activating carrying_cup then visit Kitchen

