import tkinter as tk
from tkinter import ttk





window = tk.Tk()

class Application:
    def __init__(self):
        self.text2 = None
        self.text1 = None
        self.window = window
        self.screen()
        window.mainloop()

    def screen(self):
        self.window.geometry("600x400")
        self.window.title("Analisador léxico")
        self.window.configure(background="black")

        label1 = tk.Label(self.window, text="Input", fg="white", bg="black", font=("Arial", 12))
        label1.pack(pady=(5, 0))  # padding: 10px em cima, 0 embaixo

        # Frame 1 para agrupar Text + Scrollbar
        frame1 = tk.Frame(self.window, bg="black")
        frame1.pack(pady=10)

        self.text1 = tk.Text(frame1, width=70, height=7, wrap="word")
        self.text1.pack(side="left", fill="both", expand=True)

        scrollbar1 = ttk.Scrollbar(frame1, command=self.text1.yview)
        scrollbar1.pack(side="right", fill="y")
        self.text1.config(yscrollcommand=scrollbar1.set)

        label2 = tk.Label(self.window, text="Outinput", fg="white", bg="black", font=("Arial", 12))
        label2.pack(pady=(5, 0))  # padding: 10px em cima, 0 embaixo

        # Frame 2 para agrupar Text + Scrollbar
        frame2 = tk.Frame(self.window, bg="black")
        frame2.pack(pady=10)

        self.text2 = tk.Text(frame2, width=70, height=7, wrap="word")
        self.text2.config(state="disabled")
        self.text2.pack(side="left", fill="both", expand=True)

        scrollbar2 = ttk.Scrollbar(frame2, command=self.text2.yview)
        scrollbar2.pack(side="right", fill="y")
        self.text2.config(yscrollcommand=scrollbar2.set)

        button = tk.Button(window, text="Executar Analise", command=self.copiar_texto, bg="gray", fg="white", font=("Arial", 12))
        button.pack(anchor="e", padx=15, pady=10)

    def copiar_texto(self):
        # Pega o texto do Text1
        conteudo = self.text1.get("1.0", "end-1c") 
         # do início até o fim, excluindo a quebra de linha final

        from jsonic.analisador_lexico.lexer import get_lexer
        get_lexer.input(conteudo)
       
        self.text2.config(state="normal")
        # # Limpa o Text2
        self.text2.delete("1.0", "end")
        # # Insere o conteúdo no Text2
        for tok in get_lexer:
            self.text2.insert("1.0", str(tok)+'\n')
        self.text2.config(state="disabled")
