from threading import Timer,Thread,Event

class PerpetualTimer():
    def __init__(self, t, h_function, h_ref):
        self.t = t
        self.h_function = h_function
        self.h_ref = h_ref
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.h_function(self.h_ref)
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()