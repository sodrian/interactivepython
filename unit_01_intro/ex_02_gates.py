class LogicGate(object):
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def perform_gate_logic(self):
        raise NotImplementedError

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryLogicGate(LogicGate):
    def __init__(self, label):
        super(BinaryLogicGate, self).__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        inp = input('Get pin A: ')
        return bool(int(inp))

    def get_pin_b(self):
        inp = input('Get pin B: ')
        return bool(int(inp))


class UnaryLogicGate(LogicGate):
    def __init__(self, label):
        super(UnaryLogicGate, self).__init__(label)
        self.pin = None


class AndLogicGate(BinaryLogicGate):
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        return a and b
