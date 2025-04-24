:orphan:

-------------------------------
MouseMonkeyComponent
-------------------------------

Monkey which clicks at a specific time and position


Categories:
    Monkeys (Simulated Responses)
Works in:
    PsychoPy

Parameters
-------------------------------

Basic
===============================

Name
    Name of this Component (alphanumeric or _, no spaces)

Start type
    How do you want to define your start point?
    
    Options:

    * time (s)
    * frame N
    * condition

Stop type
    How do you want to define your end point?
    
    Options:
    
    * duration (s)
    * duration (frames)
    * time (s)
    * frame N
    * condition

Start
    When does the Component start?

Stop
    When does the Component end? (blank is endless)

Expected start (s)
    (Optional) expected start (s), purely for representing in the timeline

Expected duration (s)
    (Optional) expected duration (s), purely for representing in the timeline

Component
    Component for this monkey to act on.

Data
===============================

Save onset/offset times
    Store the onset/offset times in the data file (as well as in the log file).

Sync timing with screen refresh
    Synchronize times with screen refresh (good for visual stimuli and responses based on them)

Testing
===============================

Disable Component
    Disable this Component

Action
===============================

Mouse button
    What mouse button to click?
    
    Options:
    * Left click
    * Middle (scroll) click
    * Right click

Click position [x,y]
    Where on screen to click?

Spatial units
    Units in which click position are specified
    
    Options:
    * from exp settings
    * deg
    * cm
    * pix
    * norm
    * height
    * degFlatPos
    * degFlat

Click mode
    Should this monkey click the mouse button at the start time, release at at the stop time, or do both?
    
    Options:
    * Click and release
    * Click only
    * Release only

