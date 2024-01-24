from datetime import datetime
class Logger:
    def __init__(self, filename = f"./logs/{datetime.now().isoformat()}"):
        if filename is not None:
            self.filename = filename
            f = open(filename, "w")
            f.close()

    def debug(self, message, end="\n"):
        f = open(self.filename, "a")
        f.write(message + end)
        f.close()
