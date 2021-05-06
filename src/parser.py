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
    elif command == "output":
        outputs.insert(len(outputs), identifier)
    else:
        result = False

    return result

def create_output(command, identifier):
    result = True

    if command == "output":
        outputs.insert(len(outputs), identifier)
    else:
        result = False
    
    return result


def parser():
    file = open("../user_scipt/circuit.txt", "r")
    lines = file.readlines()
    counter = 0

    for x in lines:
        x.replace("(", " ")
        x.replace(",", " ")
        x.replace(")", " ")
        components = x.split()
        insertion_operation = create_gate(components[0], components[1])

        #current problem: how to parse different types of commands eligently
        if insertion_operation:
            #...
        


        #not done yet...

            






