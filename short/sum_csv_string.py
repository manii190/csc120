def sum_csv_string(csv_string):
    sum=0
    numbers=csv_string.split(',')
    for n in numbers:
        sum+=int(n)
    return sum