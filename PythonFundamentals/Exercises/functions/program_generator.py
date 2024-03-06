import random

subjects = ['БГ', 'АЕ', 'РЕ', 'МАТ', 'ГО', 'ФВС', 'ЧК']


def call_function():
    first = random.choice(subjects)
    second = random.choice(subjects)
    third = random.choice(subjects)
    forth = random.choice(subjects)
    fifth = random.choice(subjects)
    sixth = random.choice(subjects)
    seventh = random.choice(subjects)
    days_of_week = first, second, third, forth, fifth, sixth, seventh
    form_schedule(days_of_week)

def form_schedule(days_of_week: list):
    if counter == 1:
        print('Monday', days_of_week,end=' ')
        print()
    if counter == 2:
        print('Tuesday', days_of_week,end=' ')
        print()
    if counter == 3:
        print('Wednesday', days_of_week,end=' ')
        print()
    if counter == 4:
        print('Thursday', days_of_week,end=' ')
        print()
    if counter == 5:

        print('Freeday ( )')


counter = 1
while counter < 6:
    call_function()
    counter += 1


