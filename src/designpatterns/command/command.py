#command.py

class Command:
    def execute(self):
        pass

class Tv:
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
    def get_on(self):
        return self.on

class Remote:
    def set_command(self, command):
        self.command = command

    def press_power_button(self):
        self.command.execute()

class TvOffCommand(Command):
    def __init__(self, Tv):
        self.Tv = Tv
    def execute(self):
        self.Tv.turn_off()

class TvOnCommand(Command):
    def __init__(self, Tv):
        self.Tv = Tv
    def execute(self):
        self.Tv.turn_on()
