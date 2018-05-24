import csv
import pdb

## This file generates the frequent itemsets such that at least item in them, is less than a threshold.
## This threshold is varied so as to get all of the possible item sets under a maximum threshold.
av = []
arr = []
rate = []
count = []
num = 906
minrate = 1.9
minrate = (float)(minrate)
prices = {'1': '7', '2': '8', '3': '12', '4': '21', '5': '8', '6': '10', '12': '30', '14': '10', '15': '35', '16': '5', '18': '55', '19': '20', '20': '25', '21': '30', '22': '15', '23': '20', '24': '25', '25': '10', '26': '5', '41': '15', '45': '10', '46': '18', '47': '10', '48': '10', '49': '20', '50': '20', '51': '15', '54': '20', '73': '30', '74': '25', '76': '33', '93': '32', '94': '14', '98': '10', '99': '10', '100': '35', '102': '10', '103': '10', '104': '10', '105': '25', '107': '10', '108': '20', '123': '8', '124': '25', '125': '35', '126': '40', '127': '55', '128': '25', '129': '16', '130': '21', '131': '21', '132': '21', '133': '21', '134': '15', '135': '21', '136': '25', '137': '30', '138': '22', '139': '21', '140': '26', '141': '40', '142': '25', '143': '16', '144': '20', '145': '40', '146': '85', '147': '75', '148': '90', '149': '3', '150': '6', '151': '12', '152': '15', '153': '17', '154': '22', '155': '27', '156': '30', '157': '32', '158': '14', '159': '20', '160': '25', '161': '12', '162': '18', '163': '20', '164': '81', '165': '30', '166': '85', '167': '10', '168': '27', '169': '25', '170': '20', '171': '20', '172': '80', '173': '45', '174': '12', '175': '18', '176': '30', '177': '95', '178': '40', '179': '23', '180': '170', '181': '10', '182': '95', '183': '20', '184': '25', '185': '25', '186': '18', '187': '15', '188': '18', '189': '12', '190': '15', '191': '20', '192': '20', '193': '18', '194': '10', '195': '35', '196': '25', '197': '2', '198': '20', '900': '100', '901': '-100', '902': '25', '903': '5'}

def key1(item):
	return len(item)

def key2(item):
	t1 = (str)(reverse[item[0]])
	t2 = (str)(reverse[item[1]])
	if(len(item)==2):
		return (int)(prices[t1])+ (int)(prices[t2])
	elif(len(item)==3):
		t3 = (str)(reverse[item[2]])
		return (int)(prices[t1])+ (int)(prices[t2]) + (int)(prices[t3])

def key3(item):
	t1 = (int)(reverse[item[0]])
	t2 = (int)(reverse[item[1]])
	if(len(item)==2):
		return min(av[t1],av[t2])
	elif(len(item)==3):
		t3 = (int)(reverse[item[2]])
		return min(av[t1],av[t2],av[t3])
	
for i in range(0,num):
	rate.append((int)(0))
	count.append((int)(0))	

with open('augSales.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rate[(int)(row[1])] += (int)(row[7])
		count[(int)(row[1])] = (int)(count[(int)(row[1])])+1

with open('sepSales.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rate[(int)(row[1])] += (int)(row[7])
		count[(int)(row[1])] = (int)(count[(int)(row[1])])+1
with open('octSales.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rate[(int)(row[1])] += (int)(row[7])
		count[(int)(row[1])] = (int)(count[(int)(row[1])])+1
with open('novSales.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rate[(int)(row[1])] += (int)(row[7])
		count[(int)(row[1])] = (int)(count[(int)(row[1])])+1

for i in range(0,num):
	if(count[i]>0):
		av.append((float)(rate[i])/(float)(count[i]))
	else:
		av.append((int)(-1))

file_obj = open("rules_Q2.txt","r")
x =  file_obj.readlines()

for i in range(0,len(x)):
	index = x[i].find("and")
	if(index!=-1):
		x[i] = x[i][:index-1] +"\t"+x[i][index+4:]
	if(x[i].count("and")==0):
		z =  x[i].split("\t")
	for j in range(0,len(z)):
		if(z[j].find("item_") != -1):
			z[j] = z[j][5:]
		else:
			break
	t = z[len(z)-1]
	z[len(z)-1] = t[:t.find("\r")]
	x[i] = z

names = {}
reverse = {}
decprice = {}
with open("monthwisePriceList.csv",'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		itemid = (int)(row[0])
		itemname = row[1]
		names[itemid] = itemname
		reverse[itemname] = itemid
		decprice[itemid] = (int)(row[6])
prev = []
z = []

while(minrate<5):
	new_sets = []
	print (str)(minrate) + ":"
	for i in range(0,len(x)):
		p = x[i]
		p[0] = (int)(p[0])
		p[1] = (int)(p[1])
		if(len(p)==4):
			if(av[p[0]] < minrate or av[p[1]] <minrate):
				new_sets.append(p)
		
		else:
			p[2] = (int)(p[2])
			if(av[p[0]]<minrate or av[p[1]]<minrate or av[p[2]]<minrate):
				new_sets.append(p)
	for i in range(0,len(new_sets)):
		p = new_sets[i]
		tre = []
		if(len(p)==4):
			p[0] = names[p[0]]
			p[1] = names[p[1]]
			tre.append(p[0])
			tre.append(p[1])
		else:
			p[0] = names[p[0]]
			p[1] = names[p[1]]
			p[2] = names[p[2]]
			tre.append(p[0])
			tre.append(p[1])
			tre.append(p[2])
		new_sets[i] = tre
	for i in range(0,len(x)):
		try:
			x[i][0] = reverse[x[i][0]]
			x[i][1] = reverse[x[i][1]]
			x[i][2] = reverse[x[i][2]]
		except:pass
	minrate = minrate+0.1
	z = [item for item in new_sets if item not in prev]
	for i in range(0,len(z)-2):
		for j in range(i+1,len(z)):
			try:
				t = z[i]
				s = z[j]
				if(len(t)==len(s)):
					if(len(set(t)&set(s))==len(s)):
						z.remove(s)
			except:pass	
	z = sorted(z,key=key1,reverse=True)
	z = sorted(z,key=key2)
	z = sorted(z,key=key3)
	print z
	prev = new_sets
