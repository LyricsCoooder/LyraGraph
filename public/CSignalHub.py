from .CSignal import CSignal

class CSignalHub:
    def __init__(self):
        self._dctSignals = {}
    
    def Get(self, sSignalName):
        if sSignalName not in self._dctSignals:
            self._dctSignals[sSignalName] = CSignal()
        return self._dctSignals[sSignalName]
