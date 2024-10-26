import tkinter as tk
from tkinter import messagebox
from cmath import sqrt


# Função para calcular as raízes da equação do segundo grau
def calcular_raizes():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        delta = b ** 2 - 4 * a * c

        # Cálculo das raízes usando cmath para suportar números complexos
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)

        # Exibindo o resultado
        resultado = f"Raiz 1: {raiz1:.2f}\nRaiz 2: {raiz2:.2f}"
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero.")


root = tk.Tk()
root.title("Calculadora de Raízes de Equação do 2° Grau")

# Layout para entrada dos coeficientes
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Coeficiente a:").grid(row=0, column=0, padx=5, pady=5)
entrada_a = tk.Entry(frame)
entrada_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Coeficiente b:").grid(row=1, column=0, padx=5, pady=5)
entrada_b = tk.Entry(frame)
entrada_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Coeficiente c:").grid(row=2, column=0, padx=5, pady=5)
entrada_c = tk.Entry(frame)
entrada_c.grid(row=2, column=1, padx=5, pady=5)

# Botão para calcular as raízes
bt_calcular = tk.Button(root, text="Calcular Raízes", command=calcular_raizes, bg="#4CAF50")
bt_calcular.pack(pady=10)

root.mainloop()
