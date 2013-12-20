def hash_func(string, t_size):
    s = 0
    for i in string:
        s += ord(i)
    return s % t_size


print(hash_func('some', 15))