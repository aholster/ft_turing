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
		print('Blank Invalid', tdict['blank'])
		veracity = False
	if not tdict['blank'] in tdict['alphabet']:
		print('Blank not defined in alphabet', tdict['blank'])
		veracity = False
	if not tdict['initial'] in tdict['states']:
		print('Initial state invalid', tdict['initial'])
		veracity = False
	return (veracity)