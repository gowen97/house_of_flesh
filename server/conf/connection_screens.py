# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets. UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""
#edited gowen 12 april
from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|b==============================================================|n
 Welcome to |g{}|n.

Please type "connect" to generate a new name and enter the house of flesh.
If you are a moderator, please use oldconnect to log in to your account.

 Enter |whelp|n for more info. |wlook|n will re-show this screen.
|b==============================================================|n""" \
    .format(settings.SERVERNAME)
