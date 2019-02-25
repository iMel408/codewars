
########## unlucky_days ##########
from datetime import date

# for loop version
def unlucky_days_a(year):
    '''returns the number of Friday the 13th's in a given year '''
    count = 0
    for month in range(1,13):
        if date(year,month,13).isoweekday() == 5:
            count += 1

    return count


# list comprehension version
def unlucky_days_b(year):
    """returns the number of Friday the 13th's in a given year """

    return sum(date(year,month,13).isoweekday() == 5 for month in range(1,13))


print(unlucky_days_a(2019))
print(unlucky_days_b(2019))

########## duplicate_encode##########

# for loop version
def duplicate_encode_a(word):
    ''' create new string that converts char to ")" if it appears more than once else convert to "(" '''

    dict = {char: sum([1 for char2 in word.lower() if char2 == char]) for char in word.lower()}
    result = []
    for char in word.lower():
        if dict[char] == 1:
            result.append('(')
        else:
            result.append(')')

    return ''.join(result)

print(duplicate_encode_a('Melissa maria'))

# list comprehension version
def duplicate_encode_b(word):
    ''' create new string that converts char to ")" if it appears more than once else convert to "(" '''

    return ''.join(['(' if word.lower().count(char) == 1 else ')' for char in word.lower()])

print(duplicate_encode_a('Melissa maria'))