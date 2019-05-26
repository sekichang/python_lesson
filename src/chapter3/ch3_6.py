age = int(input("年齢を入力して下さい。="))

if age < 20:
    print("未成年です")
elif age < 65:
    print("成人です")
elif age < 75:
    print("前期高齢者です")
else:
    print("後期高齢者です")
