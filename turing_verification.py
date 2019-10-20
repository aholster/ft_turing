def verify_turing_transition_table(ttbl):
    ''' verifies transition table validity as defined in subject'''
    veracity = True
    for states in ttbl['states']:
        if not states in ttbl['transitions'] and not states in ttbl['finals']:
            print('Warning: Leftover State found:', states)
            veracity = False

    ttransition_table = ttbl['transitions']
    for state_handler in ttransition_table:
        linecount = 0
        if not state_handler in ttbl['states']:
            print('Warning: Unlisted State Found: ', state_handler)
            veracity = False
        for t_instructions in ttransition_table[state_handler]:
            linecount += 1
            if len(t_instructions) != 4:
                print('Warning: wrong number of fields in', f'"{state_handler}"', 'at line', linecount)
                veracity = False
            def print_field_error(err_str, bad_entry):
                nonlocal veracity
                print(err_str, f'"{bad_entry}"', 'in', f'"{state_handler}"', 'at line', linecount)
                veracity = False

            if not 'read' in t_instructions:
                print_field_error('Warning: missing field:', 'read')
            elif not t_instructions['read'] in ttbl['alphabet']:
                print_field_error('Warning: wrong character entry:', t_instructions['read'])

            if not 'to_state' in t_instructions:
                print_field_error('Warning: missing field:', 'to_state')
            elif not t_instructions['to_state'] in ttbl['states']:
                print_field_error('Warning: wrong state entry:', t_instructions['to_state'])

            if not 'write' in t_instructions:
                print_field_error('Warning: missing field:', 'write')
            elif not t_instructions['write'] in ttbl['alphabet']:
                print_field_error('Warning: wrong character entry:', t_instructions['write'])

            val_actions = 'LEFT', 'RIGHT'
            if not 'action' in t_instructions:
                print_field_error('Warning: missing field:', 'action')
            elif not t_instructions['action'] in val_actions:
                print_field_error('Warning: wrong action entry:', t_instructions['action'])
    return (veracity)


def verify_turing_dict(tdict):
    ''' verifies that turing_dict contains the necesary fields
    also checks if said fields contain proper necesary items
    as defined in subject
    DOES NOT VERIFY TRANSITIONS '''
    veracity = True
    if (len(tdict) != 7):
        print('Warning: numer of fields should be 7 but is:', len(tdict))
        veracity = False
    prereq_fields = 'name', 'alphabet', 'blank', 'states', 'initial', 'finals', 'transitions'
    for key in prereq_fields:
        if not key in tdict:
            print('Warning: Field missing:', key)
            veracity = False
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
