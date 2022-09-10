from tkinter import simpledialog, messagebox


def main():
    prime_cost_str = simpledialog.askstring("数値", "原価は？")
    prime_cost = int(prime_cost_str)
    mode = simpledialog.askstring("数値で選んでください", "1:原価率？2:利益率？")
    if mode == str(1) or mode == str(2):
        pass
    else:
        messagebox.showerror('エラー', '数字の1か2で入力してください')
        return
    factor = int(simpledialog.askstring("数値", "言われた数値は"))
    if mode == str(1):
        factor_first = 1 + factor / 10
        result = prime_cost * factor_first
        # messagebox.showinfo('結果', str(result))
        print(result)
    elif mode == str(2):
        factor_second = 1 - float('0.' + str(factor))
        result = float(prime_cost) / factor_second
        # messagebox.showinfo('結果', str(result))
        print(result)


if __name__ == '__main__':
    main()
