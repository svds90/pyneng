# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter IP: ')
octets = ip.split('.')
oct_int = []
octets_correct = True

if len(octets) != 4:
    octets_correct = False
else:
    for octet in octets:
        if not(octet.isdigit() and int(octet) in range(256)):
            octets_correct = False
            break

if octets_correct == False:
    print('Неправильный IP-адрес')
else:
    oct_int = [int(octet) for octet in octets]

    if oct_int[0] in range(1, 224):
        print('unicast')
    elif oct_int[0] in range(224, 239):
        print('multicast')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
