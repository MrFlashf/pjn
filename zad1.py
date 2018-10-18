import re

name_correct = False
name_message = 'Podaj imie:\n'
while(not name_correct):
    name = input(name_message)
    if (re.match('[A-Z].*', name) is not None):
        name_correct = True
    else:
        name_message = 'Imie musi zaczynać się wielką literą:\n'

surname_correct = False
surname_message = 'Podaj nazwisko\n'
while(not surname_correct):
    surname = input(surname_message)
    if (re.match('[A-Z].*', surname) is not None):
        surname_correct = True
    else:
        surname_message = 'Nazwisko musi zaczynać się wielką literą:\n'

city_correct = False
city_message = 'Podaj miasto\n'
while(not city_correct):
    city = input(city_message)
    if (re.match('[A-Z].*', city) is not None):
        city_correct = True
    else:
        city_message = 'Miasto musi zaczynać się wielką literą:\n'

phone_correct = False
phone_message = 'Podaj nr tel\n'
while(not phone_correct):
    phone = input(phone_message)
    if (re.match('\([0-9]{2}\) [0-9]{3}-[0-9]{2}-[0-9]{2}', phone) is not None):
        phone_correct = True
    else:
        phone_message = 'Nr tel. musi być w formacie (61) 222-45-56\n'

post_code_correct = False
post_code_message = 'Podaj kod pocztowy\n'
while(not post_code_correct):
    post_code = input(post_code_message)
    if (re.match('[0-9]{2}-[0-9]{3}', post_code) is not None):
        post_code_correct = True
    else:
        post_code_message = 'kod pocztowy musi być w formacie 45-454\n'
