with open("census.csv",'r',encoding = 'UTF-8') as census:
    with open('summary.csv','x',encoding='UTF-8') as output_file:
        for each_line in census:
            population = int(each_line.split(',')[7])
            if population >= 2000000:
                output_file.write(each_line)

