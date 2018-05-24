import csv
path1 = "./quantity_modified/quant_modified_octSales.csv"
path2 = "./quantity_modified/PLUS18quant_modified_octSales.csv"
path3 = "./quantity_modified/MINUS18quant_modified_octSales.csv"
#path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/augSales.csv"
#path2 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/modified_augSales.txt"


with open(path1,'rt',encoding="latin1") as csvfile, open(path2, 'w') as plus18, open(path3, 'w') as minus18:
        r = csv.reader((x.replace('\0', '') for x in csvfile), delimiter = '\t')
        # r = csv.reader(x.replace('\0', '') for x in csvfile)
        # r = csv.reader(delimiter = '\t')
        spamwriter_plus = csv.writer(plus18, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter_minus = csv.writer(minus18, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # input()

        flag = True
        for row in r:
                if(flag):
                        flag = False
                        spamwriter_plus.writerow(row)
                        spamwriter_minus.writerow(row)
                        continue

                date = row[3]
                day = date.split('-')
                day = day[2].split(' ')[0]
                day = int(day)
                if(day >= 18):
                    spamwriter_plus.writerow(row)
                else:
                    spamwriter_minus.writerow(row)
