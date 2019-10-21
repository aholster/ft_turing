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
        nonlocal inf_left
        if direction == "RIGHT":
            if index + 1 < len(tape):
                index += 1
            else:
                tape = f'{tape}{blank}'
                index += 1
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
    b = tmachine["blank"]
    if len(tape) == 0:
        tape = f'{b}'
    index = 0
    inf_left = False
    real_writes = 0
    total_steps = 0
    while not curr_state in tmachine['finals']:
        txt = f'[{tape[:index]}<{tape[index]}>{tape[index + 1:]}{b}{b}{b}]\t'
        txt += f'({curr_state}, {tape[index]}) -> '

        cur_instruct = None
        for instruction in turing_table[curr_state]:
            if instruction['read'] == tape[index]:
                cur_instruct = instruction
        if cur_instruct == None:
            print(f'amachine could not find viable state from ({curr_state}, {tape[index]})')
            break

        if tape[index] != cur_instruct['write']:
            real_writes += 1
        tape = f'{tape[:index]}{cur_instruct["write"]}{tape[index + 1:]}'

        if not cur_instruct['to_state'] in tmachine['finals']:
            if move_head(cur_instruct['action'], tmachine['blank']) == False:
                break

        txt += f'({cur_instruct["to_state"]}, {tape[index]}, {cur_instruct["action"]})'
        print(txt)
        curr_state = cur_instruct['to_state']
        total_steps += 1

    if curr_state in tmachine['finals']:
        print(
            f'amachine reached acceptance state: "{curr_state}", tape is now:[{tape}]')
    else:
        print(
            f'amachine had its process interrupted in state: "{curr_state}", tape is now:[{tape}]')
    print(f'Total amount of steps: {total_steps}, and real writing actions: {real_writes}')
