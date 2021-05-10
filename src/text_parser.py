import sys

from logic_gate import logicGate
from logic_gate import orGate
from logic_gate import andGate
from logic_gate import notGate
from logic_gate import norGate
from logic_gate import nandGate
from logic_gate import xorGate
from logic_gate import xnorGate
from logic_gate import all_gates

outputs = []


def create_gate(command, identifier):
    result = True

    if command == "morr":
        all_gates[identifier] = orGate(command[1:], identifier)
    elif command == "mand":
        all_gates[identifier] = andGate(command[1:], identifier)
    elif command == "mnot":
        all_gates[identifier] = notGate(command[1:], identifier)
    elif command == "mnor":
        all_gates[identifier] = norGate(command[1:], identifier)
    elif command == "mnad":
        all_gates[identifier] = nandGate(command[1:], identifier)
    elif command == "mxor":
        all_gates[identifier] = xorGate(command[1:], identifier)
    elif command == "mxnr":
        all_gates[identifier] = xnorGate(command[1:], identifier)
    else:
        result = False

    return result

def insert_cg(all_signals, identifier):
    for x in all_signals:
        if x.isnumeric():
            all_gates[identifier].add_input(int(x))
        else:
            all_gates[identifier].add_wire(x)


def create_output(command, identifier):
    result = True

    if command == "output":
        outputs.insert(len(outputs), identifier)
    else:
        result = False
    
    return result

def insert_co(identifier):
    if identifier in all_gates:
        if identifier not in outputs:
            outputs.insert(len(outputs), identifier)
    else:
        message = "Error: " + identifier + " is not in your pool of logic gates"
        sys.exit(message)



def parser():
    file = open("user_script/circuit.txt", "r")
    lines = file.readlines()
    counter = 0

    #x represents an individual line
    for x in lines:
        x = x.replace("(", " ")
        x = x.replace(",", " ")
        x = x.replace(")", " ")
        components = x.split()
        
        #good to add some error control for users

        insertion_operation = create_gate(components[0], components[1])
        if insertion_operation:
            insert_cg(x[2:], components[0])
        
        insertion_operation = create_output(components[0], components[1])
        if insertion_operation:
            insert_co(components[1])
    

        #more functionality will be supported in the future
        #please add langugae features here

            






