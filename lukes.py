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










import tkinter as tk
import serial

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.values = {
            "A1": tk.StringVar(),
            "A2": tk.StringVar(),
            "A3": tk.StringVar(),
            "A4": tk.StringVar(),
            "A5": tk.StringVar()
        }

        self.configure_gui()

        # Configure Bluetooth port
        self.bluetooth_port = 'COM3'
        try:
            self.bluetooth = serial.Serial(self.bluetooth_port, 9600)
            self.after(100, self.update_values)
        except serial.SerialException as e:
            print("Error opening serial port:", str(e))

    def configure_gui(self):
        self.attributes('-fullscreen', True)
        self.title("Hatch Status")

        # Create status windows for each hatch
        for i, hatch in enumerate(["A1", "A2", "A3", "A4", "A5"]):
            frame = tk.Frame(self, borderwidth=2, relief="groove")
            frame.grid(row=i, column=0, padx=10, pady=10, sticky="nsew")

            label = tk.Label(frame, text=f"Люк {hatch} состояние:", font=('Arial', 18))
            label.grid(row=0, column=0, padx=10, pady=5)

            status_label = tk.Label(frame, textvariable=self.values[hatch], font=('Arial', 16))
            status_label.grid(row=1, column=0, padx=10, pady=5)

        # Button to clear all values
        clear_button = tk.Button(self, text="Сброс состояния", command=self.clear_values, bg='red', fg='white', font=('Arial', 16))
        clear_button.grid(row=len(self.values), column=0, padx=10, pady=10)

    def update_values(self):
        value = self.bluetooth.readline().decode().strip()
        if value in self.values:
            self.values[value].set(f"Люк {value} открыт")
        
        self.after(100, self.update_values)

    def clear_values(self):
        for value in self.values.values():
            value.set("")

app = App()
app.mainloop()
