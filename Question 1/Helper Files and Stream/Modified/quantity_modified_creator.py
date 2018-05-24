import csv

path1 = "./modified_decSales.csv"
path2 = "./quantity_modified/quant_modified_decSales.csv"
#path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/augSales.csv"
#path2 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/modified_augSales.txt"

missing = 0

minute_partition = 59

def getnexthour(hour):
	if(hour == 23):
		return str(0)
	return str(hour+1)

def gethour(x):
	x = (x.split(' '))[1]
	hour = x.split(':')[0]
	minute = x.split(':')[1]

	if(int(minute) > minute_partition):
		return getnexthour(int(hour))
	else:
		return int(hour)

with open(path1,'rt',encoding="latin1") as csvfile, open(path2, 'w', encoding="latin1") as modified:
	r = csv.reader(x.replace('\0', '') for x in csvfile)
	spamwriter = csv.writer(modified, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	flag = True
	for row in r:
		row = row[0].split('\t')
		#print(row)
		#input()
		if flag:
			spamwriter.writerow(row)
			flag = False
			continue
		quant = int(row[3])
		for i in range(quant):
			spamwriter.writerow(row)
		
	print(missing)
