def write_intro(tmachine, turing_table):
    tokens = 'name', 'alphabet', 'states', 'initial', 'finals'
    for token in tokens:
        print(f'{token} : {tmachine[token]}')
    for state in turing_table:
        for entry in turing_table[state]:
            print(f'({state}, {entry["read"]}) -> ({entry["to_state"]}, {entry["write"]}, {entry["action"]})')
    print('******************************************')


def run_turing(tmachine):
    turing_table = tmachine['transitions']
    write_intro(tmachine, turing_table)
    # curr_state = tmachine['initial']
