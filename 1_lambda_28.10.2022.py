# encoding=utf-8

genius = lambda x: x + 'гений '

i = input("")
while i != "off":
    print(genius(i))
    i = input("")
else:
    print('system shot down')