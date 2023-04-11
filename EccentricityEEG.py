## Base Program
from psychopy import visual, core, event, gui
import os, csv, time, random

# Emotiv
from psychopy.hardware import emotiv
from psychopy import visual, core

# Constants
NUM_TRIALS_PER_TYPE = 50
typesOfTrials = 3
maxTrials = NUM_TRIALS_PER_TYPE * (typesOfTrials+1)

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
if not (os.path.exists(OUTPATH)):
    os.makedirs(OUTPATH)

outputFileName = expInfo['subject'] + '_' + expInfo['date'] + '_' + str(expInfo['start time']) + '.csv';
outputFilePath = os.path.join(OUTPATH, outputFileName);
csvFile = open(outputFilePath, 'w');
writer = csv.writer(csvFile);
headings = ('trial','keyPressed','reactionTime','correctness');
writer.writerow(headings);

# Create instructions, fixation cross, and stimulus
instr = visual.TextStim(win = win, text = "You will be shown a letter. Press v if it is the letter E, b if it is the letter B, and n if it is the letter P. To start, press any key", font = "arial", pos = [0,0]);
cross = visual.ShapeStim(win=win, name='Cross', vertices = 'cross', size = 3, fillColor = 'white', lineColor = 'white');
eLeft = visual.TextStim(win = win, text = "E", font = "arial", pos = [-30,0], height = 3);
eCenter = visual.TextStim(win = win, text = "E", font = "arial", pos = [0,0], height = 3);
eRight = visual.TextStim(win = win, text = "E", font = "arial", pos = [30,0], height = 3);
bLeft = visual.TextStim(win = win, text = "B", font = "arial", pos = [-30,0], height = 3);
bCenter = visual.TextStim(win = win, text = "B", font = "arial", pos = [0,0], height = 3);
bRight = visual.TextStim(win = win, text = "B", font = "arial", pos = [30,0], height = 3);
pLeft = visual.TextStim(win = win, text = "P", font = "arial", pos = [-30,0], height = 3);
pCenter = visual.TextStim(win = win, text = "P", font = "arial", pos = [0,0], height = 3);
pRight = visual.TextStim(win = win, text = "P", font = "arial", pos = [30,0], height = 3);
stimCenter = visual.Circle(units = 'deg', win = win, pos = [0,0], fillColor = 'white', size = 3);
#stimLeft15 = visual.Circle(units = 'deg', win = win, pos = [-15,0], fillColor = 'white', size = 3);
stimLeft30 = visual.Circle(units = 'deg', win = win, pos = [-30,0], fillColor = 'white', size = 3);
#stimRight15 = visual.Circle(units = 'deg', win = win, pos = [15,0], fillColor = 'white', size = 3);
stimRight30 = visual.Circle(units = 'deg', win = win, pos = [30,0], fillColor = 'white', size = 3);

# Draw instructions and update the screen
instr.draw();
win.flip();
keysPressed = event.waitKeys();
win.flip();

# Create variable to store times
times = {'start': 0, 'end': 0}

# use a global variable to always have access to core.Clock();
routineTimer = core.Clock()

# starts recording
cortex_rec = visual.BaseVisualStim(win=win, name="cortex_rec")
cortex_obj = emotiv.Cortex(subject = expInfo['subject'])

leftCount = 0;
rightCount = 0;
midCount = 0;

for i in range(maxTrials):
    # Draw fixation cross and update the screen
    cross.draw();
    win.flip();
    
    timeToWait = MIN_TIME_TO_WAIT + COEFF_TIME_TO_WAIT * random.random()
    core.wait(timeToWait);
    
    # Draw stimulus and update the screen        
    win.timeOnFlip(times, 'start')
    uniformRandom = random.random()
    letterRandom = random.random()
    answer = 'b'
#    if uniformRandom < 0.2:
#        stimCenter.draw()
#    elif uniformRandom < 0.4:
#        stimLeft15.draw()
#        ivalue = "3"
#    elif uniformRandom < 0.6:
#        stimLeft30.draw()
#        ivalue = "4"
#    elif uniformRandom < 0.8:
#        stimRight15.draw()
#        ivalue = "5"
#    else:
#        stimRight30.draw()
#        ivalue = "6"
    if uniformRandom < 0.33333:
        if letterRandom < 0.33333:
            eCenter.draw()
            answer = 'v'
        elif letterRandom < 0.66666:
            bCenter.draw()
            answer = 'b'
        else:
            pCenter.draw()
            answer = 'n'
        midCount+=1
    elif uniformRandom < 0.66666:
        if letterRandom < 0.33333:
            eLeft.draw()
            answer = 'v'
        elif letterRandom < 0.66666:
            bLeft.draw()
            answer = 'b'
        else:
            pLeft.draw()
            answer = 'n'
        leftCount+=1
    else:
        if letterRandom < 0.33333:
            eRight.draw()
            answer = 'v'
        elif letterRandom < 0.66666:
            bRight.draw()
            answer = 'b'
        else:
            pRight.draw()
            answer = 'n'
        rightCount+=1
    # Emotiv
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    delta_time = tThisFlip - t
    answerint = "1";
    if answer == 'v':
        answerint = "1";
    elif answer == 'b':
        answerint = "2";
    elif answer == 'n':
        answerint = "3";
    cortex_obj.inject_marker(value = answerint, label = 'stim', delta_time = delta_time)
    
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
    
    
    # output
    trialOutput = (i,key[0],reactionTime, isCorrect);
    writer.writerow(trialOutput);
    
    if(rightCount >= NUM_TRIALS_PER_TYPE and leftCount >= NUM_TRIALS_PER_TYPE and midCount >=NUM_TRIALS_PER_TYPE):
        break;

csvFile.close();
cortex_obj.close_session()

instr = visual.TextStim(win = win, text = "Thank you for taking part in our experiment! Press any key to exit.", font = "arial", pos = [0,0]);
instr.draw();
win.flip();
event.waitKeys();