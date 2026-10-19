import tkinter as tk
import serial

port ='COM9'
baudrate=9600
ser = serial.Serial(port, baudrate)
def encender_led():
    ser.write(b'a')
print("LED encendido")
def apagar_led():
    ser.write(b'b')
print("Led apagado")

ventana = tk.Tk()
ventana.title("Actividaid 07 ­ Encender LED")
boton_encender = tk.Button(ventana, text="Encender LED", command=encender_led)
boton_encender.pack(pady=15)
boton_apagar = tk.Button(ventana, text="Apagar LED", command=apagar_led)
boton_apagar.pack(pady=15)
ventana.mainloop()
ser.close()
