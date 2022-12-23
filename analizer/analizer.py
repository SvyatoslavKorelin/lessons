def main(request):
    if "расп" in request:
        schedule()
    elif "трен" in request:
        coach()
    elif "оплат" in request:
        pricelist()
    elif "откос" in request:
        otkos()
    elif "работ" in request:
        rabota()
    else:
        nocommentary()



def schedule():
    print("kakoe to расписание")


def coach():
    print("какой-то тренер")


def pricelist():
    print("цены на занятия")


def nocommentary():
    print("без комметариев")


def otkos():
    print("ПОПАЛСЯ.РОДИНА СЛЫШИТ И ВИДИТ ВСЕ!")


def rabota():
    print("для устройства на работу тренером звонить 8 800 555 35 35")
