import datetime

print('введите Имя ')
user_name = input()
# print(user_name.isdigit())
print('введите Фамилию')
user_lastname = input()
print('Привет, ', user_name, " ", user_lastname, "введите сегодняшнюю дату")
day_today = int(input('день'))
month_today = int(input('месяц'))
year_today = int(input('год'))

print('сегодня :', day_today, month_today, year_today)

print('введите вашу дату рождения')
day_user = int(input('день'))
month_user = int(input('месяц'))
year_user = int(input('год'))
print('вы родились:', day_user, month_user, year_user)

print('Вам :', (year_today - year_user), 'лет')
month_user_life = 0
i = 0
j = year_user
k = 0
while j != year_today:

    i += 1
    if i == 30:
        month_user_life += 1
        i = 0
        k += 1
    if k == 12:
        k = 0
        j += 1
print('Вам :', month_user_life, 'месяцев')

day_lessons = 31
month_lessons = 1
year_lessons = 2019

days_studing = 0
month_studing = 0
while days_studing <= day_today and month_studing != month_today:
    days_studing += 1
print('вы учитесь ', days_studing, ' дней')
