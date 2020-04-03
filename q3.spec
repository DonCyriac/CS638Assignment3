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
r4 = p8
r5 = p7
r6 = p6
r7 = p5
r12 = p15, p16
r1 = p14
r10 = p13
r3 = p9
r11 = p17, p18
r8 = p4
r9 = p3
r2 = p10
others = p1

Spec: # Specification in structured English
# Initial conditions
Env starts with false
Robot starts in r1 with false

# Assumptions about the environment
# If you were in r1 or r9 or r10 or r11 or r12 then do not empty_cup



# Define robot pickup
Do pick_up if and only if you are sensing empty_cup and you are not activating carrying_cup

Do drop if and only if you are in r1 and you are activating carrying_cup

carrying_cup is set on pick_up and reset on drop

If you are not activating carrying_cup then always not r1


# Patrol goals
Group rooms is r2, r3, r4, r5, r6, r7, r8
If you are not activating carrying_cup then visit all rooms
If you are activating carrying_cup then visit r1

