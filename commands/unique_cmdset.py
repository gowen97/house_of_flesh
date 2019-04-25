from evennia import default_cmds
# from command import CmdUnloggedinLook
# from evennia.contrib.menu_login import CmdUnloggedinLook
# from evennia.contrib.menu_login import UnloggedinCmdSet
from command import CmdTestMenuNote
from command import CmdMore
from evennia.commands.default.building import CmdSpawn
#from command import default_cmdsets
from default_cmdsets import CharacterCmdSet
#from commands import CmdSpawn


class UniqueCmdSet(default_cmds.CharacterCmdSet):
    key = "UniqueCmdSet"

    def at_cmdset_creation(self):
        #super(CharacterCmdSet, self).at_cmdset_creation()
        self.add(CmdSpawn()) #or building.CmdSpawn if that doesn't work
