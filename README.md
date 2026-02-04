# SISTEMA DE REGISTRO DE OCORRÊNCIAS - ODS 11

## INTRODUÇÃO E TEMA

A dupla desenvolveu um programa em python baseado na ODS 11 (Cidades e Comunidades Sustentáveis).
O projeto é um terminal onde o usuário registra a ocorrência, contendo o bairro, o tipo de lixo e seu risco. Além disso, o denunciante poderá ver as ocorrências registradas, resolver uma ocorrência, gerar um relatório com o total de ocorrências, listadas como 'pendente' ou 'resolvido'.
Também poderá ver um gráfico onde mostra os bairros onde há ocorrências e a quantidade de denúncias.
Por fim, o usuário poderá sair do sistema.

## EQUIPE

* Evellyn dos Santos Ribeiro;
* Thaylanne Kérrinna Varela Leite.

## FUNÇÕES CRIADAS

### Classes de Lixo

Classe Lixo, LixoOrganico, LixoReciclavel e LixoPerigoso

* `def mostrar_risco(self):` mostra o tipo de lixo e id específico (sofre polimorfismo de acordo com o tipo de lixo).

### Classe Ocorrencia

* `__init__(self, local, lixo):` Função construtora que cria uma nova ocorrência, gera um ID único (prefixo do bairro + parte aleatória) e define local (bairro), __lixo (objeto associado) e __status inicial como "Pendente”.

* `resolver(self):` Função de negócio que altera o status da ocorrência para "Resolvido".

* `get_status(self):` Getter que retorna o status atual da ocorrência. É usado no relatório para contar pendentes e resolvidas.

* `mostrar(self):` Função de exibição que retorna uma string formatada com ID, bairro, informações do lixo e status. É usada na tela de listagem.

### Classe Sistema

* `__init__(self):` Método construtor que inicializa a lista ocorrencias, que armazena objetos da classe Ocorrencia.

* `adicionar_ocorrencia(self, ocorrencia):` Função de agregação que adiciona uma ocorrência ao sistema e centraliza o controle das ocorrências cadastradas.

### Classe App (Interface Gráfica)

* `__init__(self):` Método construtor da aplicação que configura a janela principal, define aparência, cores e botões, cria a instância do Sistema e associa cada botão a uma função específica.

## MÉTODOS DE NEGÓCIO

* `criar_ocorrencia(self, local, tipo, risco):` Cria o objeto de lixo correto (Orgânico, Reciclável ou Perigoso), cria uma nova Ocorrencia e adiciona a ocorrência ao sistema.

* `validar_risco(self, texto):` Verifica se o valor informado é numérico e está entre 0 e 10. Retorna o valor é válido ou None.

## MÉTODOS DE TELAS (INTERFACE)

* `tela_registrar(self):` Abre a tela de registro de ocorrência, coleta bairro, tipo de lixo e risco, além de validar os dados e salvar a ocorrência.

* `tela_listar(self):` Exibe todas as ocorrências cadastradas e usa o método mostrar() da classe Ocorrencia.

* `tela_resolver(self):` Permite selecionar uma ocorrência pelo ID e chama o método resolver() para alterar o status.

* `tela_relatorio(self):` Gera um relatório geral com o total de ocorrências pendentes e resolvidas. Usa get_status() para contagem.

* `gerar_grafico(self):` Gera um gráfico de barras com o total de ocorrências por bairro. Utiliza a biblioteca matplotlib.

## LISTAGEM DOS EXTRAS

Foram utilizadas as bibliotecas:

* customtkinter: para formatar a interface gráfica;
* uuid: para a geração dos ID’s únicos;
* matplotlib: para o gráfico.
