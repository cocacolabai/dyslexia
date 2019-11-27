#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division  
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  
import numpy as np  
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  

core.wait(2)#give the system time to settle
globalClock = core.Clock()  # to track the time since pulse was received from scanner
trialClock = core.Clock() # to track the time of each trial
instructionsClock = core.Clock() # to track the time the instructions are on the screen waiting for the scanner pulse
fixationClock=core.Clock()

# Dialog box to store info about the experiment session
expName = 'DYS'
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName

# Setup the Window
win = visual.Window(size=(800, 600), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

# Initialize and pre-load as much as possible before starting
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text=u'Choose the side (left or right) with the word that sounds correct.\r\n',    font=u'Monaco',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for fixation
fixationText = visual.TextStim(win=win, ori=0, name='fixationText',
    text=u'+',    font=u'Monaco',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color=u'green', colorSpace=u'rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "trial"
imgStimulus = visual.ImageStim(win=win, name='imgStimulus',
    image='sin', mask=None,
    ori=0, pos=[0, 100], size=[500, 500], units='pix',
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
combinedWords = visual.TextStim(win=win, ori=0, name='combinedWords',
    text='default text',    font='Monaco',
    pos=[0, -0.45], height=0.15, wrapWidth=5000,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Setup filename for saving
filename = u'fMRI_data' + os.path.sep + '%s_%s_%s' %(expInfo['participant'],'Phono', expInfo['date'])
# Initialize ExperimentHandler for data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  
endExpNow = False  

# set up handler to look after randomisation of conditions etc
trialLoop = data.TrialHandler(nReps=1, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'Conditions_Phonologic.xlsx'),
    seed=None, name='trialLoop')
thisExp.addLoop(trialLoop)  # add the loop to the experiment
thisTrialLoop = trialLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrialLoop.rgb)
if thisTrialLoop != None:
    for paramName in thisTrialLoop.keys():
        exec(paramName + '= thisTrialLoop.' + paramName)

# Prepare for instructions
instructionsClock.reset()
trigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
trigger.status = NOT_STARTED
instructionsComponents = []
instructionsComponents.append(instrText)
instructionsComponents.append(trigger)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    t = instructionsClock.getTime()

    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        instrText.tStart = t  
        instrText.setAutoDraw(True)
    # *trigger* updates
    if t >= 0.0 and trigger.status == NOT_STARTED:
        trigger.tStart = t  
        trigger.status = STARTED
        event.clearEvents(eventType='keyboard')
    if trigger.status == STARTED:
        theseKeys = event.getKeys('5')
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  
            continueRoutine = False
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()
#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



ISI = 6.0
correct = 0
difficulty = 3
streakCorr = 0
maxTrials = 60
numTrials = 1
numCorr = 0

trialCountDown = core.CountdownTimer()
response = event.BuilderKeyResponse()  # create an object of type KeyResponse

globalClock.reset()
for thisTrialLoop in trialLoop:
    trialStartTime=globalClock.getTime()
    t=trialStartTime # current value of time
    trialClock.reset() # counts up time
    trialCountDown.reset() # counts down time
    trialCountDown.add(ISI*numTrials-t)

    currentLoop = trialLoop
    if thisTrialLoop != None:
        for paramName in thisTrialLoop.keys():
            exec(paramName + '= thisTrialLoop.' + paramName)
    imgArray = [imgfile1, imgfile2, imgfile3, imgfile4, imgfile5]
    combinedTextArray = [text1, text2, text3, text4, text5]
    widthArray = [w1/2, w2/2, w3/2, w4/2, w5/2]
    heightArray = [h1/2, h2/2, h3/2, h4/2, h5/2]

    imgStimulus.setImage(imgArray[difficulty - 1])
    combinedWords.setText(combinedTextArray[difficulty - 1])

    # keep track of which components have finished
    response.status = NOT_STARTED
    trialComponents = []
    trialComponents.append(imgStimulus)
    trialComponents.append(ISI)
    trialComponents.append(combinedWords)
    trialComponents.append(response)

    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
 
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
         # *imgStimulus* updates
        if imgStimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            imgStimulus.tStart = t  # underestimates by a little under one frame
            imgStimulus.setAutoDraw(True)
        elif imgStimulus.status == STARTED and (trialCountDown.getTime()) < 0: #most of one frame period left
#            print "countdown %.4f too low" %(trialCountDown.getTime())
            imgStimulus.setAutoDraw(False)
        if imgStimulus.status == STARTED:  # only update if being drawn
            imgStimulus.setSize([widthArray[difficulty - 1], heightArray[difficulty - 1]], log=False)
        
        # *combinedWords* updates
        if combinedWords.status == NOT_STARTED:
            # keep track of start time/frame for later
            combinedWords.tStart = t  # underestimates by a little under one frame
            combinedWords.setAutoDraw(True)
        elif combinedWords.status == STARTED and (trialCountDown.getTime()) < 0: #most of one frame period left
            combinedWords.setAutoDraw(False)
        
        # *response* updates
        if response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif response.status == STARTED and (trialCountDown.getTime()) < 0: #most of one frame period left
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', '1', '2', '3', '4'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
#                print "response found at countdown %.4f" %(trialCountDown.getTime())
                # was this 'correct'?
                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
       response.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': response.corr = 1  # correct non-response
       else: response.corr = 0  # failed to respond (incorrectly)
    # store data for trialLoop (TrialHandler)
    trialLoop.addData('response.keys',response.keys)
    trialLoop.addData('response.corr', response.corr)
    trialLoop.addData('difficulty', difficulty)
    trialLoop.addData('current_time', trialClock.getTime())
    if response.keys != None:  # we had a response
        trialLoop.addData('response.rt', response.rt)
        
    numTrials = numTrials + 1
    if response.corr == 1:
        numCorr = numCorr + 1
        streakCorr = streakCorr + 1
        if streakCorr >= 3:
            streakCorr = 0
            difficulty += 1
            if difficulty > 5:
                difficulty = 5
    else: 
        streakCorr = 0
        difficulty -= 1
        if difficulty < 1:
            difficulty = 1
            
            
    #------Prepare to start Routine "fixation"-------
    fixationClock.reset()  # clock 
    fixationText.setText(u'+')
    fixationText.setSize(5)
    fixationText.setColor(u'white')
    fixationComponents = []
    fixationComponents.append(fixationText)


    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "fixation"-------
    continueRoutine = True
    while continueRoutine and (trialCountDown.getTime()) > 0:
        # get current time
        t = fixationClock.getTime()        
        # *fixation* updates
        if fixationText.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationText.tStart = t  # underestimates by a little under one frame
            fixationText.setAutoDraw(True)
        elif fixationText.status == STARTED and (trialCountDown.getTime()) < 0: 
            fixationText.setAutoDraw(False)
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()


#    print "numtrials: %.2f difficulty is %.2f t is %.4f globalClock is %.4f trialClock is %.4f trialCountDown is %.4f" %(numTrials,difficulty,t,globalClock.getTime(),trialClock.getTime(),trialCountDown.getTime())


   
  
win.close()
core.quit()
 