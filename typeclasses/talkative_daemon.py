"""
Evennia Talkative NPC
Contribution - Griatch 2011, grungies1138, 2016
This is a static NPC object capable of holding a simple menu-driven
conversation. It's just meant as an example. Create it by creating an
object of typeclass contrib.talking_npc.TalkingNPC, For example using
@create:
    @create/drop John : contrib.talking_npc.TalkingNPC
Walk up to it and give the talk command to strike up a conversation.
If there are many talkative npcs in the same room you will get to
choose which one's talk command to call (Evennia handles this
automatically). This use of EvMenu is very simplistic; See EvMenu for
a lot more complex possibilities.
"""

#MODIFIED by grace as of 3 march 2019
#will this actually work?
#contrib menu nodes seem to be tripping things up

from evennia import DefaultObject, CmdSet, default_cmds
from evennia.utils.evmenu import EvMenu
from evennia.commands.command import Command


# Menu implementing the dialogue tree

def start_node(caller): #originally menu_start_node currently throwing an error
    text = "The server daemon blinks their rheumy eyes at you. They grumble something that could be a greeting."

    options = ({"desc": "Where am I?",
                "goto": "info1"},
               {"desc": "Who are you?",
                "goto": "info2"})

    return text, options


def info1(caller):
    text = "'This is the debug room. This is where it begins.'"

    options = ({"desc": "What does that even mean?",
                "goto": "info3"},
               {"desc": "Ok, who are you?",
                "goto": "info2"},
               {"desc": "I'm not interested.",
                "goto": "END"})

    return text, options


def info2(caller):
    text = "'Well, I live here, and I tell travelers on their way through how they can spend their time here.'"

    options = ({"desc": "So what am I supposed to do?",
                "goto": "info3"},
               {"desc": "This is boring.",
                "goto": "END"})

    return text, options


def info3(caller):
    text = "'Now that you've named yourself, you've generated a space for yourself. You can go to it by typing HOME.'"

    options = ({"desc": "What am I supposed to do there?",
                "goto": "info4"},
               {"desc": "Ok, I'm ready to go.",
                "goto": "END"})

    return text, options

def info4(caller):
    text = "'Inside your space, you can arrange symbols to suggest a fantasy of yours. That's all I can tell you for now.'"

    options = ({"desc": "Can you repeat that?",
                "goto": "info1"},
               {"desc": "That's vague but ok!",
                "goto": "END"})

    return text, options


def END(caller):
    text = "'Goodbye, then.'"

    options = ()

    return text, options

#
# The talk command (sits on the NPC)
#


class CmdTalk(default_cmds.MuxCommand):
    """
   Talks to an npc
   Usage:
     talk
   This command is only available if a talkative non-player-character
   (NPC) is actually present. It will strike up a conversation with
   that NPC and give you options on what to talk about.
   """
    key = "talk"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        "Implements the command."

        # self.obj is the NPC this is defined on
        self.caller.msg("(You walk up and talk to %s.)" % self.obj.key)

        # Initiate the menu. Change this if you are putting this on
        # some other custom NPC class.
        EvMenu(self.caller, "typeclasses.talkative_daemon",
               startnode="start_node", cmd_on_exit="@dig a room for %s : typeclasses.rooms.UniqueRoom = to a room for %s,to debug room" % (self.caller, self.caller))


class TalkingCmdSet(CmdSet):
    "Stores the talk command."
    key = "talkingcmdset"

    def at_cmdset_creation(self):
        "populates the cmdset"
        self.add(CmdTalk())


class TalkingDaemon(DefaultObject):
    """
    This implements a simple Object using the talk command and using
    the conversation defined above.
    """

    def at_object_creation(self):
        "This is called when object is first created."
        self.db.desc = "On closer inspection you see that their feet are bolted into the formless black ground. A single massive nail was driven through each foot; now the nails are rusted and there is a black crust around the old wound like the blood was never cleaned off.."
        # assign the talk command to npc
        self.cmdset.add_default(TalkingCmdSet, permanent=True)
