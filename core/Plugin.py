"""
    Class Name : Plugin

    Description:
        Superclass for which all plugins are derived
        Handles thread-level exception publishing

    Contributors:
        - Patrick Hennessy

    License:
        PhilBot is free software: you can redistribute it and/or modify it
        under the terms of the GNU General Public License v3; as published
        by the Free Software Foundation
"""

import threading
import sys

class Plugin(threading.Thread):
    def __init__(self, core, name="GenericPlugin"):
        super(Plugin, self).__init__(name=name)
        self.core = core

    def run(self):
        try:
            self.startThread()
        except:
            self.core.publish("plugin.exception", thread=self.name, exception=sys.exc_info())

    def startThread(self):
        pass
