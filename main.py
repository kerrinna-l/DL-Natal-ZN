# ===============================
# IMPORTAÇÕES
# ===============================

import customtkinter as ctk # Biblioteca para interface gráfica
from tkinter import messagebox # Caixa de mensagens
import uuid # Geração de identificadores únicos
import matplotlib.pyplot as plt # Biblioteca para geração de gráficos

# =====================================
# CLASSES DO SISTEMA
# =====================================

# Classe base Lixo
# Herança e Polimorfismo
class Lixo:
    def __init__(self, tipo, risco):
        self.tipo = tipo # Atributo público
        self.__risco = risco # Atributo privado (encapsulamento)

    # Encapsulamento
    def get_risco(self):
        return self.__risco

    # Polimorfismo
    def mostrar_risco(self):
        return f"{self.tipo} - Risco: {self.__risco:.1f}"

# Subclasse para lixo orgânico
class LixoOrganico(Lixo):
    # Sobrescrita do método mostrar_risco
    def mostrar_risco(self):
        return f"{self.tipo} - Risco baixo: {self.get_risco():.1f}"

# Subclasse para lixo reciclável
class LixoReciclavel(Lixo):
    def mostrar_risco(self):
        return f"{self.tipo} - Risco médio: {self.get_risco():.1f}"

# Subclasse para lixo perigoso
class LixoPerigoso(Lixo):
    def mostrar_risco(self):
        return f"{self.tipo} - Risco alto: {self.get_risco():.1f}"

# =====================================
# CLASSE OCORRÊNCIA
# =====================================

# Associação e encapsulamento
class Ocorrencia:
    # Gerar prefixo do ID conforme o bairro
    prefixos_bairros = {
        "Igapó": "IG",
        "Salinas": "SA",
        "Potengi": "PO",
        "Nossa Senhora da Apresentação": "NS",
        "Lagoa Azul": "LA",
        "Pajuçara": "PA",
        "Redinha": "RE"
    }

    def __init__(self, local, lixo):
        prefixo = self.prefixos_bairros.get(local, "XX")
        aleatorio = str(uuid.uuid4())[:6] # Parte aleatória do ID
        self.id = f"{prefixo}-{aleatorio}" # ID único e padronizado

        self.local = local # Bairro da ocorrência
        self.__lixo = lixo # Objeto Lixo (associação)
        self.__status = "Pendente" # Status inicial

    # Resolver a ocorrência
    def resolver(self):
        self.__status = "Resolvido"

    # Getter do status
    def get_status(self):
        return self.__status

    # Retornar uma string formatada com os dados da ocorrência
    def mostrar(self):
        return (
            f"ID: {self.id} | "
            f"Local: {self.local} | "
            f"{self.__lixo.mostrar_risco()} | "
            f"Status: {self.__status}"
        )

# =====================================
# CLASSE SISTEMA
# =====================================

# Agregação
class Sistema:
    def __init__(self):
        self.ocorrencias = [] # Armazenar objetos Ocorrencia

    # Adicionar ocorrências ao sistema
    def adicionar_ocorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)

# =====================================
# INTERFACE GRÁFICA 
# =====================================

class App(ctk.CTk):
    # Listas fixas usadas nos menus
    bairros = [
        "Igapó", "Salinas", "Potengi",
        "Nossa Senhora da Apresentação",
        "Lagoa Azul", "Pajuçara", "Redinha"
    ]
    tipos_lixo = ["Orgânico", "Reciclável", "Perigoso"]

    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("DL Natal-ZN")
        self.geometry("800x600")

        # Configuração visual do CustomTkinter
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # Instância do sistema (agregação)
        self.sistema = Sistema()

        # Cores usadas nos botões
        self.verde_agua = ("#06b6d4", "#22d3ee")
        self.vermelho = ("#dc2626", "#b91c1c")

        # Título do menu principal
        ctk.CTkLabel(
            self,
            text="Menu Principal",
            font=("Arial", 25, "bold")
        ).pack(pady=20)

        # Lista de botões (texto, ação, cor)
        botoes = [
            ("Registrar Ocorrência", self.tela_registrar, self.verde_agua),
            ("Listar Ocorrências", self.tela_listar, self.verde_agua),
            ("Resolver Ocorrência", self.tela_resolver, self.verde_agua),
            ("Gerar Relatório", self.tela_relatorio, self.verde_agua),
            ("Gráfico de Ocorrências", self.gerar_grafico, self.verde_agua),
            ("Sair", self.destroy, self.vermelho)
        ]

        # Criação dinâmica dos botões
        for texto, comando, cor in botoes:
            ctk.CTkButton(
                self,
                text=texto,
                width=250,
                fg_color=cor[0],
                hover_color=cor[1],
                text_color="white",
                command=comando
            ).pack(pady=7)

    # =====================================
    # MÉTODOS DE NEGÓCIO
    # =====================================

    # Criar a ocorrência com base no tipo de lixo escolhido
    def criar_ocorrencia(self, local, tipo, risco):
        if tipo == "Orgânico":
            lixo = LixoOrganico(tipo, risco)
        elif tipo == "Reciclável":
            lixo = LixoReciclavel(tipo, risco)
        else:
            lixo = LixoPerigoso(tipo, risco)

        self.sistema.adicionar_ocorrencia(Ocorrencia(local, lixo))

    # Validar se o risco é um número entre 0 e 10
    def validar_risco(self, texto):
        try:
            valor = float(texto)
            if 0 <= valor <= 10:
                return valor
        except:
            pass
        return None

    # =====================================
    # TELAS
    # =====================================

    # Tela de registro de ocorrência
    def tela_registrar(self):
        win = ctk.CTkToplevel(self)
        win.title("Registrar Ocorrência")
        win.geometry("400x350")
        win.grab_set() # Bloquear a janela principal

        ctk.CTkLabel(
            win,
            text="Registrar Ocorrência",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        bairro_var = ctk.StringVar(value=self.bairros[0])
        tipo_var = ctk.StringVar(value=self.tipos_lixo[0])
        entrada_risco = ctk.CTkEntry(win, placeholder_text="Risco (0-10)")

        # Menus de seleção
        ctk.CTkOptionMenu(
            win, values=self.bairros,
            variable=bairro_var,
            fg_color=self.verde_agua[0],
            button_color=self.verde_agua[1],
            button_hover_color="#0e7490",
            text_color="white"
        ).pack(pady=5)

        ctk.CTkOptionMenu(
            win, values=self.tipos_lixo,
            variable=tipo_var,
            fg_color=self.verde_agua[0],
            button_color=self.verde_agua[1],
            button_hover_color="#0e7490",
            text_color="white"
        ).pack(pady=5)

        entrada_risco.pack(pady=5)

        # Salvar a ocorrência
        def registrar():
            risco = self.validar_risco(entrada_risco.get())
            if risco is None:
                messagebox.showerror("Erro", "Risco deve ser um número entre 0 e 10")
                return

            self.criar_ocorrencia(bairro_var.get(), tipo_var.get(), risco)
            messagebox.showinfo("OK", "Ocorrência registrada!")
            win.destroy()

        ctk.CTkButton(
            win, text="Salvar", width=200,
            fg_color=self.verde_agua[0],
            hover_color=self.verde_agua[1],
            text_color="white",
            command=registrar
        ).pack(pady=20)

    # Listar ocorrências
    def tela_listar(self):
        win = ctk.CTkToplevel(self)
        win.title("Ocorrências")
        win.geometry("500x400")
        win.grab_set()

        caixa = ctk.CTkTextbox(win, width=480, height=350)
        caixa.pack(fill="both", expand=True, padx=10, pady=10)

        if not self.sistema.ocorrencias:
            caixa.insert("end", "Nenhuma ocorrência cadastrada.")
        else:
            for oc in self.sistema.ocorrencias:
                caixa.insert("end", oc.mostrar() + "\n\n")

    # Resolver ocorrência
    def tela_resolver(self):
        if not self.sistema.ocorrencias:
            messagebox.showinfo("Info", "Nenhuma ocorrência cadastrada.")
            return

        win = ctk.CTkToplevel(self)
        win.title("Resolver Ocorrência")
        win.geometry("350x250")
        win.grab_set()

        id_var = ctk.StringVar(value=self.sistema.ocorrencias[0].id)

        ctk.CTkOptionMenu(
            win,
            values=[o.id for o in self.sistema.ocorrencias],
            variable=id_var,
            fg_color=self.verde_agua[0],
            button_color=self.verde_agua[1],
            button_hover_color="#0e7490",
            text_color="white"
        ).pack(pady=10)

        def resolver():
            for oc in self.sistema.ocorrencias:
                if oc.id == id_var.get():
                    oc.resolver()
                    messagebox.showinfo("OK", "Ocorrência resolvida!")
                    win.destroy()
                    return

        ctk.CTkButton(
            win, text="Resolver", width=150,
            fg_color=self.verde_agua[0],
            hover_color=self.verde_agua[1],
            text_color="white",
            command=resolver
        ).pack(pady=20)

    # Relatório
    def tela_relatorio(self):
        win = ctk.CTkToplevel(self)
        win.title("Relatório")
        win.geometry("400x300")
        win.grab_set()

        total = len(self.sistema.ocorrencias)
        pendentes = sum(oc.get_status() == "Pendente" for oc in self.sistema.ocorrencias)
        resolvidas = total - pendentes

        ctk.CTkLabel(win, text="Relatório Geral", font=("Arial", 20, "bold")).pack(pady=15)
        ctk.CTkLabel(win, text=f"Total: {total}").pack(pady=5)
        ctk.CTkLabel(win, text=f"Pendente: {pendentes}").pack(pady=5)
        ctk.CTkLabel(win, text=f"Resolvido: {resolvidas}").pack(pady=5)

    # Gerar de gráfico com matplotlib
    def gerar_grafico(self):
        if not self.sistema.ocorrencias:
            messagebox.showinfo("Info", "Nenhuma ocorrência cadastrada.")
            return

        bairros = {}
        for oc in self.sistema.ocorrencias:
            bairros[oc.local] = bairros.get(oc.local, 0) + 1

        plt.figure(figsize=(10, 6))
        plt.bar(bairros.keys(), bairros.values(), color=self.verde_agua[0])
        plt.title("Ocorrências por Bairro")
        plt.ylabel("Quantidade")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# =====================================
# EXECUÇÃO
# =====================================

app = App()
app.mainloop()