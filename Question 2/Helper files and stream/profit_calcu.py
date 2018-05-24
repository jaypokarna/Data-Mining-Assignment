import csv
import itertools

## This file is the main driver code of the 2nd question.
## Data set has been taken directly from the data_sets.py file after manual checking.
## We calculate the loss incured due to the combo meals.
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

path2 ="./impdic.txt"
path1 = "./decSales.csv"
#path1 = "./quantity_modified/octPLUS18_nov_combined_quant_modified.csv"

namedic = {1: 'Samosa', 2: 'Veg Petty', 3: 'Paneer Petty', 4: 'Veg Burger', 5: 'Tea', 6: 'Coffee', 12: 'Pasta', 14: '5STAR', 15: 'DAIRY MILK@35', 16: 'PERK / DAIRY MILK', 18: 'DAIRY MILK SILKY', 19: '5* CRUNCHY', 20: '5*', 21: 'BOURNVILLE', 22: 'SNICKERS SNACK ', 23: 'MARS SNACK', 24: 'GALAXY MILK', 25: 'CHCO PIE', 26: 'CAKE SANDWICH', 41: 'MANGO DRINK', 45: 'BIS 50-50 @10', 46: 'BOURBONE@18', 47: 'BIS GD BUTTER @10', 48: 'BIS GD CASHEW @10', 49: 'BIS GD COCONUT@20', 50: 'BIS GD PISTA @20', 51: 'BIS JAM TREAT @15', 54: 'BIS PURE MAGIC@25', 73: 'COKE 600 ML ', 74: 'COKE CAN 300 ML', 76: 'COKE MIX 600 ML', 93: 'MAZZA PET 600 ML', 94: 'Mazza T.P', 98: 'BIKANO NAMKEEN', 99: 'PERFETTI HAPPYDENT', 100: 'DUKE WAFFY BISCUIT', 102: 'HR NAMKEEN @10', 103: 'BIS SF CREAM@10', 104: 'BIS SF DREAM @10', 105: 'DARK FANTASY@25', 107: 'BINOG CHIP @10', 108: 'BINOG CHIP @20', 123: 'Pastry', 124: 'Chese Burger', 125: 'Veg Pizza', 126: 'Chese Pizza', 127: 'Chicken Pizza', 128: 'Chese Toast', 129: 'Plain Dosa', 130: 'Masala Dosa', 131: 'Onion Masala Dosa', 132: 'Onion Uttapam', 133: 'Mix Uttapam', 134: 'Plain Maggi', 135: 'Fried Maggi', 136: 'Paneer Maggi', 137: 'Veg Chomin', 138: 'Paneer Franky', 139: 'Veg Rice', 140: 'Egg Rice', 141: 'Chicken Rice', 142: 'Chicken Sandwich', 143: 'OMLETE', 144: 'Dum Aloo', 145: 'Mutter Paneer', 146: 'Butter Chicken', 147: 'Chicken Curry', 148: 'Tandury Chicken 1/2', 149: 'Plain Roti', 150: 'Butter Roti', 151: 'Butter Naan', 152: 'Banana Shake', 153: 'Frit Shake', 154: 'Ice Cream Shake', 155: 'PEPSI 600ML', 156: 'DEW MIX', 157: 'SLICE 600ML', 158: 'SLICE TP', 159: 'MYCAN', 160: 'BHELPURI', 161: 'SINGLE SCOOP', 162: 'TROPICANA APPLE', 163: 'TROPICANA', 164: 'KADHAI PANEER', 165: 'FRANCH FRY', 166: 'CHILLI PANEER', 167: 'LITTLE HEARTS', 168: 'BRT CAKES', 169: 'PULPY ORANGE', 170: 'REAL ', 171: 'PULPY LEMON', 172: 'SOAN N PAPDI', 173: 'FUNGAMA', 174: 'JUMPIN MANGO', 175: 'BRT CAKES', 176: 'OREO', 177: 'CHILLY CHICKEN ', 178: 'CHI.PASTA', 179: 'MIX JUICE', 180: 'TANDOORI FULL', 181: 'BRT TIGER', 182: 'RED BULL', 183: 'WATER', 184: 'DAIRY MILK', 185: 'TREAT', 186: 'CHI SOOP', 187: 'CHIPS', 188: 'SAMOSA CHAT', 189: 'BOURBON', 190: 'OREO', 191: 'MCVITIES BIS.', 192: 'DAHI BHALLA', 193: 'COKE CAN', 194: 'COOKIES', 195: 'HOBNOBS', 196: 'DIGESTIVE', 197: 'PACKING CHARGE', 198: 'BOURBON 20', 900: 'FINE', 901: 'REIMBURSEMENT', 902: 'PANEER SANDWICH', 903: 'TIGER'}
{'HR NAMKEEN @10': 102, 'PULPY LEMON': 171, 'CHCO PIE': 25, 'FUNGAMA': 173, 'TREAT': 185, 'MAZZA PET 600 ML': 93, 'PULPY ORANGE': 169, 'Paneer Franky': 138, 'Chicken Pizza': 127, 'BIS GD CASHEW @10': 48, 'Plain Roti': 149, 'OREO': 190, '5STAR': 14, 'COKE 600 ML ': 73, 'Mix Uttapam': 133, 'MYCAN': 159, 'PERK / DAIRY MILK': 16, 'Masala Dosa': 130, 'Butter Chicken': 146, 'TROPICANA APPLE': 162, 'COOKIES': 194, 'DUKE WAFFY BISCUIT': 100, 'TROPICANA': 163, 'JUMPIN MANGO': 174, 'KADHAI PANEER': 164, 'WATER': 183, 'MANGO DRINK': 41, 'PERFETTI HAPPYDENT': 99, 'Tea': 5, 'BIS PURE MAGIC@25': 54, 'Samosa': 1, 'DEW MIX': 156, 'DAIRY MILK SILKY': 18, 'BIKANO NAMKEEN': 98, '5* CRUNCHY': 19, 'Tandury Chicken 1/2': 148, 'BINOG CHIP @20': 108, 'Chicken Rice': 141, 'Coffee': 6, 'SINGLE SCOOP': 161, 'CAKE SANDWICH': 26, 'Onion Masala Dosa': 131, 'CHILLY CHICKEN ': 177, 'COKE MIX 600 ML': 76, 'BIS JAM TREAT @15': 51, 'REIMBURSEMENT': 901, 'MCVITIES BIS.': 191, 'Veg Pizza': 125, 'DAHI BHALLA': 192, 'Veg Petty': 2, '5*': 20, 'BINOG CHIP @10': 107, 'Onion Uttapam': 132, 'PANEER SANDWICH': 902, 'Frit Shake': 153, 'SLICE 600ML': 157, 'BIS GD COCONUT@20': 49, 'BIS SF DREAM @10': 104, 'Plain Dosa': 129, 'GALAXY MILK': 24, 'Butter Naan': 151, 'Fried Maggi': 135, 'Chese Burger': 124, 'DIGESTIVE': 196, 'Butter Roti': 150, 'REAL ': 170, 'Chese Pizza': 126, 'Chicken Sandwich': 142, 'BOURBON 20': 198, 'Chicken Curry': 147, 'Banana Shake': 152, 'PACKING CHARGE': 197, 'CHILLI PANEER': 166, 'Veg Rice': 139, 'Dum Aloo': 144, 'HOBNOBS': 195, 'SOAN N PAPDI': 172, 'TIGER': 903, 'BOURNVILLE': 21, 'OMLETE': 143, 'MARS SNACK': 23, 'TANDOORI FULL': 180, 'Plain Maggi': 134, 'DARK FANTASY@25': 105, 'BIS SF CREAM@10': 103, 'Paneer Maggi': 136, 'SLICE TP': 158, 'BIS GD PISTA @20': 50, 'Paneer Petty': 3, 'Veg Burger': 4, 'Mutter Paneer': 145, 'RED BULL': 182, 'PEPSI 600ML': 155, 'BHELPURI': 160, 'BRT TIGER': 181, 'MIX JUICE': 179, 'FRANCH FRY': 165, 'Mazza T.P': 94, 'BIS 50-50 @10': 45, 'BOURBON': 189, 'CHI SOOP': 186, 'CHI.PASTA': 178, 'COKE CAN 300 ML': 74, 'FINE': 900, 'Veg Chomin': 137, 'Ice Cream Shake': 154, 'Pasta': 12, 'SNICKERS SNACK ': 22, 'Pastry': 123, 'COKE CAN': 193, 'SAMOSA CHAT': 188, 'Chese Toast': 128, 'BOURBONE@18': 46, 'DAIRY MILK@35': 15, 'BRT CAKES': 175, 'DAIRY MILK': 184, 'BIS GD BUTTER @10': 47, 'LITTLE HEARTS': 167, 'CHIPS': 187, 'Egg Rice': 140}

nametoid = {'HR NAMKEEN @10': 102, 'PULPY LEMON': 171, 'CHCO PIE': 25, 'FUNGAMA': 173, 'TREAT': 185, 'MAZZA PET 600 ML': 93, 'PULPY ORANGE': 169, 'Paneer Franky': 138, 'Chicken Pizza': 127, 'BIS GD CASHEW @10': 48, 'Plain Roti': 149, 'OREO': 190, '5STAR': 14, 'COKE 600 ML ': 73, 'Mix Uttapam': 133, 'MYCAN': 159, 'PERK / DAIRY MILK': 16, 'Masala Dosa': 130, 'Butter Chicken': 146, 'TROPICANA APPLE': 162, 'COOKIES': 194, 'DUKE WAFFY BISCUIT': 100, 'TROPICANA': 163, 'JUMPIN MANGO': 174, 'KADHAI PANEER': 164, 'WATER': 183, 'MANGO DRINK': 41, 'PERFETTI HAPPYDENT': 99, 'Tea': 5, 'BIS PURE MAGIC@25': 54, 'Samosa': 1, 'DEW MIX': 156, 'DAIRY MILK SILKY': 18, 'BIKANO NAMKEEN': 98, '5* CRUNCHY': 19, 'Tandury Chicken 1/2': 148, 'BINOG CHIP @20': 108, 'Chicken Rice': 141, 'Coffee': 6, 'SINGLE SCOOP': 161, 'CAKE SANDWICH': 26, 'Onion Masala Dosa': 131, 'CHILLY CHICKEN ': 177, 'COKE MIX 600 ML': 76, 'BIS JAM TREAT @15': 51, 'REIMBURSEMENT': 901, 'MCVITIES BIS.': 191, 'Veg Pizza': 125, 'DAHI BHALLA': 192, 'Veg Petty': 2, '5*': 20, 'BINOG CHIP @10': 107, 'Onion Uttapam': 132, 'PANEER SANDWICH': 902, 'Frit Shake': 153, 'SLICE 600ML': 157, 'BIS GD COCONUT@20': 49, 'BIS SF DREAM @10': 104, 'Plain Dosa': 129, 'GALAXY MILK': 24, 'Butter Naan': 151, 'Fried Maggi': 135, 'Chese Burger': 124, 'DIGESTIVE': 196, 'Butter Roti': 150, 'REAL ': 170, 'Chese Pizza': 126, 'Chicken Sandwich': 142, 'BOURBON 20': 198, 'Chicken Curry': 147, 'Banana Shake': 152, 'PACKING CHARGE': 197, 'CHILLI PANEER': 166, 'Veg Rice': 139, 'Dum Aloo': 144, 'HOBNOBS': 195, 'SOAN N PAPDI': 172, 'TIGER': 903, 'BOURNVILLE': 21, 'OMLETE': 143, 'MARS SNACK': 23, 'TANDOORI FULL': 180, 'Plain Maggi': 134, 'DARK FANTASY@25': 105, 'BIS SF CREAM@10': 103, 'Paneer Maggi': 136, 'SLICE TP': 158, 'BIS GD PISTA @20': 50, 'Paneer Petty': 3, 'Veg Burger': 4, 'Mutter Paneer': 145, 'RED BULL': 182, 'PEPSI 600ML': 155, 'BHELPURI': 160, 'BRT TIGER': 181, 'MIX JUICE': 179, 'FRANCH FRY': 165, 'Mazza T.P': 94, 'BIS 50-50 @10': 45, 'BOURBON': 189, 'CHI SOOP': 186, 'CHI.PASTA': 178, 'COKE CAN 300 ML': 74, 'FINE': 900, 'Veg Chomin': 137, 'Ice Cream Shake': 154, 'Pasta': 12, 'SNICKERS SNACK ': 22, 'Pastry': 123, 'COKE CAN': 193, 'SAMOSA CHAT': 188, 'Chese Toast': 128, 'BOURBONE@18': 46, 'DAIRY MILK@35': 15, 'BRT CAKES': 175, 'DAIRY MILK': 184, 'BIS GD BUTTER @10': 47, 'LITTLE HEARTS': 167, 'CHIPS': 187, 'Egg Rice': 140}

decprice = {1: 7, 2: 8, 3: 12, 4: 21, 5: 8, 6: 10, 12: 30, 14: 10, 15: 35, 16: 5, 18: 55, 19: 20, 20: 25, 21: 30, 22: 15, 23: 20, 24: 25, 25: 10, 26: 5, 41: 15, 45: 10, 46: 18, 47: 10, 48: 10, 49: 20, 50: 20, 51: 15, 54: 20, 73: 30, 74: 25, 76: 33, 93: 32, 94: 14, 98: 10, 99: 10, 100: 35, 102: 10, 103: 10, 104: 10, 105: 25, 107: 10, 108: 20, 123: 8, 124: 25, 125: 35, 126: 40, 127: 55, 128: 25, 129: 16, 130: 21, 131: 21, 132: 21, 133: 21, 134: 15, 135: 21, 136: 25, 137: 30, 138: 22, 139: 21, 140: 26, 141: 40, 142: 25, 143: 16, 144: 20, 145: 40, 146: 85, 147: 75, 148: 90, 149: 3, 150: 6, 151: 12, 152: 15, 153: 17, 154: 22, 155: 27, 156: 30, 157: 32, 158: 14, 159: 20, 160: 25, 161: 12, 162: 18, 163: 20, 164: 81, 165: 30, 166: 85, 167: 10, 168: 27, 169: 25, 170: 20, 171: 20, 172: 80, 173: 45, 174: 12, 175: 18, 176: 30, 177: 95, 178: 40, 179: 23, 180: 170, 181: 10, 182: 95, 183: 20, 184: 25, 185: 25, 186: 18, 187: 15, 188: 18, 189: 12, 190: 15, 191: 20, 192: 20, 193: 18, 194: 10, 195: 35, 196: 25, 197: 2, 198: 20, 900: 100, 901: -100, 902: 25, 903: 5}

data = [['Plain Maggi', 'CAKE SANDWICH'], ['Plain Maggi', 'Pastry'], ['Plain Maggi', 'BIS 50-50 @10'], ['Plain Maggi', 'LITTLE HEARTS'], ['Plain Maggi', 'SINGLE SCOOP'], ['Plain Maggi', 'Plain Dosa'], ['Plain Maggi', 'CHI SOOP'], ['Plain Maggi', 'BOURBONE@18'], ['Plain Maggi', 'BRT CAKES'],  ['Plain Maggi', 'TROPICANA'], ['Plain Maggi', 'MYCAN'], ['Plain Maggi', 'Mix Uttapam'], ['Plain Maggi', 'Onion Uttapam'], ['Plain Maggi', 'Onion Masala Dosa'], ['Plain Maggi', 'Masala Dosa'], ['Plain Maggi', 'Veg Rice'], ['Plain Maggi', 'Paneer Franky'],['Veg Rice', 'Plain Dosa'], ['Ice Cream Shake', 'Plain Maggi'], ['Chese Toast', 'Plain Maggi'], ['Plain Maggi', 'DARK FANTASY@25'], ['Plain Maggi', 'Chese Burger'], ['Plain Maggi', 'BHELPURI'], ['Plain Maggi', 'Egg Rice'], ['Veg Rice', 'MYCAN'], ['Veg Rice', 'TROPICANA'], ['Fried Maggi', 'Veg Rice'],['Fried Maggi', 'Onion Masala Dosa'], ['Masala Dosa', 'Veg Rice'], ['Veg Rice', 'Mix Uttapam'], ['Veg Rice', 'Onion Uttapam'], ['Butter Naan', 'DEW MIX'], ['Veg Rice', 'Onion Masala Dosa'], ['Plain Maggi', 'PEPSI 600ML'], ['Paneer Franky', 'Veg Rice'], ['Paneer Franky', 'Onion Masala Dosa'], ['Ice Cream Shake', 'Onion Masala Dosa'], ['Ice Cream Shake', 'Veg Rice'], ['Butter Naan', 'SLICE 600ML'], ['Egg Rice', 'BRT CAKES'], ['Veg Rice', 'Paneer Maggi'], ['Chese Toast', 'Onion Masala Dosa'], ['Chese Toast', 'Veg Rice'], ['Onion Masala Dosa', 'Paneer Maggi'], ['Chicken Sandwich', 'Veg Rice'], ['Chese Burger', 'Onion Masala Dosa'], ['Egg Rice', '5* CRUNCHY'], ['Egg Rice', 'TROPICANA'], ['Fried Maggi', 'Egg Rice'], ['Masala Dosa', 'Egg Rice'], ['Egg Rice', 'Mix Uttapam'], ['Egg Rice', 'Onion Uttapam'], ['Paneer Franky', 'Egg Rice'], ['Ice Cream Shake', 'Egg Rice'], ['PEPSI 600ML', 'Onion Masala Dosa'], ['PEPSI 600ML', 'Veg Rice'], ['Chicken Sandwich', 'Egg Rice'], ['Egg Rice', 'Paneer Maggi'], ['Chese Toast', 'Egg Rice'], ['DEW MIX', 'Veg Rice'],['PEPSI 600ML', 'Egg Rice'], ['Plain Maggi', 'Chicken Rice'], ['Chicken Rice', 'PULPY LEMON'],['Fried Maggi', 'Chicken Rice'], ['Masala Dosa', 'Chicken Rice'], ['Paneer Franky', 'Chicken Rice'], ['Ice Cream Shake', 'Chicken Rice'], ['Chicken Sandwich', 'Chicken Rice'], ['Chicken Rice', 'Paneer Maggi'],['PEPSI 600ML', 'Chicken Rice'], ['Butter Naan', 'KADHAI PANEER'], ['Butter Naan', 'Butter Chicken'],['Plain Maggi', 'Butter Chicken'], ['Plain Maggi', 'CHILLI PANEER'], ['CAKE SANDWICH', 'Butter Chicken', 'Butter Naan'],['Pastry', 'Butter Chicken', 'Butter Naan'], ['Plain Maggi', 'Tandury Chicken 1/2'], ['Butter Chicken', 'Veg Rice'], ['Butter Chicken', 'Onion Masala Dosa'], ['Butter Naan', 'CHILLY CHICKEN '],['Butter Chicken', 'Egg Rice'], ['Tandury Chicken 1/2', 'Veg Rice'], ['Tandury Chicken 1/2', 'Onion Masala Dosa'], ['Plain Maggi', 'Butter Chicken', 'Butter Naan'], ['Plain Dosa', 'Butter Chicken', 'Butter Naan'],['Tandury Chicken 1/2', 'Egg Rice'],['MYCAN', 'Butter Chicken', 'Butter Naan'], ['Veg Rice', 'Butter Chicken', 'Butter Naan'], ['Masala Dosa', 'Butter Chicken', 'Butter Naan'],['Mix Uttapam', 'Butter Chicken', 'Butter Naan'], ['Fried Maggi', 'Butter Chicken', 'Butter Naan'], ['Ice Cream Shake', 'Butter Chicken', 'Butter Naan'], ['Paneer Franky', 'Butter Chicken', 'Butter Naan'], ['Chicken Sandwich', 'Butter Chicken', 'Butter Naan'],['Chese Toast', 'Butter Chicken', 'Butter Naan'], ['DIGESTIVE', 'Butter Chicken', 'Butter Naan'], ['Paneer Maggi', 'Butter Chicken', 'Butter Naan'], ['Chese Burger', 'Butter Chicken', 'Butter Naan'],['Egg Rice', 'Butter Chicken', 'Butter Naan'],['PEPSI 600ML', 'Butter Chicken', 'Butter Naan'], ['Butter Chicken', 'Chicken Rice'], ['Chicken Rice', 'CHILLI PANEER'],['Pasta', 'Butter Chicken', 'Butter Naan'],['COKE MIX 600 ML', 'Butter Chicken', 'Butter Naan'], ['Tandury Chicken 1/2', 'Chicken Rice'], ['DEW MIX', 'Tandury Chicken 1/2', 'Butter Naan'], ['SLICE 600ML', 'Tandury Chicken 1/2', 'Butter Naan'], ['Chicken Rice', 'CHILLY CHICKEN '], ['Chicken Rice', 'Butter Chicken', 'Butter Naan'], ['CHI.PASTA', 'Butter Chicken', 'Butter Naan'],['KADHAI PANEER', 'Butter Chicken', 'Butter Naan'], ['CHILLI PANEER', 'Butter Chicken', 'Butter Naan'],['PEPSI 600ML', 'SINGLE SCOOP'], ['PEPSI 600ML', 'OREO'], ['PEPSI 600ML', 'BRT CAKES'],['PEPSI 600ML', 'Mix Uttapam'], ['Masala Dosa', 'PEPSI 600ML'], ['Ice Cream Shake', 'PEPSI 600ML'], ['PEPSI 600ML', 'Paneer Maggi'], ['PEPSI 600ML', 'BHELPURI'], ['Chese Toast', 'PEPSI 600ML'],['CAKE SANDWICH', 'DAIRY MILK SILKY'],['COKE CAN 300 ML', 'DAIRY MILK SILKY'],['Pasta', 'DAIRY MILK SILKY'], ['COKE MIX 600 ML', 'DAIRY MILK SILKY'], ['PEPSI 600ML', 'KADHAI PANEER'], ['Butter Chicken', 'PEPSI 600ML'], ['PEPSI 600ML', 'Tandury Chicken 1/2'],['Veg Petty', 'PERK / DAIRY MILK'], ['Veg Petty', '5STAR'], ['Veg Petty', 'OREO'],['Veg Petty', '5* CRUNCHY'], ['COKE CAN 300 ML', 'CAKE SANDWICH'], ['Veg Petty', '5*'], ['COKE CAN 300 ML', 'BIS 50-50 @10'], ['COKE CAN 300 ML', 'CHCO PIE'], ['COKE CAN 300 ML', 'BIS GD CASHEW @10'], ['CAKE SANDWICH', 'MAZZA PET 600 ML'], ['Veg Petty', 'Pasta'], ['Veg Petty', 'BOURNVILLE'], ['COKE CAN 300 ML', 'BIS JAM TREAT @15'], ['DAIRY MILK@35', 'CAKE SANDWICH'], ['SNICKERS SNACK ', 'COKE CAN 300 ML'], ['COKE CAN 300 ML', 'SNICKERS SNACK '], ['BINOG CHIP @10', 'MAZZA PET 600 ML'], ['MAZZA PET 600 ML', 'BIS GD CASHEW @10'], ['DAIRY MILK@35', 'Samosa'], ['MAZZA PET 600 ML', 'CHCO PIE'], ['COKE CAN 300 ML', 'BOURBONE@18'], ['Veg Petty', 'DAIRY MILK@35'],['COKE CAN 300 ML', 'BIS GD PISTA @20'], ['DAIRY MILK@35', 'BIS GD CASHEW @10'], ['DAIRY MILK@35', 'BIS 50-50 @10'], ['BINOG CHIP @10', 'DAIRY MILK@35'], ['BOURBON 20', 'BHELPURI'],['DAIRY MILK@35', 'BIS JAM TREAT @15'], ['MAZZA PET 600 ML', 'BOURBONE@18'], ['Chese Burger', 'COKE CAN 300 ML'], ['BINOG CHIP @20', 'MAZZA PET 600 ML'], ['DAIRY MILK@35', 'BOURBONE@18'], ['DAIRY MILK@35', 'BRT CAKES'], ['COKE CAN 300 ML', 'BOURNVILLE'], ['DAIRY MILK@35', 'BIS GD PISTA @20'], ['Pasta', 'COKE CAN 300 ML'], ['DAIRY MILK@35', 'Veg Burger'], ['Chese Toast', 'MAZZA PET 600 ML'], ['MAZZA PET 600 ML', 'DARK FANTASY@25'], ['Chese Burger', 'MAZZA PET 600 ML'], ['COKE CAN 300 ML', 'DUKE WAFFY BISCUIT'], ['DAIRY MILK@35', 'COKE CAN 300 ML'], ['Chese Toast', 'DAIRY MILK@35'], ['MAZZA PET 600 ML', 'BOURNVILLE'],['Pasta', 'DAIRY MILK@35'], ['MAZZA PET 600 ML', 'DUKE WAFFY BISCUIT'], ['COKE MIX 600 ML', 'DAIRY MILK@35'], ['DAIRY MILK@35', 'HOBNOBS']]

datanew = []

thedic = {}
hrcontrib = {}
segcontrib = {}

def intval(x):
	return nametoid[x]

def priceset(x):
	p = 0
	for i in x:
		p += decprice[int(i)]
	return p
	
def countof(x, val):
	ret = 100000000
	for i in x:
		to = 0
		for j in val:
			if i == j:
				to += 1
		ret = min(to, ret)
	return ret
		

def priceof(x):
	ret = 0
	for i in x:
		ret += int(decprice[int(i)])
	return ret	
		
def getmaxloss(val, sz):
	loss = -100
	ret = None
	for i in findsubsets(val, sz):
		i = set(i)
		if i not in datanew or len(i) != sz:
			continue
		if priceof(i) > loss:
			ret = set(i)
			loss = priceof(set(i))
	return ret
	
with open(path1,'rt') as csvfile, open(path2, 'w') as wf:
	r = csv.reader(x.replace('\0', '') for x in csvfile)	
	flag = True
	tr = 0
	for row in r:
		if(flag):
			flag = False
			continue
		quant = int(row[3]) 
		tup = (row[1], row[5])
		if tup not in thedic:
			thedic[tup] = [row[2]]
			for j in range(quant-1):
				thedic[tup].append(row[2])
		else:
			for j in range(quant):
				thedic[tup].append(row[2])

		price = decprice[int(row[2])]
		tr += quant*price
		
	newrev = 0
	for itemset in data:
		x = [str(nametoid[i]) for i in itemset]
		datanew.append(set(x))
		
	wf.write(str(datanew))
	
	trfinal = 0
	
	ans = 0
	for key, val in thedic.items():
		out=False
		
		x4 = getmaxloss(val, 4)
		# for x4 in findsubsets(val, 4):
		if(x4 is not None):
			if x4 in datanew and len(x4) == 4:
				c = countof(x4, val)
				for j in range(c):	
					for i in x4:
						val.remove(i)
				for i in val:
					trfinal += decprice[int(i)]
				for i in x4:
					trfinal += decprice[int(i)]*(1-.2/4)*c
					# trfinal += decprice[int(i)]*c
				out = True
				# break
				
		if(out):
			continue
		
		x3 = getmaxloss(val, 3)
		if x3 is not None:
		# for x3 in findsubsets(val, 3):
			x3 = set(x3)
			if x3 in datanew and len(x3) == 3:
				c = countof(x3, val)
				for j in range(c):
					for i in x3:
						val.remove(i)	
				for i in val:
					trfinal += decprice[int(i)]

				for i in x3:
					trfinal += decprice[int(i)]*(1-.2/3)*c
					# trfinal += decprice[int(i)]*c
				out = True
				# break

		
		if out:
			continue
		
		x2 = getmaxloss(val, 2)
		if x2 is not None:
		# for x2 in findsubsets(val, 2):
			x2 = set(x2)
			if x2 in datanew and len(x2) == 2:
				c = countof(x2, val)
				# print(val)
				for j in range(c):
					for i in x2:	
						val.remove(i)
				for i in val:
					trfinal += decprice[int(i)]
				for i in x2:
					trfinal += decprice[int(i)]*c*(0.9)
					# trfinal += decprice[int(i)]*c
				out = True
				# break
		
		if out:
			continue

		for i in val:
			trfinal += decprice[int(i)]
			
	print("Number of combo meals offered are :" + (str)(len(datanew)))
	print("Loss incured is:" + (str)((float)(tr-trfinal)*100/tr))
