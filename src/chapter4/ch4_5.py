def to_float(s):
    try:
        return float(s)
    except ValueError:
        print("文字列ではなく数値を入力して下さい")

num = input("数値を入力して下さい:")

print(to_float(num))
