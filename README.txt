Dyslexia Behavioral and fMRI Task Code and Stimuli
Rita Barakat
November 27, 2019 

This repository contains the following files to execute the Orthographic and Phonological adaptive visual task paradigm for the purpose of behavioral and/ or neuroimaging studies of children with dyslexia and control subjects: 

1. behavioral_task folder: contains the following files, 

Conditions_Orthographic_beh.xlsx: contains the target/ foil word and pseudoword pairs for each image, width and height of the image as they will be displayed on an optimized computer screen, and the path to each image (*) 

Conditions_Phonologic_beh.xlsx: contains the target/ foil pseudoword pairs for each image, width and height of the image as they will be displayed on an optimized computer screen, and the path to each image (*)

DBP_Ortho.py: PsychoPy2 script to execute Orthographic task run, will automatically generate three files upon completion of the task run (a .xlsx file with subjects' responses, reaction time, and other pertinent task data; a .csv file containing the same information as the .xlsx file; and a .log file to track the PsychoPy script execution and stimulus timing). 

DBP_Ortho.pyc: Copy of Orthographic task PsychoPy2 script (for editing purposes). 

DBP_Phono.py: PsychoPy2 script to execute Phonological task run, will automatically generate three files upon completion of the task run (a .xlsx file with subjects' responses, reaction time, and other pertinent task data; a .csv file containing the same information as the .xlsx file; and a .log file to track the PsychoPy script execution and stimulus timing).

DBP_Phono.pyc: Copy of Phonological task PsychoPy2 script (for editing purposes). 

2. fMRI_task folder: contains the following files, 

Conditions_Orthographic_fMRI.xlsx: contains the target/ foil word and pseudoword pairs for each image, width and height of the image as they will be displayed on an optimized projector screen, and the path to each image (*) 

Conditions_Phonologic_fMRI.xlsx: contains the target/ foil pseudoword pairs for each image, width and height of the image as they will be displayed on an optimized projector screen, and the path to each image (*)

DYS_Ortho.py: PsychoPy2 script to execute Orthographic task run, will automatically generate three files upon completion of the task run (a .xlsx file with subjects' responses, reaction time, and other pertinent task data; a .csv file containing the same information as the .xlsx file; and a .log file to track the PsychoPy script execution and stimulus timing). 

DYS_Ortho.pyc: Copy of Orthographic task PsychoPy2 script (for editing purposes). 

DYS_Phono.py: PsychoPy2 script to execute Phonological task run, will automatically generate three files upon completion of the task run (a .xlsx file with subjects' responses, reaction time, and other pertinent task data; a .csv file containing the same information as the .xlsx file; and a .log file to track the PsychoPy script execution and stimulus timing).

DYS_Phono.pyc: Copy of Phonological task PsychoPy2 script (for editing purposes). 

3. images folder: contains all the images in varying file formats (*.gif, *.jpg, *.png, etc.) required for the behavioral- and fMRI-optimized task scripts. 

(*) IMPORTANT NOTE: All image paths in the Orthographic and Phonological "conditions" spreadsheets are currently set to the following: '/path/to/images/<image file>'. This must be adjusted according to the users' directory structure. 
