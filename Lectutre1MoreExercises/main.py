# Read User Input
import math

WORK_SPACE_WIDTH = 70
WORK_SPACE_LENGHT = 120
CORIDOR = 100
FRONT_DOOR = 1
ROSTRUM = 2

length_in_meters = float(input())
width_in_meters = float(input())

# Logic

lenght_in_cm = length_in_meters * 100
width_in_cm = width_in_meters * 100
total_desks_per_row = math.floor((width_in_cm - CORIDOR) / WORK_SPACE_WIDTH)
total_desks_per_collumn = math.floor(lenght_in_cm / WORK_SPACE_LENGHT)
total_desks = total_desks_per_row * \
              total_desks_per_collumn - \
              (FRONT_DOOR + ROSTRUM)

# Print Output
print(total_desks)