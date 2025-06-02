import weakref
import types

class CSignal:
    def __init__(self):
        self._lstSubscribers = []

    def Connect(self, callback):
        if isinstance(callback, types.MethodType):
            ref = weakref.WeakMethod(callback)
        else:
            ref = weakref.ref(callback)
        self._lstSubscribers.append(ref) 
    
    def disconnect(self, callback):
        self._lstSubscribers = [ref for ref in self._lstSubscribers if ref() is not callback]

    def emit(self, *args, **kwargs):
        dead = []
        for ref in self._lstSubscribers:
            func = ref()
            if func is not None:
                func(*args, **kwargs)
            else:
                dead.append(ref)
        for ref in dead:
            self._lstSubscribers.remove(ref)