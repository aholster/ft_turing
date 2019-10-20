import sys
import json


from turing_verification import verify_turing_dict
from turing_verification import verify_turing_transition_table

from run_turing import run_turing


def usage():
    '''prints usage? '''
    print('''usage: ft_turing [-h] jsonfile input

positional arguments:

  jsonfile              json description of the machine

  input                 input of the machine

optional arguments:
  -h, --help            show this help message and exit''')


def verify_input_tape(tdict, input_tape):
    veracity = True
    for char in input_tape:
        if not char in tdict['alphabet']:
            print(
                f'Warning: input tape character {char} is not part of alphabet: {tdict["alphabet"]}')
            veracity = False
        if char in tdict['blank']:
            print(f'Warning: input tape character {char} is BLANK character')
            veracity = False
    return veracity


def verify_json_machine(json_name, input_str):
    '''verifies json turing machine is not mangled'''
    try:
        with open(sys.argv[1], "r") as file:
            turing_dict = json.load(file)
    except:
        print('error: could not open file')
        return False
    else:
        try:
            if (verify_turing_dict(turing_dict) == False):
                print('error: json machine-structure mangled')
                return False
            if (verify_turing_transition_table(turing_dict) == False):
                print('error: transition table invalid')
                return False
            if (verify_input_tape(turing_dict, input_str) == False):
                print('error: input tape invalid')
                return False
            run_turing(turing_dict, input_str)
        except Exception as err:
            print(f'Error: {err}')

    return True


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
        else:
            print('error: not enough arguments')
            sys.exit(1)
    elif len(sys.argv) == 3:
        if verify_json_machine(sys.argv[1], sys.argv[2]) == False:
            sys.exit(1)
    else:
        print('error: too many arguments')
        sys.exit(1)

    sys.exit(0)
