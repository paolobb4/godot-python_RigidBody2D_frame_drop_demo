extends RigidBody2D

func _ready():
    linear_velocity = Vector2(500, 0)

func _process(delta):
    if position.x < 0:
        position.x = 0
        linear_velocity = Vector2(500, 0)
                                                     
    if position.x > get_viewport().size.x:
        position.x = get_viewport().size.x
        linear_velocity = Vector2(-500, 0)
