This project demonstrates that having several instances of RigidBody2D in movement (through the property *RigidBody2D.linear_velocity*) that have a script assigned causes the frame rate to drop drastically.
The same is not true if they are assigned a gdscript instead or if no script is asigned but instead the main object that instansciates them is the only one to have a script. This makes me think that it has to do with the script being instantiated many times yet this only is a problem if the objects are in movement, no frame drop is present if the objects are inmobile.

godot-python is required to run this project. Remember to compile and add it to the project folder.


**main.py**: manually manages it's children objects wich are instances of *RB2D.tscn* (already assigned to *Main.tscn*).
**rb2d-empty.py**: defining a class that does nothing (already assigned to *RB2D.tscn*).
**rb2d.py**: manages itself, assigne to *RB2D.tscn* and disable *Main.tscn*'s script to test.
**rb2d.gd**: manages itself, assigne to *RB2D.tscn* and disable *Main.tscn*'s script to test.
