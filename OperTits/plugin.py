###
# Copyright (c) 2017, Connor Angell
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('OperTits')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class OperTits(callbacks.Plugin):
    """Server Admin tools"""
    threaded = True


Class = OperTits


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
