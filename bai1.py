import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Máy Tính Cơ Bản")

        # Tạo ô nhập liệu
        self.entry = tk.Entry(master, width=25, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Tạo các nút
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0
        for button_text in buttons:
            if button_text == "=":
                tk.Button(master, text=button_text, width=5, command=self.evaluate).grid(row=row, column=col)
            else:
                tk.Button(master, text=button_text, width=5, command=lambda x=button_text: self.add_to_entry(x)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_to_entry(self, value):
        self.entry.insert(tk.END, value)

    def evaluate(self):
        try:
            result = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()