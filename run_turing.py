def write_intro(tmachine, turing_table):
    tokens = 'name', 'alphabet', 'states', 'initial', 'finals'
    for token in tokens:
        print(f'{token} : {tmachine[token]}')
    for state in turing_table:
        for entry in turing_table[state]:
            print(
                f'({state}, {entry["read"]}) -> ({entry["to_state"]}, {entry["write"]}, {entry["action"]})')
    print('******************************************')


def run_turing(tmachine, tape):
    def move_head(direction,  blank):
        '''handles moving head or expanding tape'''
        nonlocal index
        nonlocal tape
        nonlocal inf_right
        nonlocal inf_left
        if direction == "RIGHT":
            if not index < len(tape) - 1:
                index += 1
            else:
                if inf_right != True:
                    if input('Turing Machine requesting unbounded RIGHT tape, authorize? y/n:') == 'n':
                        return False
                    else:
                        inf_right = True
                index += 1
                tape = f'{tape}{blank}'
        else:
            if index != 0:
                index -= 1
            else:
                if inf_left != True:
                    if input('Turing Machine requesting unbounded LEFT tape, authorize? y/n:') == 'n':
                        return False
                    else:
                        inf_left = True
                tape = f'{blank}{tape}'
        return True

    turing_table = tmachine['transitions']
    write_intro(tmachine, turing_table)
    curr_state = tmachine['initial']
    index = 0
    inf_left = False
    inf_right = False
    while not curr_state in tmachine['finals']:
        txt = f'[{tape[:index]}<{tape[index]}>{tape[index + 1:]}]\t'
        txt += f'({curr_state}, {tape[index]}) -> '

        next_state = None
        for instruction in turing_table[curr_state]:
            if instruction['read'] == tape[index]:
                next_state = instruction
        if next_state == None:
            print(
                f'FSM could not find viable state from ({curr_state}, {tape[index]})')
            break

        tape = f'{tape[:index]}{next_state["write"]}{tape[index + 1:]}'

        if move_head(next_state['action'], tmachine['blank']) == False:
            break

        curr_state = next_state['to_state']
        txt += f'({curr_state}, {tape[index]}, {next_state["action"]})'
        print(txt)

    if curr_state in tmachine['finals']:
        print(
            f'amachine reached acceptance state: "{curr_state}", tape is now:[{tape}]')
    else:
        print(
            f'amachine had its process interrupted in state: "{curr_state}", tape is now:[{tape}]')
