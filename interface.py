import tkinter as tk
from tkinter import messagebox
import subprocess

def rodar_script():
    try:
        subprocess.run(["python", "captura_clima.py"], check=True)
        messagebox.showinfo("Sucesso", "Dados coletados com sucesso e planilha atualizada!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Erro ao executar o script!")

janela = tk.Tk()
janela.title("Captador de Clima")
janela.geometry("300x150")

rotulo = tk.Label(janela, text="Clique no botão para buscar a previsão.")
rotulo.pack(pady=10)

botao = tk.Button(janela, text="Buscar previsão", command=rodar_script)
botao.pack(pady=10)

janela.mainloop()
