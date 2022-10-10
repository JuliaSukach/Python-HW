# Написать ф-ю, которая выводит сегодн дату, текущее время и приветствие.
from datetime import datetime
import time


def get_time_through_datetime():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 'Hi Yulia'


print('Now is {0} \n{1}'.format(*get_time_through_datetime()))


def get_time_through_time():
    return time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())


print(f'{get_time_through_time()} \nHi Yulia')
