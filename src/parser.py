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
    if command == "morr":
        all_gates[identifier] = orGate(command[1:], ideentifier)
    elif command == "mand":
        all_gates[identifier] = andGate(command[1:], ideentifier)
    elif command == "mnot":
        all_gates[identifier] = notGate(command[1:], ideentifier)



def parser():
    file = open("../user_scipt/circuit.txt", "r")
    lines = file.readlines()

    for x in lines:
        x.replace("(", " ")
        x.replace(",", " ")
        x.replace(")", " ")
        components.split()
        #not done yet...

            






