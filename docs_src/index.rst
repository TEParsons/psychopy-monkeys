=======================================================
Welcome to psychopy-monkeys's documentation!
=======================================================

The `psychopy-monkeys` plugin adds Components to Builder which emulate participant responses (I 
call them monkeys), but only when running in pilot mode. This is intended to save you time and 
effort when building and debugging your experiment, as you can let the monkeys do the button 
pressing and mouse clicking for you while you're in pilot mode, then switch to running mode when 
you're testing on an actual participant.

The following monkeys are added:

.. grid:: 1 2 3 4

   .. grid-item-card:: Routine Ender Monkey
      :link: components/RoutineEnderMonkeyComponent
      :img-top: static/enderMonkey.svg

      Ends the Routine at a specific time

   .. grid-item-card:: Keyboard Monkey
      :link: components/KeyboardMonkeyComponent
      :img-top: static/keyboardMonkey.svg

      Presses a key at a specific time
   
   .. grid-item-card:: Mouse Monkey
      :link: components/MouseMonkeyComponent
      :img-top: static/mouseMonkey.svg

      Clicks at a specific time and position
   
   .. grid-item-card:: Slider Monkey
      :link: components/SliderMonkeyComponent
      :img-top: static/sliderMonkey.svg

      Makes a Slider response at a specific time with a specific value
