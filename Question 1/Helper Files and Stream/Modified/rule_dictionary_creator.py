import csv


path1 = "./apriori_q1_model.csv"
# path2 = "./profit_decSales.csv"
#path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/augSales.csv"
#path2 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/modified_augSales.txt"


total_revenue = 0
d = {}

with open(path1,'rt',encoding="latin1") as csvfile:
	r = csv.reader(x.replace('\0', '') for x in csvfile)
	# spamwriter = csv.writer(modified, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	flag = True
	for row in r:
		row = row[0].split('\t')
		if(flag):
			flag = False
			continue
			
		# print(row)
		# input()
		if(row[0] not in d):
			d[row[0]] = [(row[1], row[3])]
		else:
			d[row[0]].append((row[1], row[3]))
	print(d)
