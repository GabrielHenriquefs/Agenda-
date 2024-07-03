import json
from prettytable import PrettyTable

# Função para carregar a agenda de um arquivo JSON
def carregar_agenda(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)  # Carrega os dados do arquivo e retorna como uma lista de dicionários
    except FileNotFoundError:
        return []  # Se o arquivo não existir, retorna uma lista vazia

# Função para salvar a agenda em um arquivo JSON
def salvar_agenda(arquivo, agenda):
    with open(arquivo, 'w') as f:
        json.dump(agenda, f, indent=4)  # Salva a lista de eventos no arquivo com indentação para melhor legibilidade

# Função para adicionar um evento à agenda
def adicionar_evento(agenda, titulo, data, hora, descricao):
    evento = {
        "titulo": titulo,
        "data": data,
        "hora": hora,
        "descricao": descricao
    }
    agenda.append(evento)  # Adiciona o evento à lista de eventos

# Função para remover um evento da agenda pelo título
def remover_evento(agenda, titulo):
    agenda[:] = [evento for evento in agenda if evento["titulo"] != titulo]  # Remove todos os eventos que têm o título especificado

# Função para listar todos os eventos da agenda
def listar_eventos(agenda):
    tabela = PrettyTable()
    tabela.field_names = ["Título", "Data", "Hora", "Descrição"]  # Define os cabeçalhos das colunas da tabela
    for evento in agenda:
        tabela.add_row([evento["titulo"], evento["data"], evento["hora"], evento["descricao"]])  # Adiciona cada evento como uma linha na tabela
    print(tabela)  # Exibe a tabela
    print("--------")  # Imprime a separação após a tabela

# Função para buscar um evento pelo título
def buscar_evento(agenda, titulo):
    for evento in agenda:
        if evento["titulo"] == titulo:  # Verifica se o título do evento corresponde ao título procurado
            return evento  # Retorna o evento encontrado
    return None  # Retorna None se nenhum evento com o título especificado for encontrado

# Função principal que controla o fluxo do programa
def main():
    arquivo = "agenda.json"  # Nome do arquivo onde a agenda será salva/carregada
    agenda = carregar_agenda(arquivo)  # Carrega a agenda do arquivo
    
    while True:
        # Menu de opções
        print("\nAgenda:")
        print("1. Adicionar evento")
        print("2. Remover evento")
        print("3. Listar eventos")
        print("4. Buscar evento")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Coleta os dados do evento a ser adicionado
            titulo = input("Título: ")
            data = input("Data (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            descricao = input("Descrição: ")
            adicionar_evento(agenda, titulo, data, hora, descricao)  # Adiciona o evento à agenda
            salvar_agenda(arquivo, agenda)  # Salva a agenda atualizada no arquivo
        
        elif opcao == "2":
            titulo = input("Título do evento a ser removido: ")
            remover_evento(agenda, titulo)  # Remove o evento pelo título
            salvar_agenda(arquivo, agenda)  # Salva a agenda atualizada no arquivo
        
        elif opcao == "3":
            listar_eventos(agenda)  # Lista todos os eventos da agenda
        
        elif opcao == "4":
            titulo = input("Título do evento a ser buscado: ")
            evento = buscar_evento(agenda, titulo)  # Busca o evento pelo título
            if evento:
                print(f"Encontrado: {evento}")  # Exibe o evento encontrado
            else:
                print("Evento não encontrado.")  # Mensagem caso o evento não seja encontrado
        
        elif opcao == "5":
            break  # Sai do loop e termina o programa

        else:
            print("Opção inválida, tente novamente.")  # Mensagem de erro para opção inválida

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal
