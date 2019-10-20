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
    turing_table = tmachine['transitions']
    write_intro(tmachine, turing_table)
    curr_state = tmachine['initial']
    index = 0
    while not curr_state in tmachine['finals']:
        # print(f'[{tape[:index]}<{tape[index]}>{tape[index + 1:]}]')
        txt = f'[{tape[:index]}<{tape[index]}>{tape[index + 1:]}]\t'
        txt += f'({curr_state}, {tape[index]}) -> '

        next_state = None
        for instruction in turing_table[curr_state]:
            if instruction['read'] == tape[index]:
                next_state = instruction
        if next_state == None:
            print(f'FSM could not find viable state from ({curr_state}, {tape[index]})')
            break

        tape = f'{tape[:index]}{next_state["write"]}{tape[index + 1:]}'

        curr_state = next_state['to_state']
        if next_state['action'] == "RIGHT":
            index += 1
        else:
            index -= 1

        txt += f'({curr_state}, {tape[index]}, {next_state["action"]})'
        print(txt)
    print(f'FSM reached acceptance state: {curr_state}, tape is now:{tape}')
