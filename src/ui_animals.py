from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)

# Instructions
Label = M5Label("Select number of animals",20,60,0xE5E4E2,FONT_MONT_22)

# Options
txt_color = 0x000000 #black
bgnd_color = 0xF5DEB3 #platinum
w = 60
h = 50
y = 120
x_0 = 10

def x_step(pos):
  x_step = pos*w + x_0 + pos*20
  return x_step

Btn_1 = M5Btn("1", x_step(0), y, w, h, bgnd_color, txt_color, FONT_MONT_22)
Btn_2 = M5Btn("2", x_step(1), y, w, h, bgnd_color, txt_color, FONT_MONT_22)
Btn_3 = M5Btn("3", x_step(2), y, w, h, bgnd_color, txt_color, FONT_MONT_22)
Btn_4 = M5Btn("4", x_step(3), y, w, h, bgnd_color, txt_color, FONT_MONT_22)

