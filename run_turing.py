def write_intro(tmachine, turing_table):
    '''writes short introductory statement about the turing machine described'''
    tokens = 'name', 'alphabet', 'states', 'initial', 'finals'
    for token in tokens:
        print(f'{token} : {tmachine[token]}')
    for state in turing_table:
        for entry in turing_table[state]:
            print(
                f'({state}, {entry["read"]}) -> ({entry["to_state"]}, {entry["write"]}, {entry["action"]})')
    print('******************************************')

class TransitionError(Exception):
    pass

def run_turing(tmachine, tape):
    '''turing machine executer

    turing_machine_loop handles actual transition table and turing machine execution
    
    run_turing itself contains calls to necesary functions
    and supporting code for calculating time complexity'''

    def turing_machine_loop(turing_table, tmachine):
        '''handles transition table looping
        
        move_head handles movement of turing machine head, and memory tape expansion'''
        def move_head(direction,  blank):
            '''handles moving head or expanding tape'''
            nonlocal index
            nonlocal tape
            nonlocal inf_left
            if direction == "RIGHT":
                index += 1
                if not index + 1 < len(tape):
                    tape = f'{tape}{blank}'
            else:
                if index != 0:
                    index -= 1
                else:
                    if inf_left != True:
                        if input('Turing Machine requesting unbounded LEFT tape, authorize? y/n:') == 'n':
                            raise TransitionError(f'amachine is trying to access beyond start of tape')
                        else:
                            inf_left = True
                    tape = f'{blank}{tape}'


        nonlocal curr_state
        nonlocal total_steps
        nonlocal tape
        b = tmachine["blank"]
        index = 0
        while not curr_state in tmachine['finals']:
            txt = f'[{tape[:index]}<{tape[index]}>{tape[index + 1:]}{b}{b}{b}]\t'
            txt += f'({curr_state}, {tape[index]}) -> '

            for instruction in turing_table[curr_state]:
                if instruction['read'] == tape[index]:
                    tape = f'{tape[:index]}{instruction["write"]}{tape[index + 1:]}'

                    txt += f'({instruction["to_state"]}, {tape[index]}, {instruction["action"]})'
    
                    if not instruction['to_state'] in tmachine['finals']:
                            move_head(instruction['action'], tmachine['blank'])

                    print(txt)
                    curr_state = instruction['to_state']
                    total_steps += 1
                    break
            else:
                raise TransitionError(f'amachine could not find viable state from ({curr_state}, {tape[index]})')



    write_intro(tmachine, tmachine['transitions'])
    curr_state = tmachine['initial']
    if len(tape) == 0:
        tape = f'{tmachine["blank"]}'
    tape_len = len(tape)
    inf_left = False
    total_steps = 0

    try:
        turing_machine_loop(tmachine['transitions'], tmachine)
    except TransitionError as transerr:
        print(f'Error: {transerr}')
    finally:
        print('******************************************')

    if curr_state in tmachine['finals']:
        print(f'amachine reached acceptance state: "{curr_state}", tape is now:[{tape}]')
    else:
        print(f'amachine had its process interrupted in state: "{curr_state}", tape is now:[{tape}]')

    import math
    print(f'''
Total amount of steps: {total_steps}, initial tape len {tape_len}

| for this tape, O is ({total_steps}), N is ({tape_len})
| aprox time complexity is (n * {total_steps / tape_len})
|	linear O(n) ({tape_len})
|	linearithmetic O(n log n) ({tape_len * math.log10(tape_len)})
|	quadratic O(n^2) ({tape_len ** 2})
|	factorial O(n!) ({math.factorial(tape_len)})
| the closest of shown values might be the real one
| (ignoring constant time or constant factors (ie: fractional power or polynomial))''')

