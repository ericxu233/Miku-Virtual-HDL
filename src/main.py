#this is the main file
from text_parser import *
from logic_gate import all_gates
from logic_gate import trace_output


def main():
    parser() 

    for x in outputs:
        value = trace_output(x)*1
        print("Gate " + str(x) + " has an ouput value of " + str(value) + ".")
    
    print("Finish;")


if __name__ == "__main__":
    main()
