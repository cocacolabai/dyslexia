#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.04), Tue Jun  3 21:55:22 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'DBP'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = u'Beh_data' + os.path.sep + '%s_%s_%s' %(expInfo['participant'],'Phono', expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text=u'Choose the side (left or right) with the word that is spelled correctly.\r\nPress any button to continue.\r\n',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
imgStimulus = visual.ImageStim(win=win, name='imgStimulus',
    image='sin', mask=None,
    ori=0, pos=[0, 100], size=[500, 500], units='pix',
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
combinedWords = visual.TextStim(win=win, ori=0, name='combinedWords',
    text='default text',    font='Arial',
    pos=[0, -0.45], height=0.15, wrapWidth=5000,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
correct = 0
difficulty = 3
numTrials = 50

#SCcode - set counting variables for beginning of experiment
streakCorr = 0
maxTrials = 60
numTrials = 0
numCorr = 0

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedbackText = visual.TextStim(win=win, ori=0, name='feedbackText',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color=u'green', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "EndofExpFeedback"
EndofExpFeedbackClock = core.Clock()
endText = visual.TextStim(win=win, ori=0, name='endText',
    text=u'END\n\nSCORE: 00/00',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instrText)
instructionsComponents.append(key_resp_2)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
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

#SCcode - set initial difficulty
difficulty = 3

for thisTrialLoop in trialLoop:
    currentLoop = trialLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop.keys():
            exec(paramName + '= thisTrialLoop.' + paramName)
    
    # SCcode - set the arrays
    imgArray = [imgfile1, imgfile2, imgfile3, imgfile4, imgfile5]
    combinedTextArray = [text1, text2, text3, text4, text5]
    widthArray = [w1, w2, w3, w4, w5]
    heightArray = [h1, h2, h3, h4, h5]
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(6.500000)
    # SCcode - update component parameters for each repeat
    imgStimulus.setImage(imgArray[difficulty - 1])
    combinedWords.setText(combinedTextArray[difficulty - 1])
    #bottomword.setText(bottomTextArray[difficulty - 1])
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    
    # keep track of which components have finished
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
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imgStimulus* updates
        if t >= 0.5 and imgStimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            imgStimulus.tStart = t  # underestimates by a little under one frame
            imgStimulus.frameNStart = frameN  # exact frame index
            imgStimulus.setAutoDraw(True)
        elif imgStimulus.status == STARTED and t >= (0.5 + (6.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            imgStimulus.setAutoDraw(False)
        if imgStimulus.status == STARTED:  # only update if being drawn
            #imgStimulus.setSize([500,500], log=False)
            imgStimulus.setSize([widthArray[difficulty - 1], heightArray[difficulty - 1]], log=False)

        # *combinedWords* updates
        if t >= 0.5 and combinedWords.status == NOT_STARTED:
            # keep track of start time/frame for later
            combinedWords.tStart = t  # underestimates by a little under one frame
            combinedWords.frameNStart = frameN  # exact frame index
            combinedWords.setAutoDraw(True)
        elif combinedWords.status == STARTED and t >= (0.5 + (6.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            combinedWords.setAutoDraw(False)
            
        # *response* updates
        if t >= 0.5 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif response.status == STARTED and t >= (0.5 + (6.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # was this 'correct'?
                if (response.keys == str(corrAns)) or (response.keys == corrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
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
    
    numTrials = numTrials + 1
    
    #SCcode - check difficulty
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
            
    if response.keys != None:  # we had a response
        trialLoop.addData('response.rt', response.rt)
    
    
    #------Prepare to start Routine "feedback"-------
    #t = 0
    feedbackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(6.500000-t)
    
    if response.corr == 1:
        feedbackText.setText(u'+')
        feedbackText.setSize(0.3)
        feedbackText.setColor(u'white')
    else:
        feedbackText.setText(u'+')
        feedbackText.setSize(0.3)
        feedbackText.setColor(u'white')
        
    # update component parameters for each repeat
    # keep track of which components have finished
    feedbackComponents = []
    feedbackComponents.append(feedbackText)
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "feedback"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackText* updates
        if t >= 0.5 and feedbackText.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackText.tStart = t  # underestimates by a little under one frame
            feedbackText.frameNStart = frameN  # exact frame index
            feedbackText.setAutoDraw(True)
        elif feedbackText.status == STARTED and t >= (0.5 + (6.0-win.monitorFramePeriod*0.75)-t): #most of one frame period left
            feedbackText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialLoop'


#------Prepare to start Routine "EndofExpFeedback"-------
t = 0
EndofExpFeedbackClock.reset()  # clock 
frameN = -1

endText.setText(u'Congratulations! You completed the round. Press any button to exit.')
# update component parameters for each repeat
endExperimentKeystroke = event.BuilderKeyResponse()  # create an object of type KeyResponse
endExperimentKeystroke.status = NOT_STARTED
# keep track of which components have finished
EndofExpFeedbackComponents = []
EndofExpFeedbackComponents.append(endText)
EndofExpFeedbackComponents.append(endExperimentKeystroke)
for thisComponent in EndofExpFeedbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "EndofExpFeedback"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = EndofExpFeedbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if t >= 0.5 and endText.status == NOT_STARTED:
        # keep track of start time/frame for later
        endText.tStart = t  # underestimates by a little under one frame
        endText.frameNStart = frameN  # exact frame index
        endText.setAutoDraw(True)
    
    # *endExperimentKeystroke* updates
    if t >= 0.5 and endExperimentKeystroke.status == NOT_STARTED:
        # keep track of start time/frame for later
        endExperimentKeystroke.tStart = t  # underestimates by a little under one frame
        endExperimentKeystroke.frameNStart = frameN  # exact frame index
        endExperimentKeystroke.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if endExperimentKeystroke.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndofExpFeedbackComponents:
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

#-------Ending Routine "EndofExpFeedback"-------
for thisComponent in EndofExpFeedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
