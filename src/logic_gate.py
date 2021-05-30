import sys
all_gates = dict()


#This is the file that contains the core objects for the representation of logic gates
class logicGate:
    def __init__(self, typev, name):
        self.gateType = typev
        self.gateName = name
        self.output = None
        self.next_gate = " "
        self.input = []

        #control flow of logic gate
        self.connection_wires = []
        self.complete_connections = []
        self.complete = False

        all_gates[name] = self
    
    def add_input(self, signal):
        self.input.insert(len(self.input), signal)
    
    def add_wire(self, wire):
        self.connection_wires.insert(len(self.connection_wires), wire)

    #verify if all wires have produced an output
    def verify_complete(self):
        complete = not self.connection_wires
        return complete
    
    #complete a wire connection, note: does not handle the inputed signal (will be handled by trace_output())
    def wire_complete(self, wire):
        self.connection_wires.remove(wire)
        self.complete_connections.insert(len(self.complete_connections), wire)
    

        



class orGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result(self):
        output = False
        for x in self.input:
            output = output or x


    
class andGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result(self):
        output = True
        for x in self.input:
            output = output and x


class notGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result(self):
        output = not self.input[0]


class norGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result(self):
        output = False
        for x in self.input:
            output = output or x
        output = not output


class nandGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result(self):
        output = True
        for x in self.input:
            output = output and x
        output = not output


class xorGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)

    def compute_result(self):
        output = False
        counter = 0
        for x in self.input:
            if x == 1:
                counter += 1
        if counter%2 == 1:
            output = True


class xnorGate(logicGate):
    def __init__(self, typev, name):
        logicGate.__init__(self, typev, name)
    
    def compute_result(self):
        output = False
        counter = 0
        for x in self.input:
            if x == 0:
                counter += 1
        if counter%2 == 0:
            output = True
 
#fuction that produces the circuite ouput with recusion
def trace_output(gate_name):
    #print(gate_name)

    gate = all_gates[gate_name]

    #first verify if logic gate is already complete
    if gate.verify_complete():
        gate.compute_result()
        return gate.output
    
    #recursion to get all logic gates input
    for x in gate.connection_wires:
        gate.add_input(trace_output(x))
        gate.wire_complete(x)
    
    #return and error handling
    if gate.verify_complete():
        gate.compute_result()
        return gate.output
    else:
        sys.exit("Invalid input might have occured!")
    

    
            


