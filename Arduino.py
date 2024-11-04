import tkinter as tk
from tkinter import messagebox
import time
import serial  # Módulo para comunicação serial, caso queira conectar ao HC-05

# Configurações do HC-05 (Bluetooth) - Ajuste a porta e baudrate conforme necessário
# Tente conectar à porta serial se estiver usando o HC-05
try:
    # Substitua "COM3" pela porta correta do seu HC-05
    bt_serial = serial.Serial("COM3", 9600, timeout=1)
    connected = True
except:
    connected = False
    messagebox.showinfo(
        "Conexão", "Não foi possível conectar ao dispositivo HC-05.")

# Funções para simulação de conexão Bluetooth


def connect_bluetooth():
    global connected
    if connected:
        messagebox.showinfo("Conexão", "Já está conectado!")
    else:
        try:
            bt_serial.open()  # Abre a conexão serial
            connected = True
            messagebox.showinfo("Conexão", "Conectado com sucesso!")
        except:
            messagebox.showinfo(
                "Erro", "Não foi possível conectar ao dispositivo HC-05.")


def disconnect_bluetooth():
    global connected
    if connected:
        bt_serial.close()  # Fecha a conexão serial
        connected = False
        messagebox.showinfo("Conexão", "Desconectado com sucesso!")
    else:
        messagebox.showinfo("Erro", "Nenhuma conexão ativa para desconectar.")

# Função para alternar o estado da campainha


def toggle_buzzer(state):
    if connected:
        # Envia o comando pela porta serial
        bt_serial.write(state.encode())
        # Altera o texto do botão com base no estado
        if state == '1':
            btn_alarm.config(text="Desligar Campainha",
                             command=lambda: toggle_buzzer('0'))
        else:
            btn_alarm.config(text="Ligar Campainha",
                             command=lambda: toggle_buzzer('1'))
    else:
        messagebox.showinfo("Erro", "Conecte-se ao dispositivo primeiro.")

# Função para acionar o alarme e fazer o efeito de botão pressionado


def trigger_alarm():
    if connected:
        # Temporariamente altera o botão para um estado pressionado
        # Cor quando pressionado
        btn_alarm.config(bg="#e06c75", activebackground="#be5046")
        btn_alarm.config(relief="sunken")  # Efeito de botão afundado
        root.update()  # Atualiza a interface para refletir mudanças imediatamente
        bt_serial.write(b'1')  # Envia o comando para ligar o alarme
        time.sleep(1)  # Pausa por 1 segundo
        bt_serial.write(b'0')  # Envia o comando para desligar o alarme
        # Cor original
        btn_alarm.config(bg="#61afef", activebackground="#4b8bbf")
        btn_alarm.config(relief="raised")  # Volta ao efeito original
    else:
        messagebox.showinfo("Erro", "Conecte-se ao dispositivo primeiro.")


# Interface Gráfica
root = tk.Tk()
root.title("Controle do Alarme")
root.geometry("600x700")
root.configure(bg="#282c34")

# Estilos de Botões
button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#61afef",
    "fg": "white",
    "activebackground": "#4b8bbf",
    "activeforeground": "white",
    "bd": 0,
    "relief": "flat",
    "width": 20,
    "height": 2
}

# Botão de Conectar
btn_connect = tk.Button(root, text="Conectar ao HC-05",
                        command=connect_bluetooth, **button_style)
btn_connect.pack(pady=10)

# Botão de Desconectar
btn_disconnect = tk.Button(root, text="Desconectar",
                           command=disconnect_bluetooth, **button_style)
btn_disconnect.pack(pady=10)

# Botão de Acionar Alarme (grande)
btn_alarm = tk.Button(
    root, text="ACIONAR ALARME", command=trigger_alarm,
    font=("Arial", 16, "bold"), bg="#61afef", fg="white",
    activebackground="#4b8bbf", activeforeground="white",
    width=30, height=20, bd=0, relief="raised"
)
btn_alarm.pack(pady=30)

root.mainloop()
