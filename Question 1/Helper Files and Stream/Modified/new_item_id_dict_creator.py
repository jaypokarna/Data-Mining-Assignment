path1 = 'E:\ACADEMICS\Data Mining\Assignment\Dataset for DM Assignment\Modified\with_newline_itemid_hr_dict.txt'
path2 = 'E:\ACADEMICS\Data Mining\Assignment\Dataset for DM Assignment\Modified\itemid_hour_group_dict.txt'

with open(path1, 'w') as with_newline, open(path2, 'r') as orig:
	towrite = ''
	while(True):
		c = orig.read(1)
		if not c:
			break
		if c == ']':
			towrite += '\n\n'
			towrite += c
		else:
			towrite += c
		
	with_newline.write(towrite)