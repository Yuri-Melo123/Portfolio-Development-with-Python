import tkinter as tk
from tkinter import messagebox
import subprocess

# Função que roda o script captura_clima.py
def rodar_script():
    try:
        subprocess.run(["python", "captura_clima.py"], check=True)
        messagebox.showinfo("Sucesso", "Dados coletados com sucesso e planilha atualizada!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Erro ao executar o script!")

# Cria a janela
janela = tk.Tk()
janela.title("Captador de Clima")
janela.geometry("300x150")

# Cria os widgets
rotulo = tk.Label(janela, text="Clique no botão para buscar a previsão.")
rotulo.pack(pady=10)

# Cria o botão
botao = tk.Button(janela, text="Buscar previsão", command=rodar_script)
botao.pack(pady=10)

# Roda a janela
janela.mainloop()
