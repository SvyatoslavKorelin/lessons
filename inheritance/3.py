# encoding=utf-8
class Animal():
    def __init__ (self, vid_type, voice):
        self.type = vid_type
        self.voice = voice

    def print_t(self):
        print(self.voice)

Egnyat = Animal('Барящик', 'кушац хочется')
Egnyat.print_t()
print(Egnyat.type)
katikovka = Animal('Птица', 'Курлык - курлык')
print(katikovka.type)
katikovka.print_t()