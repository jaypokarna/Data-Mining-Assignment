import csv

# path1 = "./quantity_modified/quant_modified_novSales.csv"
path1 = "./quantity_modified/octPLUS18_nov_combined_quant_modified.csv"

prices_dic = {'1': '7', '2': '8', '3': '12', '4': '21', '5': '8', '6': '10', '12': '30', '14': '10', '15': '35', '16': '5', '18': '55', '19': '20', '20': '25', '21': '30', '22': '15', '23': '20', '24': '25', '25': '10', '26': '5', '41': '15', '45': '10', '46': '18', '47': '10', '48': '10', '49': '20', '50': '20', '51': '15', '54': '20', '73': '30', '74': '25', '76': '33', '93': '32', '94': '14', '98': '10', '99': '10', '100': '35', '102': '10', '103': '10', '104': '10', '105': '25', '107': '10', '108': '20', '123': '8', '124': '25', '125': '35', '126': '40', '127': '55', '128': '25', '129': '16', '130': '21', '131': '21', '132': '21', '133': '21', '134': '15', '135': '21', '136': '25', '137': '30', '138': '22', '139': '21', '140': '26', '141': '40', '142': '25', '143': '16', '144': '20', '145': '40', '146': '85', '147': '75', '148': '90', '149': '3', '150': '6', '151': '12', '152': '15', '153': '17', '154': '22', '155': '27', '156': '30', '157': '32', '158': '14', '159': '20', '160': '25', '161': '12', '162': '18', '163': '20', '164': '81', '165': '30', '166': '85', '167': '10', '168': '27', '169': '25', '170': '20', '171': '20', '172': '80', '173': '45', '174': '12', '175': '18', '176': '30', '177': '95', '178': '40', '179': '23', '180': '170', '181': '10', '182': '95', '183': '20', '184': '25', '185': '25', '186': '18', '187': '15', '188': '18', '189': '12', '190': '15', '191': '20', '192': '20', '193': '18', '194': '10', '195': '35', '196': '25', '197': '2', '198': '20', '900': '100', '901': '-100', '902': '25', '903': '5'}

hrcontrib = {}
segcontrib = {}
with open(path1,'rt',encoding="latin1") as csvfile:

	while(1):
		r = csv.reader(x.replace('\0', '') for x in csvfile)	
		print('FOR WHAT ITEM>')
		for_item = input()
		for_hr = -1
		for_item = str(for_item)
		contrib = 0
		total = 0
		flag = True
		for row in r:
			if(for_hr == -1):
				if(flag):
					flag = False
					continue
				
				if(len(row) < 1):
					continue
				row = row[0].split('\t')
				itemid = str(row[1])
				seg = str(row[5])
				seg = str(seg[0:2])
				if(itemid != for_item):
					price = int(prices_dic[itemid])
					total += price
					continue
				price = int(prices_dic[itemid])
				total += price
				contrib += price
				hr = row[3].split(' ')
				hr = hr[1].split(':')
				hr = hr[0]
				hr = hr.split(':')[0]
				if(hr not in hrcontrib):
					hrcontrib[hr] = price
				else:
					hrcontrib[hr] += price
				if seg not in segcontrib:
					segcontrib[seg] = price
				else:
					segcontrib[seg] += price
		
		print('%%% === ', (contrib/total)*100)
		print()
		print(str(hrcontrib))
		print()
		print(str(segcontrib))
		break

