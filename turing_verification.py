def verify_turing_transition_table(ttbl):
    ''' verifies transition table validity as defined in subject'''
    veracity = True
    for states in ttbl['states']:
        if not states in ttbl['transitions'] and not states in ttbl['finals']:
            print('Warning: Leftover State found:', states)
            veracity = False

    ttransition_table = ttbl['transitions']
    for state_handler in ttransition_table.keys():
        linen = 0
        if not state_handler in ttbl['states']:
            print('Warning: State not properly declared Found: ', state_handler)
            veracity = False
        if type(ttransition_table[state_handler]) != list:
                print(f'Warning: "{state_handler}" is not a list type')
                veracity = False
                continue
        for t_instructions in ttransition_table[state_handler]:
            linen += 1
            if (type(t_instructions) != dict):
                print(f'Warning: "{t_instructions}" is not a dict type, at line :{linen}')
                veracity = False
                continue
            val_actions = 'LEFT', 'RIGHT'
            expected_fields = {'read': ttbl['alphabet'],
                               'to_state': ttbl['states'],
                               'write':  ttbl['alphabet'],
                               'action': val_actions}
            if set(expected_fields) != set(t_instructions.keys()):
                print(f'Warning: Bad Fields at "{state_handler}"')
                veracity = False
            for entry in expected_fields.keys():
                if not entry in t_instructions.keys():
                    print(
                        f'Warning: Field "{entry}" not present in,"{state_handler}" at {linen}')
                    veracity = False
                elif not t_instructions[entry] in expected_fields[entry]:
                    print(
                        f'Warning: bad entry "{entry}": "{t_instructions[entry]}" unexpected value, line{linen}')
                    veracity = False
    return (veracity)


def verify_turing_dict(tdict):
    ''' verifies that turing_dict contains the necesary fields
    also checks if said fields contain proper necesary items
    as defined in subject
    DOES NOT VERIFY TRANSITIONS '''
    prereq_fields = {'name': str,
                     'alphabet': list,
                     'blank': str,
                     'states': list,
                     'initial': str,
                     'finals': list,
                     'transitions': dict}

    if set(prereq_fields.keys()) != set(tdict.keys()):
        print('Warning: incorrect keys in json')
        return False
    for key in prereq_fields:
        if type(tdict[key]) != prereq_fields[key]:
            print(f'Warning: field is wrong type: "{key}" "{type(tdict[key])}"')
            return False
    veracity = True
    for token in tdict['alphabet']:
        if len(token) != 1:
            print('Warning: Alphabet Token Invalid:', token)
            veracity = False
    if len(tdict['blank']) != 1:
        print('Warning: Blank Invalid:', tdict['blank'])
        veracity = False
    if not tdict['blank'] in tdict['alphabet']:
        print('Warning: Blank not defined in alphabet:', tdict['blank'])
        veracity = False
    if not tdict['initial'] in tdict['states']:
        print('Warning: Initial state invalid:', tdict['initial'])
        veracity = False
    return (veracity)
