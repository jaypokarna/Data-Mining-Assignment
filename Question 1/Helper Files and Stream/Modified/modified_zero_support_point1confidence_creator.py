import csv
path1 = "./zero_support_point1confidence.csv"
path2 = "./modified_zero_support_point1confidence.csv"
path3 = "./itemid_hour_group_dict.txt"
#path1 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/augSales.csv"
#path2 = "E:/ACADEMICS/Data Mining/Assignment/Dataset for DM Assignment/Modified/modified_augSales.txt"

missing = 0

d = {}

def remove_space(x):
        return x.split(' ')[0]

with open(path1,'rt',encoding="latin1") as csvfile, open(path2, 'w') as modified, open(path3, 'w') as dictionary:
        r = csv.reader((x.replace('\0', '') for x in csvfile), delimiter = '\t')
        # r = csv.reader(x.replace('\0', '') for x in csvfile)
        # r = csv.reader(delimiter = '\t')
        spamwriter = csv.writer(modified, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # input()
        count = 0
        flag = True
        for row in r:
                count += 1
                # print(row)
                # input()
                if(flag):
                        flag = False
                        spamwriter.writerow(row)
                        continue
                if('and' not in row[1]):
                        continue
                if(('hour' not in row[1]) or ('student_group' not in row[1])):
                        continue
                        
                itemid = row[0]
                itemid = itemid.split('ItemID_')[1]
                hour = 1
                group = 1
                temp = row[1].split('and')
                hour = temp[1]
                group = temp[0]
                if('hour' in temp[0]):
                        hour = temp[0]
                        group = temp[1]
                hour = hour.split('hour_')[1]
                group = group.split('group_')[1]
                if(itemid not in d):
                        d[itemid] = [(remove_space(hour), remove_space(group))]
                else:
                        d[itemid].append((remove_space(hour), remove_space(group)))
                        
                spamwriter.writerow(row)
                
        print(missing)
        dictionary.write(str(d))
