import csv
 
delimit = '\t'

with open('group.csv','r') as csv_file:
    csv_read = csv.reader(csv_file)
    
    with open('new_group.csv', 'w') as new_file:
        csv_write = csv.writer(new_file, delimiter=delimit)
        
        # Skips one line
        for line in csv_read:
            csv_write.writerow(line)
    
# Dict facilita a compreensão do código, 
# pois usa key names ['nome','id'] , invés de índices [0,1,2..]
with open('new_group.csv','r') as csv_file:
    csv_read = csv.DictReader(csv_file, delimiter=delimit)
    
    with open('dic_group.csv','w') as new_file:
        # Não são índices quaisquer, utilizar os padrões
        fdnames = ['group_name', 'group_owner','group_code']
        csv_write = csv.DictWriter(new_file, fieldnames=fdnames)    
    
        csv_write.writeheader()

        for line in csv_read:
            del line['group_code']
            csv_write.writerow(line)

