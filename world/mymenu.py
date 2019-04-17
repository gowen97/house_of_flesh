# Grace: This is needed to create arbitrary objects
from evennia import create_object

# To access this menu, use the command "testmenu"
# TO DO as of 03.01: create an actual option for no;
# most urgently, change the way the note shows up in "look" to read: "a note titled 'x'"
# or something similar?
# what's the best way to phrase that?

def node_set_note_name(caller):
    text = "Enter the note name: "
    # The import thing below is to not put the value for "goto" in quotes, like some of the tutorials have. This should just be the name of the function that one goes to when one enters the note name, in this example.
    options = {"key": "_default",
            "goto": _set_note_name}

    return text, options

def _set_note_name(caller, raw_string, **kwargs):
    # See https://github.com/evennia/evennia/wiki/EvMenu#example-storing-data-between-nodes for more info about what I'm doing here.
    caller.ndb._menutree.notedata = {}
    caller.ndb._menutree.notedata["name"] = raw_string.strip()
    caller.msg("You set the title of the note to \"{}\"".format(raw_string.strip()))
    # This, for some reason, *does* need to be in quotes! It's the name of the menu node, the function that will take the next thing to do.
    return "node_set_note_content"

def node_set_note_content(caller):
    text = "Enter the note's content: "
    options = {"key": "_default",
            "goto": _set_note_content}

    return text, options


def _set_note_content(caller, raw_string, **kwargs):
    caller.ndb._menutree.notedata["content"] = raw_string.strip()
    caller.msg("You set the note content to \"{}\"".format(raw_string.strip()))
    return "node_view_note"

# This views the note before it's saved. I haven't tested the "no" version too much. Ideally it should just discard the note, probably.
def node_view_note(caller, raw_string, **kwargs):
    name = caller.ndb._menutree.notedata["name"]
    content = caller.ndb._menutree.notedata["content"]

    text = "Do you want to create the note below?\n\nName: %s\n\n%s" % (name, content)
    options = ({"key": ("Yes", "yes", "y"),
        "goto": "create_note"},
        {"key": ("No", "no", "n"),
            "goto": "node3"}) #change no to just exit out

    return text, options

def node3(caller): #this ends the menu since there are no options
    text = "You crumple up the piece of paper in your fist and throw it away."
    return text, None

# This actually creates the note
def create_note(caller, raw_string, **kwargs):
    # Get the name and content from the _menutree we saved above
    name = caller.ndb._menutree.notedata["name"]
    content = caller.ndb._menutree.notedata["content"]

    # Use the create_object method to make a new object and save it to this room.
    new_object = create_object("typeclasses.note.NoteObject", key="a note titled " + name, location=caller.location)
    # Update the content property of the object db with our content.
    new_object.db.content = content

    # This saves the creator, not sure how to not have the object number in parentheses also saved, that could probably be removed relatively easily.
    new_object.db.creator = caller.get_display_name(caller)

    # Let user know we created the note
    caller.msg("Created your note %s" % name)

    # Exit out of this menu tree
    return None
