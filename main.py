from godot import exposed
from godot.bindings import *


@exposed
class main(Node):
    def _ready(self):
        for i in range(self.get_child_count()):
            self.get_child(i).linear_velocity = Vector2(500, 0)

    def _process(self, delta):
        for i in range(self.get_child_count()):
            rb = self.get_child(i)

            if rb.position.x < 0:
                rb.position.x = 0
                rb.linear_velocity = Vector2(500, 0)

            if rb.position.x > self.get_viewport().size.x:
                rb.position.x = self.get_viewport().size.x
                rb.linear_velocity = Vector2(-500, 0)
