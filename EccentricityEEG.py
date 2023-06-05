## Base Program
from psychopy import visual, core, event, gui
import os, csv, time, random, math

# Constants
NUM_TRIALS = 10
DIRECTIONS = ["head", "left hand", "right hand", "both hands", "legs"]
MAX_TRIALS = NUM_TRIALS_PER_TYPE * (NUM_DIRECTIONS + 1)

# time to wait = MIN_TIME_TO_WAIT + COEFF_TIME_TO_WAIT * ContinuousUniform([0,1])
TIME_TO_WAIT = 0.1

# record information
date = time.strftime("%y-%m-%d")
startTime = time.strftime("%H-%M-%S")

expInfo = {'subject': '', 'date' : date, 'start time' : startTime};
dlg = gui.DlgFromDict(dictionary = expInfo, sortKeys = False, title = 'user input')
if dlg.OK == False:
    core.quit();

# Create window
win = visual.Window(fullscr = True, units = 'deg', monitor = "TV");

# Write out into the output file
_thisDir = os.path.dirname(os.path.abspath(__file__));
os.chdir(_thisDir);
OUTPATH = os.path.join(os.getcwd(), 'Data');
if not (os.path.exists(OUTPATH)):
    os.makedirs(OUTPATH)

outputFileName = expInfo['subject'] + '_' + expInfo['date'] + '_' + str(expInfo['start time']) + '.csv';
outputFilePath = os.path.join(OUTPATH, outputFileName);
csvFile = open(outputFilePath, 'w');
writer = csv.writer(csvFile);
headings = ('trial','keyPressed','reactionTime','correctness');
writer.writerow(headings);

# Create instructions, fixation cross, and stimulus
instr = visual.TextStim(win = win, text = "You will be shown a crosshair. Shortly after, you will be shown a letter. Keep you gaze on the position of the crosshair throughout the experiment. Press v if the letter is the letter E, b if it is the letter B, and n if it is the letter P. To start, press any key", font = "arial", pos = [0,0]);
cross = visual.ShapeStim(win = win, name = 'Cross', vertices = 'cross', size = 3, fillColor = 'white', lineColor = 'white');

# Draw instructions and update the screen
instr.draw();
win.flip();
keysPressed = event.waitKeys();
win.flip();

# Create variable to store times
times = {'start': 0, 'end': 0}

# use a global variable to always have access to core.Clock();
routineTimer = core.Clock()

for i in range(MAX_TRIALS):
    # Draw fixation cross and update the screen
    cross.draw();
    win.flip();
    
    timeToWait = MIN_TIME_TO_WAIT + COEFF_TIME_TO_WAIT * random.random()
    core.wait(timeToWait)
    
    # Draw stimulus and update the screen
    win.timeOnFlip(times, 'start')
    directionRandom = math.floor(NUM_DIRECTIONS * random.random()) #gives a random integer from 0 to 4
    letterRandom = math.floor(len(LETTERS) * random.random()) #gives a random integer from 0 to 2
    directionalStimuli[letterRandom * NUM_DIRECTIONS + directionRandom].draw() #draws the appropriate stimuli
    answer = KEY_LETTERS[letterRandom]
    DIRECTION_COUNT[directionRandom] += 1
    
    # Flip
    win.flip();
    keysPressed = event.waitKeys(timeStamped = True);
    win.flip();
    core.wait(2);

    # Logic
    key = keysPressed[0];
    times['end'] = key[1];
    reactionTime = times['end'] - times['start']
    isCorrect = key == answer
    
    # Output
    trialOutput = (i, key[0], reactionTime, isCorrect);
    writer.writerow(trialOutput);
    
    # Check we've satsifed the minimum number of trials for each letter
    meetsTrialCountRequirement = True
    for j in DIRECTION_COUNT:
        if j < NUM_TRIALS_PER_TYPE:
            meetsTrialCountRequirement = False
    if meetsTrialCountRequirement:
        break;

csvFile.close()
cortex_obj.close_session()

instr = visual.TextStim(win = win, text = "Thank you for taking part in our experiment! Press any key to exit.", font = "arial", pos = [0,0]);
instr.draw();
win.flip();
event.waitKeys();