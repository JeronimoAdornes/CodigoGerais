import tkinter as tk
from tkinter import messagebox
import time

# Funções para simulação


def connect_bluetooth():
    messagebox.showinfo("Conexão", "Conectado com sucesso!")


def disconnect_bluetooth():
    messagebox.showinfo("Conexão", "Desconectado com sucesso!")


def toggle_buzzer(state):
    # Alterna o texto do botão entre Ligar e Desligar
    if state == '1':
        btn_alarm.config(text="Desligar Campainha",
                         command=lambda: toggle_buzzer('0'))
    else:
        btn_alarm.config(text="Ligar Campainha",
                         command=lambda: toggle_buzzer('1'))


def trigger_alarm():
    # Temporariamente altera o botão para um estado pressionado
    # Cor quando pressionado
    btn_alarm.config(bg="#e06c75", activebackground="#be5046")
    btn_alarm.config(relief="sunken")  # Efeito de botão afundado
    root.update()  # Atualiza a interface para refletir mudanças imediatamente
    time.sleep(1)  # Pausa por 1 segundo
    btn_alarm.config(bg="#61afef", activebackground="#4b8bbf")  # Cor original
    btn_alarm.config(relief="raised")  # Volta ao efeito original


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
    font=("Arial", 18, "bold"), bg="#61afef", fg="white",
    activebackground="#4b8bbf", activeforeground="white",
    width=30, height=20, bd=0, relief="raised"
)
btn_alarm.pack(pady=30)

root.mainloop()
