import uuid

class Lixo:
    def __init__(self, tipo, risco):
        self.tipo = tipo
        self.__risco = risco

    def get_risco(self):
        return self.__risco

    def mostrar_risco(self):
        return f"{self.tipo} - Risco: {self.__risco:.1f}"

class LixoOrganico(Lixo):
    def mostrar_risco(self):
        return f"{self.tipo} - Risco baixo: {self.get_risco():.1f}"

class LixoReciclavel(Lixo):
    def mostrar_risco(self):
        return f"{self.tipo} - Risco médio: {self.get_risco():.1f}"

class LixoPerigoso(Lixo):
    def mostrar_risco(self):
        return f"{self.tipo} - Risco alto: {self.get_risco():.1f}"

class Ocorrencia:
    def __init__(self, local, lixo):
        aleatorio = str(uuid.uuid4())[:6]
        self.id = f"{aleatorio}"
        self.local = local
        self.__lixo = lixo
        self.__status = "Pendente"

    def resolver(self):
        self.__status = "Resolvido"

    def get_status(self):
        return self.__status

    def mostrar(self):
        return (f"ID: {self.id} | Local: {self.local} | "
                f"{self.__lixo.mostrar_risco()} | Status: {self.__status}")

class Sistema:
    def __init__(self):
        self.ocorrencias = []

    def adicionar_ocorrencia(self, ocorrencia):
        self.ocorrencias.append(ocorrencia)

    def gerar_relatorio(self):
        total = len(self.ocorrencias)
        pendentes = sum(oc.get_status() == "Pendente" for oc in self.ocorrencias)
        resolvidas = total - pendentes
        return {
            "total": total,
            "pendentes": pendentes,
            "resolvidas": resolvidas
        }


if __name__ == "__main__":
    sistema = Sistema()

    while True:
        print("\n=== Menu ===")
        print("1. Registrar ocorrência")
        print("2. Listar ocorrências")
        print("3. Resolver ocorrência")
        print("4. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            local = input("Digite o bairro: ")
            tipo = input("Tipo de lixo (organico/reciclavel/perigoso): ")

            if tipo == "organico":
                lixo = LixoOrganico("Orgânico", 1.0)
            elif tipo == "reciclavel":
                lixo = LixoReciclavel("Reciclável", 2.5)
            elif tipo == "perigoso":
                lixo = LixoPerigoso("Perigoso", 5.0)
            else:
                print("Tipo inválido.")
                continue

            ocorr = Ocorrencia(local, lixo)
            sistema.adicionar_ocorrencia(ocorr)
            print("Ocorrência registrada com ID:", ocorr.id)

        elif opcao == "2":
            print("\n=== Ocorrências ===")
            for o in sistema.ocorrencias:
                print(o.mostrar())

        elif opcao == "3":
            id_alvo = input("ID da ocorrência a resolver: ")
            encontrou = False
            for o in sistema.ocorrencias:
                if o.id == id_alvo:
                    o.resolver()
                    encontrou = True
                    print("Ocorrência resolvida.")
            if not encontrou:
                print("ID não encontrado.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")