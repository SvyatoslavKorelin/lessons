category = input("выберите время приема пищи: завтрак/обед/ужин")
wish = input("плотность")
if category == "завтрак":
    print("каша")
if category == "обед" or "ужин":
    if wish == "плотно":
        print("плов")
    else:
        print("котлета с пюре")

