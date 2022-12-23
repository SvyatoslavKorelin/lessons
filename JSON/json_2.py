# encoding=utf-8
import json
task = ["Slava", 18, ["Russia"]]
slovar = tuple(task)
with open('Task2_Korelin.json', 'w') as write_file:
    json.dump(slovar, write_file, indent=4)