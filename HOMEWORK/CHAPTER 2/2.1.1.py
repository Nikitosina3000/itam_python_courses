def greetings(name):
    a = ('Доброго времени суток, ' + name.split()[0] + " \"Человек\" " + name.split()[1])
    return a
print(greetings(input()))
