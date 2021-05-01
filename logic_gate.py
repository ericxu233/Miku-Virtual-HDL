all_gates = []


#This is the file that contains the core objects for the representation of logic gates
class logicGate:
    def __init__(self, typev, name):
        self.gateType = typev
        self.gateName = name
        self.output = None
        self.next_gate = " "
        self.input = []

        all_gates[name] = self
    
    def add_input(wire):
        input.insert(len(input), wire)



class orGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result():
        output = False
        for x in input:
            output = output or x


    
class andGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result():
        output = True
        for x in input:
            output = output and x


class notGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result():
        output = not input[0]


class norGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result():
        output = False
        for x in input:
            output = output or x
        ouput = not ouput


class nandGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result():
        output = True
        for x in input:
            output = output and x
        output = not output


