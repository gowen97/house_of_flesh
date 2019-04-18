"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass

class UniqueRoom(DefaultRoom):
    """
    using this to add unique description
    """
    # change locks so only the original creator can edit the room
    # change default description
    def at_object_creation(self):
        """
        called when object is first created
        """
        self.db.desc = "This is %s's room." (% self.caller)

    #when and how to message the player character to let them know about how to use their room?
