import sys
import json


from turing_verification import verify_turing_dict
from turing_verification import verify_turing_transition_table


def usage():
    '''prints usage? '''
    print('''usage: ft_turing [-h] jsonfile input

positional arguments:

  jsonfile              json description of the machine

  input                 input of the machine

optional arguments:
  -h, --help            show this help message and exit''')
    sys.exit(1)


def verify_json_machine(json_name):
    '''verifies json turing machine is not mangled'''
    try:
        with open(sys.argv[1], "r") as file:
            turing_dict = json.load(file)
    except:
        print('error: could not open file')
        sys.exit(1)
    else:
        if (verify_turing_dict(turing_dict) == False):
            print('error: json machine-structure mangled')
            sys.exit(1)
        elif (verify_turing_transition_table(turing_dict) == False):
            print('error: transition table invalid')
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
        else:
            print('error: not enough arguments')
            sys.exit(1)
    elif len(sys.argv) == 3:
        verify_json_machine(sys.argv[1])
    else:
        print('error: too many arguments')
