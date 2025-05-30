:orphan:

-------------------------------
SliderMonkeyComponent
-------------------------------

Monkey which makes a Slider response


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

Slider response
    What value to choose on the Slider?

