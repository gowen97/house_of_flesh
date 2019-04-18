"""
Prototypes

A prototype is a simple way to create individualized instances of a
given `Typeclass`. For example, you might have a Sword typeclass that
implements everything a Sword would need to do. The only difference
between different individual Swords would be their key, description
and some Attributes. The Prototype system allows to create a range of
such Swords with only minor variations. Prototypes can also inherit
and combine together to form entire hierarchies (such as giving all
Sabres and all Broadswords some common properties). Note that bigger
variations, such as custom commands or functionality belong in a
hierarchy of typeclasses instead.

Example prototypes are read by the `@spawn` command but is also easily
available to use from code via `evennia.spawn` or `evennia.utils.spawner`.
Each prototype should be a dictionary. Use the same name as the
variable to refer to other prototypes.

Possible keywords are:
    prototype - string pointing to parent prototype of this structure.
    key - string, the main object identifier.
    typeclass - string, if not set, will use `settings.BASE_OBJECT_TYPECLASS`.
    location - this should be a valid object or #dbref.
    home - valid object or #dbref.
    destination - only valid for exits (object or dbref).

    permissions - string or list of permission strings.
    locks - a lock-string.
    aliases - string or list of strings.

    ndb_<name> - value of a nattribute (the "ndb_" part is ignored).
    any other keywords are interpreted as Attributes and their values.

See the `@spawn` command and `evennia.utils.spawner` for more info.

"""

#from random import randint
#
# GOBLIN = {
# "key": "goblin grunt",
# "health": lambda: randint(20,30),
# "resists": ["cold", "poison"],
# "attacks": ["fists"],
# "weaknesses": ["fire", "light"]
# }
#
# GOBLIN_WIZARD = {
# "prototype": "GOBLIN",
# "key": "goblin wizard",
# "spells": ["fire ball", "lighting bolt"]
# }
#
# GOBLIN_ARCHER = {
# "prototype": "GOBLIN",
# "key": "goblin archer",
# "attacks": ["short bow"]
#}
#
# This is an example of a prototype without a prototype
# (nor key) of its own, so it should normally only be
# used as a mix-in, as in the example of the goblin
# archwizard below.
# ARCHWIZARD_MIXIN = {
# "attacks": ["archwizard staff"],
# "spells": ["greater fire ball", "greater lighting"]
#}
#
# GOBLIN_ARCHWIZARD = {
# "key": "goblin archwizard",
# "prototype" : ("GOBLIN_WIZARD", "ARCHWIZARD_MIXIN")
#}

#LIGHTS HERE
#add permissions, aliases, and locks!
NEON = {
    "prototype_key": "neon",
    "key": "neon light",
    "strength": 5,
    "typeclass": "typeclasses.objects.Light",
    "desc": "Bright red neon in a tube.",
    #"locks": "edit:Players" #not sure if this is right syntax
}

CANDLES = {
    "prototype_key": "candles",
    "key": "flickering candles",
    "strength": 1,
    "typeclass": "typeclasses.objects.Light",
    "desc": "Small tea lights."
}

LIGHTBULB = {
    "prototype_key": "lightbulb",
    "key": "a bare lightbulb",
    "strength": 4,
    "typeclass": "typeclasses.objects.Light",
    "desc": "Bare white light bulb."
}

LAMP = {
    "prototype_key": "lamp",
    "key": "a lamp",
    "strength": 5,
    "typeclass": "typeclasses.objects.Light",
    "desc": "A lamp with a red shade."
}

STARLIGHT = {
    "prototype_key": "starlight",
    "key": "light from the stars",
    "strength": 1,
    "typeclass": "typeclasses.objects.Light",
    "desc": "Faint twinkling of stars far away."
}

FLUORESCENTS = {
    "prototype_key": "fluorescents",
    "key": "a fluorescent light",
    "strength": 5,
    "typeclass": "typeclasses.objects.Light",
    "desc": "A yellowy white fluorescent light in a panel."
}

BLACKLIGHT = {
    "prototype_key": "blacklight",
    "key": "a blacklight",
    "strength": 2,
    "typeclass": "typeclasses.objects.Light",
    "desc": "A purply blacklight."
}

FLASHLIGHT = {
    "prototype_key": "flashlight",
    "key": "a flashlight",
    "strength": 2,
    "typeclass": "typeclasses.objects.Light",
    "desc": "A sturdy flashlight."
}

#WEAPONS here
#add permissions, aliases, and locks!
DAGGER = {
    "prototye_key": "dagger",
    "key": "a dagger",
    "typeclass": "typeclasses.objects.Weapon",
    "desc": "Thick, short dagger with a leather handle."
}

GUN = {
    "prototype_key": "gun",
    "key": "a gun",
    "typeclass": "typeclasses.objects.Weapon",
    "desc": "A semiautomatic with the safety on."
}

KNIFE = {
    "prototype_key": "knife",
    "key": "a knife",
    "typeclass": "typeclasses.objects.Weapon",
    "desc": "A thick kitchen knife."
}

BASEBALL_BAT = {
    "prototype_key": "bat",
    "key": "a baseball bat",
    "typeclass": "typeclasses.objects.Weapon",
    "desc": "A wooden baseball bat."
}

#where do i find more examples of weapons used in erotic contexts

#MEDIA
#add permissions, aliases, and locks
BOOK = {
    "prototype_key": "book",
    "key": "a book",
    "typeclass": "typeclasses.objects.Media",
    "desc": "A leather-bound novel."
}

MAGAZINE = {
    "prototype_key": "magazine",
    "key": "a magazine",
    "typeclass": "typeclasses.objects.Media",
    "desc": "A glossy magazine."
}

NEWSPAPER = {
    "prototype_key": "newspaper",
    "key": "a newspaper",
    "typeclass": "typeclasses.objects.Media",
    "desc": "A slightly soggy paper."
}

TELEVISION = {
    "prototype_key": "television",
    "key": "a TV set",
    "typeclass": "typeclasses.objects.Media",
    "desc": "A rabbit-eared TV set."
}

LAPTOP = {
    "prototype_key": "laptop",
    "key": "a laptop",
    "typeclass": "typeclasses.objects.Media",
    "desc": "A black laptop with a charger."
}

VIDEO_GAME_CONSOLE = {
    "prototype_key": "videogame",
    "key": "a video game console",
    "typeclass": "typeclasses.objects.Media",
    "desc": "An old, dusty console with a scratched-up cartridge in it."
}

RADIO = {
    "prototype_key": "radio",
    "key": "a radio",
    "typeclass": "typeclasses.objects.Media",
    "desc": "An old radio with a big antenna."
}

FILM_PROJECTOR = {
    "prototype_key": "projector",
    "key": "a projector",
    "typeclass": "typeclasses.objects.Media",
    "desc": "A film projector that makes a loud whirring noise."
}

PHONE = {
    "prototype_key": "phone",
    "key": "a cell phone",
    "typeclass": "typeclasses.objects.Media",
    "desc": "An old black battered flip phone."
}

#Furniture

DIVAN = {
    "prototype_key": "divan",
    "key": "a fainting couch",
    "typeclass": "typeclasses.objects.Furniture",
    "desc": "A richly upholstered seat."
}

TABLE = {
    "prototype_key": "table",
    "key": "a table",
    "typeclass": "typeclasses.objects.Furniture",
    "desc": "A plain wooden table with four legs."
}

BED = {
    "prototype_key": "bed",
    "key": "a bed",
    "typeclass": "typeclasses.objects.Furniture",
    "desc": "A plain bed with white sheets."
}

#Misc

CIGARETTES = {
    "prototype_key": "cigarettes",
    "key": "a pack of cigarettes",
    "typeclass": "typeclasses.objects.Misc",
    "desc": "A rumpled silvery pack with a few cigarettes missing."
}

WINE = {
    "prototype_key": "wine",
    "key": "a bottle of wine",
    "typeclass": "typeclasses.objects.Misc",
    "desc": "An opened bottle of red wine."
}

WEED = {
    "prototype_key": "weed",
    "key": "a joint",
    "typeclass": "typeclasses.objects.Misc",
    "desc": "An inexpertly rolled joint."
}

HANDCUFFS = {
    "prototype_key": "cigarettes",
    "key": "a pack of cigarettes",
    "typeclass": "typeclasses.objects.Misc",
    "desc": "A rumpled silvery pack with a few cigarettes missing."
}
