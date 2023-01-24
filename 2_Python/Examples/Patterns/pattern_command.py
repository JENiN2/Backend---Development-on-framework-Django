class Light:
    def turn_on(self):
        print('Light is on')

    def turn_off(self):
        print('Light is off')


class CommandBase:
    def execute(self):
        raise NotImplementedError


class LightCommandBase(CommandBase):
    def __init__(self, light):
        self.light = light


class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()


class Switch:
    def __init__(self, cmd_on, cmd_off):
        self.cmd_on = cmd_on
        self.cmd_off = cmd_off

    def on(self):
        self.cmd_on.execute()

    def off(self):
        self.cmd_off.execute()


lamp = Light()
tumbler = Switch(cmd_on=TurnOnLightCommand(lamp), cmd_off=TurnOffLightCommand(lamp))

tumbler.on()
tumbler.off()
