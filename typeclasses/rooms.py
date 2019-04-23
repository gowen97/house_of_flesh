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

class DebugRoom(DefaultRoom):
    """
    using this to message about more
    """
    def at_object_receive(self, new_arrival, source_location):
        self.caller.execute_cmd("more")
        #hopefully this works? TODO test me when moving over tmrw

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
        #self.db.desc = "This is %s's room. It represents a dream, a fantasy." (% self.caller)
    def at_object_receive(self, new_arrival, source_location):
        """
        When an object enter a tutorial room we tell other objects in
        the room about it by trying to call a hook on them. The Mob object
        uses this to cheaply get notified of enemies without having
        to constantly scan for them.
        Args:
            new_arrival (Object): the object that just entered this room.
            source_location (Object): the previous location of new_arrival.
        """
        if new_arrival.has_account: #and not new_arrival.is_superuser:
            # this is a character
            # new arrival allows us to message the account in the room as it arrives
            # TODO make this message only show up to the person who created the room
            # check if name matches name in room
            new_arrival.msg("|b Welcome to your room. Type @SPAWN to place objects in the room to represent a fantasy of yours.")
            new_arrival.msg("|b What kind of fantasy? A sex dream, a desire, some kind of need or yearning.")
            new_arrival.msg("|b What is lurking inside your entrails? Gesture to it here. No need to be explicit. Suggest it.")

    #when and how to message the player character to let them know about how to use their room?
