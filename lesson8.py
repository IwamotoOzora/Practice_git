def eat(breakfast, lunch, dinner="カレー", *desserts):
    print("朝は{}を食べました".format(breakfast))
    print("昼は{}を食べました".format(lunch))
    print("夜は{}を食べました".format(dinner))
    for dessert in desserts:
        print("おやつに{}を食べました".format(dessert))

eat("トースト", "パスタ", "カレー", "アイス", "バナナ", "スープカレー")