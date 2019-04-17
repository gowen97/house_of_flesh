# Grace: this object allows one to create notes with timestamps on them
#code from Adriana 2/27/19

import time
from typeclasses.objects import Object

class NoteObject(Object):
    """
    A note with a name, subject, and datetime
    """
    def at_object_creation(self):
        # Save the time that the note was created.
        current_time = round(time.time())
        self.db.timestamp = current_time
        self.db.content = ""
        self.db.creator = ""

    def return_appearance(self, caller):
        """
        Called by the look command. Format the note properly as needed
        """
        # first get the base string from the
        # parent's return_appearance.
        # This gives us the note "name"
        string = super(NoteObject, self).return_appearance(caller)

        #caller.msg(caller.get_display_name(caller))

        # Then, format this with the note content (which was saved when we finished the menu tree) and the note time.
        string = string + "\n\n%s\n\nThis note was created on %s by %s." % (self.db.content, time.strftime("%A, %d %B %Y at %H:%M", time.localtime(self.db.timestamp)), self.db.creator)
        return string
