#this is the main file
from text_parser import *
from logic_gate import all_gates
from logic_gate import trace_output


def main():
    parser()

    print(outputs)
    print(all_gates)

    for x in outputs:
        value = trace_output(x)
        print("Gate " + x + " has an ouput value of " + value + ".")
    
    print("Finish;")


if __name__ == "__main__":
    main()
