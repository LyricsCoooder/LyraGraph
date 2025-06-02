from . import Defs
from . import CSignalHub

g_oSignalHub = None
def GetSignalHub() -> CSignalHub.CSignalHub:
    global g_oSignalHub
    if not g_oSignalHub:
        g_oSignalHub = CSignalHub.CSignalHub()
    return g_oSignalHub