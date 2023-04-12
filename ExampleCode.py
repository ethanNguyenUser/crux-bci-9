## Base Program
from psychopy import visual, core, event, gui
import os, csv, time, random

# Constants
NUM_TRIALS = 3

# time to wait = MIN_TIME_TO_WAIT + COEFF_TIME_TO_WAIT * ContinuousUniform([0,1])
MIN_TIME_TO_WAIT = 1
COEFF_TIME_TO_WAIT = 2

# record information
date = time.strftime("%y-%m-%d");
startTime = time.strftime("%H-%M-%S")

expInfo = {'subject': '', 'date' : date, 'start time' : startTime};
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title='user input')
if dlg.OK == False:
    core.quit();

# Create window
win = visual.Window(fullscr = True, units = 'deg', monitor = "TV");

# Write out into the output file
_thisDir = os.path.dirname(os.path.abspath(__file__));
os.chdir(_thisDir);
OUTPATH = os.path.join(os.getcwd(), 'Data');

outputFileName = expInfo['subject'] + '_' + expInfo['date'] + '_' + str(expInfo['start time']) + '.csv';
outputFilePath = os.path.join(OUTPATH, outputFileName);
csvFile = open(outputFilePath, 'w');
writer = csv.writer(csvFile);
headings = ('trial','keyPressed','reactionTime','correctness');
writer.writerow(headings);

# Create instructions, fixation cross, and stimulus
instr = visual.TextStim(win = win, text = "Press f when you see the red circle, j if you see the blue circle. To start, press any key", font = "arial", pos = [0,0]);
cross = visual.ShapeStim(win=win, name='Cross', vertices = 'cross', size = 3, fillColor = 'white', lineColor = 'white');
stimBlue = visual.Circle(win = win, pos = [0,0], fillColor = 'blue', size = 3);
stimRed = visual.Circle(win = win, pos = [0,0], fillColor = 'red', size = 3);
# Draw instructions and update the screen
instr.draw();
win.flip();
keysPressed = event.waitKeys(timeStamped = True);

# Create variable to store times
times = {'start': 0, 'end': 0}

for i in range(NUM_TRIALS):
    # Draw fixation cross and update the screen
    cross.draw();
    win.flip();
    
    timeToWait = MIN_TIME_TO_WAIT + COEFF_TIME_TO_WAIT * random.random()
    core.wait(timeToWait);
    
    # Draw stimulus and update the screen        
    win.timeOnFlip(times, 'start')
    answer = 'f'
    if random.random() > 0.5:
        stimRed.draw();
    else:
        stimBlue.draw();
        answer = 'j'
    win.flip();
    keysPressed = event.waitKeys(timeStamped = True);

    # logic
    key = keysPressed[0];
    times['end'] = key[1];
    reactionTime = times['end'] - times['start']
    isCorrect = (key[0] == answer)

    # output
    trialOutput = (i,key[0],reactionTime,isCorrect);
    writer.writerow(trialOutput);

csvFile.close();