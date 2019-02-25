from datetime import date

#### unlucky_days - for loop vs. List comprehension ####

def unlucky_days_a(year):
    ''' for loop'''
    count = 0
    for month in range(1,13):
        if date(year,month,13).isoweekday() == 5:
            count += 1
    return count

def unlucky_days_b(year):
    ''' list comprehension '''

    return sum(date(year,month,13).isoweekday() == 5 for month in range(1,13))

print(unlucky_days_a(2019))
print(unlucky_days_b(2019))












def bday_of_week():

    return (date(y))




