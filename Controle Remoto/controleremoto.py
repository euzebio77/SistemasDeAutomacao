import tkinter as tk
import serial

class ArduinoBluetoothApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Controle Remoto")
        self.configure_window()
        self.create_widgets()

        # Identificando a porta COM da qual o módulo Bluetooth está conectado
        self.arduino_serial = serial.Serial('COM13', 9600, timeout=1)

    def configure_window(self):
        # Configuração para desabilitar a maximização e centralizar na tela
        self.master.resizable(0, 0)  # Desabilita a maximização
        width = 400  # Largura desejada
        height = 300  # Altura desejada
        self.master.geometry(f"{width}x{height}+{int((self.master.winfo_screenwidth() - width) / 2)}+{int((self.master.winfo_screenheight() - height) / 2)}")

    def create_widgets(self):
        self.led_on_button = tk.Button(self.master, text="Apagar LED", command=self.turn_on_led)
        self.led_on_button.pack(pady=10)

        self.led_off_button = tk.Button(self.master, text="Acender LED", command=self.turn_off_led)
        self.led_off_button.pack(pady=10)

        self.quit_button = tk.Button(self.master, text="Sair", command=self.quit_app)
        self.quit_button.pack(pady=10)

    def turn_on_led(self):
        self.send_data('A')

    def turn_off_led(self):
        self.send_data('a')

    def send_data(self, data):
        self.arduino_serial.write(data.encode())

    def quit_app(self):
        self.arduino_serial.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ArduinoBluetoothApp(root)
    root.mainloop()
