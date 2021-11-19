from django.test import TestCase

# Create your tests here.
with open("test.txt",'r+') as file:
    l = file.read()

    for n in l:
        if n == '\n':
            l = l.replace('\n', '<br>')

    file.write(l)