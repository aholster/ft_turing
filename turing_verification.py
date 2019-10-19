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
		for event_handler in ttransition_table[state_handler]:
			linecount += 1
			if not 'read' in event_handler:
				print('Warning missing field: Read in:', state_handler, 'at line:', linecount)
				veracity = False
			elif not event_handler['read'] in ttbl['alphabet']:
				print('Warning: wrong character:', event_handler['read'], 'in Read Field at', state_handler, 'line:', linecount)
				veracity = False
			
			if not 'to_state' in event_handler:
				print('Warning missing field: State in:', state_handler, 'at line:', linecount)
				veracity = False
			elif not event_handler['to_state'] in ttbl['states']:
				print('Warning: wrong state:', event_handler['to_state'], 'in to_state Field at', state_handler, 'line:', linecount)
				veracity = False
			
			if not 'write' in event_handler:
				print('Warning missing field: Write in:', state_handler, 'at line:', linecount)
				veracity = False
			elif not event_handler['write'] in ttbl['alphabet']:
				print('Warning: wrong character:', event_handler['write'], 'in Write Field at', state_handler, 'line:', linecount)
				veracity = False
			
			val_actions ='LEFT', 'RIGHT'
			if not 'action' in event_handler:
				print('Warning missing field: Action in:', state_handler, 'at line:', linecount)
				veracity = False
			elif not event_handler['action'] in val_actions:
				print('Warning: wrong action listed at:', state_handler, 'at line', linecount)
				veracity = False	
	return (veracity)


def verify_turing_dict(tdict):
	''' verifies that turing_dict contains the necesary fields
	also checks if said fields contain proper necesary items
	as defined in subject
	DOES NOT VERIFY TRANSITIONS '''
	veracity = True
	prereq_fields = 'name', 'alphabet', 'blank', 'states', 'initial', 'finals', 'transitions'
	for key in prereq_fields:
		if not key in tdict:
			print('Field missing:', key)
			veracity = False
	for token in tdict['alphabet']:
		if len(token) != 1:
			print('Alphabet Token Invalid:', token)
			veracity = False
	if len(tdict['blank']) != 1:
		print('Blank Invalid:', tdict['blank'])
		veracity = False
	if not tdict['blank'] in tdict['alphabet']:
		print('Blank not defined in alphabet:', tdict['blank'])
		veracity = False
	if not tdict['initial'] in tdict['states']:
		print('Initial state invalid:', tdict['initial'])
		veracity = False
	return (veracity)