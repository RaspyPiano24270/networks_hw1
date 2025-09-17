import sys, termios, tty

class RawTerminal:
    def __init__(self, stream=sys.stdin):
        self.stream = stream
        self.fd = stream.fileno()
        self.old = None

    def __enter__(self):
        self.old = termios.tcgetattr(self.fd)
        tty.setraw(self.fd, when=termios.TCSANOW)
        return self
    
    def __exit__(self, exc_type, exc, tb):
        if self.old:
            termios.tcsetattr(self.fd, termios.TCSANOW, self.old)