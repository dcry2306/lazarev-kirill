import tkinter as tk
import serial


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.value = tk.StringVar()

        # Настройка интерфейса
        self.attributes('-fullscreen', True)

        # Создание элементов интерфейса
        self.label = tk.Label(self, textvariable=self.value, font=('Arial', 24))
        self.label.grid(row=0, column=0, sticky='w', padx=10, pady=10)

        self.button1 = tk.Button(self, text="Вызвать спец.службу", command=self.call_special_services, bg='blue',
                                 fg='white', font=('Arial', 16))
        self.button1.grid(row=1, column=0, sticky='w', padx=10, pady=10)

        self.button2 = tk.Button(self, text="Обновить состояние", command=self.clear_value, bg='red', fg='white',
                                 font=('Arial', 16))
        self.button2.grid(row=2, column=0, sticky='w', padx=10, pady=10)

        # Настройка порта Bluetooth
        self.bluetooth_port = 'COM3'
        try:
            self.bluetooth = serial.Serial(self.bluetooth_port, 9600)
            self.after(100, self.update_value)
        except serial.SerialException as e:
            print("Error opening serial port:", str(e))

    def update_value(self):
        value = self.bluetooth.readline().decode().strip()
        if value == "A1":
            self.value.set("Люк A открыт")
        self.after(100, self.update_value)

    def call_special_services(self):
        print("Calling special services...")
        # Здесь можно добавить код для вызова спецслужб

    def clear_value(self):
        self.value.set("")


app = App()
app.mainloop()