# Input: lines like "L<number>" or "R<number>"
# Output: number starts at 50, L decreases, R increases
#         range is 0 to 99 (out of bounds -> wrap around)
#         how many times does it hit 0?
#         part 1: at the end of a move / part 2: also mid-move
 
from tkinter import *
import math
import time
 
pointer_ids = []
instruction_id = -1
number_instructions_id = -1
password_part1_id = -1
password_part2_id = -1
 
old_pointer = -1
number_hits_part1 = 0
number_hits_part2 = 0
number_instructions_so_far = 0
 
# *** graphics functions ***
 
def get_radians(index):
  return math.tau * index / 100
 
def get_x(index, distance):
  return int(250 + math.sin(get_radians(index)) * distance)
 
def get_y(index, distance):
  return int(250 - math.cos(get_radians(index)) * distance)
 
def refresh_display():
  root.update_idletasks()
  root.update()
 
def draw_pointer():
  global old_pointer # required to be able to alter it
  if old_pointer >= 0:
    canvas.itemconfigure(pointer_ids[old_pointer], state=HIDDEN)
  old_pointer = pointer
  canvas.itemconfigure(pointer_ids[pointer], state=NORMAL)
  refresh_display()
 
def update_password():
  canvas.itemconfigure(password_part1_id, text="Part 1: " + str(number_hits_part1))
  canvas.itemconfigure(password_part2_id, text="Part 2: " + str(number_hits_part2))
  refresh_display()
 
def update_instruction():
  global number_instructions_so_far
  canvas.itemconfigure(instruction_id, text=instruction)
  number_instructions_so_far += 1
  canvas.itemconfigure(number_instructions_id, text=str(number_instructions_so_far) + " of " + str(number_instructions))
  refresh_display()
 
# *** graphics setup ***
 
root = Tk()
canvas = Canvas(root, width=500, height=500, background='white')
 
# without this, the window would render as empty
canvas.pack()
 
# draw outline of dial
# coordinates = left/top/right/bottom of bounding box
canvas.create_oval(50, 50, 450, 450, fill='white', outline='black', width=5)
 
# draw labels around dial
for index in range(0, 100, 5):
  radians = get_radians(index)
  x = get_x(index, 225)
  y = get_y(index, 225)
  canvas.create_text(x, y, text=str(index))
 
# create pointer_ids
for index in range(0, 100):
  x = get_x(index, 175)
  y = get_y(index, 175)
  pointer_ids.append(canvas.create_line(250, 250, x, y, fill='black', arrow=LAST, state=HIDDEN))
 
# draw pointer
pointer = 50
draw_pointer()
 
# draw stuff for current instruction
canvas.create_text(75, 25, text="Instruction:")
instruction_id = canvas.create_text(25, 50, text="")
 
# draw stuff for number of instructions
canvas.create_text(400, 25, text="Instruction count:")
number_instructions_id = canvas.create_text(440, 50, text="")
 
canvas.create_text(450, 450, text="Password:")
password_part1_id = canvas.create_text(450, 470, text="")
password_part2_id = canvas.create_text(450, 485, text="")
update_password()
 
# *** solve the puzzle ***
 
time.sleep(10) # allow time to start screen capture
 
file_preview = open("01_example.txt", "r")
number_instructions = 0
for line in file_preview:
  number_instructions += 1
 
file = open("01_example.txt", "r")
for line in file:
  instruction = line.replace("\n", "")
  update_instruction()
  direction = -1 if instruction[0] == "L" else 1
  for steps in range(0, int(instruction[1:])):
    pointer = (pointer + direction) % 100
    draw_pointer()
    time.sleep(0.01)
    if pointer == 0:
      number_hits_part2 += 1
      update_password()
      time.sleep(0.1)
  if pointer == 0:
    number_hits_part1 += 1
    update_password()
    time.sleep(0.1)
 
canvas.create_text(50, 450, text="Done!")
root.mainloop()