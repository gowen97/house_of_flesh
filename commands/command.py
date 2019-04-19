"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia import Command as BaseCommand
from evennia import default_cmds
from evennia import syscmdkeys
from evennia.contrib.menu_login import CmdUnloggedinLook
from evennia.utils.evmenu import EvMenu


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

# class CmdCreateUniqueRoom(Command):
#     """
#     Create the players unique room
#     """
#         caller = self.caller
#         key = "unique"
#
#         # if not self.lhs:
#         #     string = "Usage: @dig[/teleport] <roomname>[;alias;alias...]" \
#         #              "[:parent] [= <exit_there>"
#         #     string += "[;alias;alias..][:parent]] "
#         #     string += "[, <exit_back_here>[;alias;alias..][:parent]]"
#         #     caller.msg(string)
#         #     return
#         #
#         # room = self.lhs_objs[0]
#         #
#         # if not room["name"]:
#         #     caller.msg("You must supply a new room name.")
#         #     return
#         # location = caller.location
#
#         # Create the new room
#         # typeclass = room['option']
#         # if not typeclass:
#         typeclass = settings.BASE_ROOM_TYPECLASS
#
#         # create room
#         new_room = create.create_object(typeclass, room[caller + "'s room'"], #???
#                                         report_to=caller)
#         lockstring = "edit:none()"
#         new_room.locks.add(lockstring)
#         # alias_string = ""
#         # if new_room.aliases.all():
#         #     alias_string = " (%s)" % ", ".join(new_room.aliases.all())
#         room_string = "Created %s room for %s." % (
#                 new_room, caller)
#
#         # create exit to room
#
#         exit_to_string = ""
#         exit_back_string = ""
#
#         if self.rhs_objs:
#             to_exit = self.rhs_objs[0]
#             if not to_exit["name"]:
#                 exit_to_string = "\nNo exit created to new room."
#             elif not location:
#                 exit_to_string = "\nYou cannot create an exit from a None-location."
#             else:
#                 # Build the exit to the new room from the current one
#                 typeclass = to_exit["option"]
#                 if not typeclass:
#                     typeclass = settings.BASE_EXIT_TYPECLASS
#
#                 new_to_exit = create.create_object(typeclass, to_exit["name"],
#                                                    location,
#                                                    aliases=to_exit["aliases"],
#                                                    locks=lockstring,
#                                                    destination=new_room,
#                                                    report_to=caller)
#                 alias_string = ""
#                 if new_to_exit.aliases.all():
#                     alias_string = " (%s)" % ", ".join(new_to_exit.aliases.all())
#                 exit_to_string = "\nCreated Exit from %s to %s: %s(%s)%s."
#                 exit_to_string = exit_to_string % (location.name,
#                                                    new_room.name,
#                                                    new_to_exit,
#                                                    new_to_exit.dbref,
#                                                    alias_string)
#
#         # Create exit back from new room
#
#         if len(self.rhs_objs) > 1:
#             # Building the exit back to the current room
#             back_exit = self.rhs_objs[1]
#             if not back_exit["name"]:
#                 exit_back_string = "\nNo back exit created."
#             elif not location:
#                 exit_back_string = "\nYou cannot create an exit back to a None-location."
#             else:
#                 typeclass = back_exit["option"]
#                 if not typeclass:
#                     typeclass = settings.BASE_EXIT_TYPECLASS
#                 new_back_exit = create.create_object(typeclass,
#                                                      back_exit["name"],
#                                                      new_room,
#                                                      aliases=back_exit["aliases"],
#                                                      locks=lockstring,
#                                                      destination=location,
#                                                      report_to=caller)
#                 alias_string = ""
#                 if new_back_exit.aliases.all():
#                     alias_string = " (%s)" % ", ".join(new_back_exit.aliases.all())
#                 exit_back_string = "\nCreated Exit back from %s to %s: %s(%s)%s."
#                 exit_back_string = exit_back_string % (new_room.name,
#                                                        location.name,
#                                                        new_back_exit,
#                                                        new_back_exit.dbref,
#                                                        alias_string)
#         caller.msg("%s%s%s" % (room_string, exit_to_string, exit_back_string))
#trying to get menu_login contrib to work
class CmdUnloggedinLook(Command):
    """
    An unloggedin version of the look command. This is called by the server
    when the account first connects. It sets up the menu before handing off
    to the menu's own look command.
    """
    key = syscmdkeys.CMD_LOGINSTART
    locks = "cmd:all()"
    arg_regex = r"^$"

    def func(self):
        "Execute the menu"
        EvMenu(self.caller, "evennia.contrib.menu_login",
               startnode="start", auto_look=False, auto_quit=False,
               cmd_on_exit=None, node_formatter=_formatter)

class CmdTestMenuNote(Command):
    key = "note"

    def func(self):
        # Here we look in the file mymenu.py for the function "node_set_note_name". And yes, we have to pass "self.caller" as the first argument, the tutorial isn't clear on that point.
        EvMenu(self.caller, "world.mymenu", startnode="node_set_note_name")



# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super(MuxCommand, self).has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None
