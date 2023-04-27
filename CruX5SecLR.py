## Base Program
from psychopy import visual, core, event, gui
import os, csv, time, random

# Constants
NUM_TRIALS = 30

# Create window
win = visual.Window(fullscr = True, units = 'deg', monitor = "TV");

# Write out into the output file

# Create instructions, fixation cross, and stimulus
instr = visual.TextStim(win = win, text = "To start, press any key", font = "arial", pos = [0,0]);
instr1 = visual.TextStim(win = win, text = "Think Left", font = "arial", pos = [0,0]);
instr2 = visual.TextStim(win = win, text = "Think Right", font = "arial", pos = [0,0]);

# Draw instructions and update the screen
instr.draw();
win.flip();
keysPressed = event.waitKeys(timeStamped = True);

# Create variable to store times
times = {'start': 0, 'end': 0}


for i in range(NUM_TRIALS):
    if i % 2 == 0:
        instr1.draw();
    else:
        instr2.draw();
    win.flip();
    core.wait(4);