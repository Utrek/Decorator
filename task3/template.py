import datetime
import os

def logger(path):
    if not os.path.exists(path):
        open(path, 'w').close()
    def __logger(old_function):
        def new_function(*args,**kwargs):
            current_time = datetime.datetime.now()
            result = old_function(*args,**kwargs)
            my_file = open(path, "a")
            my_file.write(f'Дата и время вызова функции:{current_time}\nИмя функции: {old_function.__name__} \nАргументы, с которыми вызывалась функция: {args=} {kwargs=}\nВозвращаемое значение: {result}\n')
            my_file.close()
            return result
        return new_function
    return __logger

