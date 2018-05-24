import csv

path1 = "./modified_decSales.csv"
path2 = "./profit_decSales.csv"
#path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/augSales.csv"
#path2 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/modified_augSales.txt"

prices_dic = {'1': '7', '2': '8', '3': '12', '4': '21', '5': '8', '6': '10', '12': '30', '14': '10', '15': '35', '16': '5', '18': '55', '19': '20', '20': '25', '21': '30', '22': '15', '23': '20', '24': '25', '25': '10', '26': '5', '41': '15', '45': '10', '46': '18', '47': '10', '48': '10', '49': '20', '50': '20', '51': '15', '54': '20', '73': '30', '74': '25', '76': '33', '93': '32', '94': '14', '98': '10', '99': '10', '100': '35', '102': '10', '103': '10', '104': '10', '105': '25', '107': '10', '108': '20', '123': '8', '124': '25', '125': '35', '126': '40', '127': '55', '128': '25', '129': '16', '130': '21', '131': '21', '132': '21', '133': '21', '134': '15', '135': '21', '136': '25', '137': '30', '138': '22', '139': '21', '140': '26', '141': '40', '142': '25', '143': '16', '144': '20', '145': '40', '146': '85', '147': '75', '148': '90', '149': '3', '150': '6', '151': '12', '152': '15', '153': '17', '154': '22', '155': '27', '156': '30', '157': '32', '158': '14', '159': '20', '160': '25', '161': '12', '162': '18', '163': '20', '164': '81', '165': '30', '166': '85', '167': '10', '168': '27', '169': '25', '170': '20', '171': '20', '172': '80', '173': '45', '174': '12', '175': '18', '176': '30', '177': '95', '178': '40', '179': '23', '180': '170', '181': '10', '182': '95', '183': '20', '184': '25', '185': '25', '186': '18', '187': '15', '188': '18', '189': '12', '190': '15', '191': '20', '192': '20', '193': '18', '194': '10', '195': '35', '196': '25', '197': '2', '198': '20', '900': '100', '901': '-100', '902': '25', '903': '5'}
maindic = {'2': [('17', 'F2'), ('17', 'F3'), ('17', 'F1'), ('17', 'F4'), ('18', 'F2')

], '151': [('20', 'F0'), ('20', 'F3'), ('20', 'F4'), ('20', 'F2'), ('21', 'F0'), ('22', 'F0'), ('20', 'F1'), ('23', 'F0'), ('0', 'F0'), ('21', 'F4'), ('21', 'F2'), ('22', 'F1'), ('21', 'F1'), ('21', 'F3'), ('23', 'F1'), ('22', 'F3'), ('22', 'F4'), ('0', 'F1'), ('22', 'F2'), ('23', 'F2'), ('23', 'F3'), ('23', 'F4'), ('1', 'F1'), ('0', 'F2'), ('0', 'F4'), ('0', 'F3'), ('1', 'F3'), ('1', 'F2'), ('1', 'F4')

], '134': [ ('0', 'F1'),  ('0', 'F0'),  ('0', 'F2'), ('0', 'F3'), ('23', 'F1'), ('23', 'F2'), ('23', 'F0'), ('22', 'F1'),  ('23', 'F3'), ('0', 'F4'), ('23', 'F4'), ('22', 'F2'),  ('22', 'F3'),  ('22', 'F4'), ('22', 'F0')

], '130': [('20', 'F0'), ('21', 'F0'), ('0', 'F1'), ('23', 'F0'), ('23', 'F1'), ('20', 'F1'), ('23', 'F2'), ('21', 'F1'), ('0', 'F0'), ('21', 'F2'), ('0', 'F2'), ('21', 'F4'), ('20', 'F2'), ('23', 'F3'), ('21', 'F3'), ('20', 'F3'), ('23', 'F4'), ('0', 'F4'),  ('0', 'F3'), ('20', 'F4')

], '123': [('17', 'F3'), ('17', 'F1'), ('17', 'F2'), ('17', 'F4'), ('18', 'F2')

], '188': [('17', 'F1'), ('17', 'F4'), ('18', 'F2'), ('17', 'F3'), ('17', 'F2')

], '128': [('23', 'F4'), ('23', 'F2'), ('22', 'F4'), ('0', 'F3'), ('23', 'F3'), ('23', 'F1'), ('0', 'F4'), ('0', 'F1'), ('0', 'F2'), ('22', 'F2'), ('1', 'F3'), ('22', 'F3'), ('21', 'F4'), ('1', 'F4'), ('1', 'F2'), ('1', 'F1'), ('23', 'F0'), ('21', 'F3'), ('22', 'F1'), ('21', 'F2'), ('21', 'F1'), ('0', 'F0'), ('22', 'F0')

], '154': [('21', 'F1'), ('23', 'F1'), ('22', 'F2'), ('0', 'F1'), ('21', 'F3'), ('21', 'F4'), ('22', 'F1'), ('21', 'F2'), ('22', 'F3'), ('0', 'F0'), ('21', 'F0'), ('23', 'F3'), ('20', 'F1'), ('0', 'F2'), ('23', 'F4'), ('23', 'F2'), ('22', 'F4'), ('0', 'F3'), ('23', 'F0'), ('0', 'F4'), ('20', 'F4'), ('20', 'F2'), ('20', 'F3'), ('22', 'F0'),  ('20', 'F0')

], '146': [('20', 'F0'), ('20', 'F3'), ('20', 'F4'), ('22', 'F0'), ('21', 'F0'), ('20', 'F2'), ('20', 'F1'), ('23', 'F0'), ('21', 'F2'), ('21', 'F1'), ('21', 'F4'), ('21', 'F3'), ('22', 'F1'), ('22', 'F3'), ('0', 'F0')

], '107': [ ('17', 'F2'), ('23', 'F2'), ('0', 'F2'), ('17', 'F3'), ('22', 'F2'), ('23', 'F3'), ('17', 'F4'), ('0', 'F3'), ('17', 'F1'), ('22', 'F3'), ('0', 'F4'), ('23', 'F4'), ('22', 'F4')

], '76': [('1', 'F3'), ('22', 'F0'), ('23', 'F4'), ('1', 'F2'), ('1', 'F4'), ('22', 'F4'), ('21', 'F3'), ('1', 'F1'), ('0', 'F4'), ('23', 'F0'), ('22', 'F3'), ('21', 'F4'), ('22', 'F1'), ('0', 'F3'), ('21', 'F1'), ('0', 'F1'), ('0', 'F0'), ('23', 'F3'), ('20', 'F3'), ('23', 'F1'), ('21', 'F2'), ('22', 'F2'), ('20', 'F2'), ('20', 'F1'), ('0', 'F2'), ('20', 'F4'), ('23', 'F2'), ('21', 'F0'), ('20', 'F0')

], '169': [('1', 'F2'), ('1', 'F1'), ('1', 'F3'), ('21', 'F1'), ('22', 'F1'), ('17', 'F3'), ('0', 'F3'), ('21', 'F3'), ('22', 'F2'), ('0', 'F2'), ('21', 'F2'), ('22', 'F3'), ('23', 'F3'), ('22', 'F4'),  ('17', 'F4'), ('23', 'F2'), ('21', 'F4'), ('17', 'F2'), ('23', 'F4'),  ('17', 'F1'), ('0', 'F4'), ('23', 'F1'), ('1', 'F4'), ('22', 'F0'), ('0', 'F1'), ('23', 'F0')

], '142': [('22', 'F3'), ('23', 'F3'), ('23', 'F4'), ('0', 'F3'), ('0', 'F4'), ('22', 'F4'), ('21', 'F3'), ('23', 'F1'), ('23', 'F2'),  ('22', 'F1'), ('20', 'F4'), ('0', 'F2'), ('22', 'F2'), ('21', 'F2'), ('21', 'F1'), ('21', 'F4'), ('20', 'F3'), ('20', 'F1'), ('0', 'F1'), ('0', 'F0'), ('23', 'F0'), ('21', 'F0'), ('22', 'F0'), ('20', 'F2')

], '124': [('20', 'F1'), ('21', 'F1'), ('22', 'F1'), ('20', 'F2'), ('21', 'F2'), ('22', 'F2'), ('21', 'F3'), ('20', 'F4'), ('20', 'F3'), ('22', 'F3'), ('21', 'F4'), ('22', 'F4'), ('21', 'F0'), ('22', 'F0')

], '138': [('22', 'F1'), ('22', 'F2'), ('23', 'F1'), ('23', 'F2'), ('22', 'F3'), ('22', 'F4'), ('23', 'F3'), ('23', 'F4'), ('0', 'F1')

], '26': [('0', 'F0'), ('23', 'F0'), ('0', 'F2')

], '25': [('0', 'F4'), ('1', 'F3'), ('1', 'F4'), ('1', 'F2'), ('18', 'F2'), ('1', 'F1'), ('0', 'F3'), ('0', 'F2')

], '108': [('18', 'F2'), ('17', 'F4'), ('17', 'F2')

], '164': [('20', 'F3'), ('20', 'F4'), ('20', 'F2'), ('21', 'F0'), ('20', 'F0'), ('20', 'F1'), ('22', 'F0'), ('23', 'F0'), ('21', 'F4'), ('21', 'F3')

], '1': [('0', 'F0'), ('0', 'F2'), ('0', 'F1'),  ('0', 'F3'), ('23', 'F2'), ('23', 'F3'), ('0', 'F4'), ('23', 'F1')

], '22': [('1', 'F3'), ('18', 'F2'), ('1', 'F1'), ('1', 'F2'), ('1', 'F4')

], '15': [ ('21', 'F3'), ('22', 'F3'), ('0', 'F4'), ('22', 'F4'), ('20', 'F3')

], '129': [('1', 'F1'), ('1', 'F4'), ('22', 'F0'), ('21', 'F0'), ('1', 'F3'), ('0', 'F4'), ('1', 'F2')

], '170': [('18', 'F2')

], '93': [('1', 'F1'), ('22', 'F1')

], '135': [('0', 'F1'), ('0', 'F4'), ('23', 'F2'), ('0', 'F2'), ('23', 'F4')

], '5': [('0', 'F0')

], '139': [('23', 'F0'), ('21', 'F0'), ('22', 'F0')

], '100': [('1', 'F4')

], '141': [('23', 'F3'), ('23', 'F2'), ('22', 'F3')

], '161': [('22', 'F0')

], '193': [('1', 'F4')

]}



segment_wt = {'F1': 12, 'F2': 32, 'F3': 30, 'F4': 20, 'F5': 3, 'F1': 1, 'H1': 2, 'H2': 20, 'P5':1, 'F6':1, 'B1':1, 'H4':1, 'F7':1, 'D1':1, 'H3':1, 'P3':1, 'P1':1, 'P2':1, 'F0': 1}
hr_total_dict = {}
seg_total_dict = {}

missing = 0
total_revenue = 0
total_revenue_orig = 0
minute_partition = 59

def get_penalty():
	ans = 0

	for key, val in maindic.items():
		seg_wt_total = 0
		allseg = []
		allhrs = []
		for pair in val:
			allseg.append(pair[1])
			allhrs.append(pair[0])
		allseg = set(allseg)
		allhrs = set(allhrs)
		for seg in allseg:
			seg_wt_total += segment_wt[seg]
		hr_total_dict[key] = len(allhrs)
		seg_total_dict[key] = seg_wt_total
		total_hours = min(len(allhrs)**2, 50)
		# hr_total_dict[key] = len(allhrs)
		# seg_total_dict[key] = len(allseg)
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		'''ALTER HERE TO NOT RETURN THE MAX CHANGE BUT SOMETHING ELSE'''
		price_change = min(int(prices_dic[key])*.1, 10)
		ans += price_change * total_hours * seg_wt_total
	return ans

def formula(item, hr, grp, price):
	if(str(item) not in maindic):
		return 0
	if((str(hr), str(grp)) not in maindic[str(item)]):
		return 0
	else:
		return min(price*.1, 10)
	
with open(path1,'rt',encoding="latin1") as csvfile:
	r = csv.reader((x.replace('\0', '') for x in csvfile), delimiter='\t')

	count = 0
	flag = True
	for row in r:
		if(flag):
			flag = False
			continue
		else:
			itemid = row[2]
			quant = int(row[3])
			hour = row[7]
			group = row[6]
			price = int(prices_dic[str(itemid)])
		
			total_revenue += (price + formula(itemid, hour, group, price)) * quant
			total_revenue_orig += price*quant

	print('CHECK IF HAVE OR HAVE NOT REPLACED THE ITEMHOURSEG DICT WITH THE NEW ONE')
	print('CHECK IF HAVE OR HAVE NOT REPLACED THE ITEMHOURSEG DICT WITH THE NEW ONE')
	print('CHECK IF HAVE OR HAVE NOT REPLACED THE ITEMHOURSEG DICT WITH THE NEW ONE')
	print('enter support used')
	sup = input()
	print('enter conf used')
	conf= input()
	print('USING DIFFERNT FILES!!!')
	print('USING DIFFERNT FILES!!!')
	print('USING DIFFERNT FILES!!!')
	print('USING DIFFERNT FILES!!!')
	print('HAVE YOU USED THE CORRECT FILES?')
	ip = input()
	if(ip != 'yes'):
		print('DOOOODOOOODOOOODOOOODOOOODOOOODOOOODOOOODOOOODOOOODOOOO')
	print('tr = ',total_revenue)
	print('penalty= ',get_penalty())
	print('orig tr = ', total_revenue_orig)
	print('profit% = ', (total_revenue - total_revenue_orig)*100/total_revenue_orig)
	print('net profit value = ', total_revenue - total_revenue_orig)
	print('net profit MINUS PENALTY = ', total_revenue - total_revenue_orig - get_penalty())
	print()
	print()
	print('HR TOTAL DICT', hr_total_dict)
	print()
	print()
	print()
	print('SEG WT DICT', seg_total_dict)
	
