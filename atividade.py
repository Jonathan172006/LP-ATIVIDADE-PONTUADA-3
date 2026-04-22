import os

def limpar_tela():

    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n" + "="*45)
    print(" SISTEMA DE RESERVAS - SWEET FLIGHT ")
    print("="*45)
    print("1. Registrar o número de cada avião")
    print("2. Registrar assentos disponíveis (por avião)")
    print("3. Reservar passagem aérea")
    print("4. Realizar consulta por avião")
    print("5. Realizar consulta por passageiro")
    print("6. Encerrar sistema")
    print("="*45)
    return input("Escolha uma opção: ")

def registrar_avioes(avioes):
    limpar_tela()
    print("--- Registro de Aviões ---\n")
    for i in range(4):
        avioes[i] = input(f"Informe o número de identificação do {i+1}º avião: ")
    print("\n Aviões registrados com sucesso!")

def registrar_assentos(avioes, assentos):
    limpar_tela()
    print("--- Registro de Assentos ---\n")
    
    if avioes[0] == "":
        print("  Aviso: Registre os aviões (Opção 1) antes de registrar os assentos.")
        return

    for i in range(4):
        while True:
            try:
                qtd = int(input(f"Informe a quantidade de assentos disponíveis no avião {avioes[i]}: "))
                if qtd >= 0:
                    assentos[i] = qtd
                    break
                else:
                    print("A quantidade não pode ser negativa. Tente novamente.")
            except ValueError:
                print("Valor inválido! Digite um número inteiro.")
    print("\n Assentos registrados com sucesso!")

def reservar_passagem(avioes, assentos, reservas):
    limpar_tela()
    print("--- Reserva de Passagem ---\n")
    
    if len(reservas) >= 20:
        print(" Limite máximo de 20 reservas globais atingido!")
        return

    num_aviao = input("Informe o número do avião desejado: ")

    if num_aviao not in avioes:
        print(" Este avião não existe!")
        return

    indice_aviao = avioes.index(num_aviao)

    if assentos[indice_aviao] <= 0:
        print(" Não há assentos disponíveis para este avião!")
        return

    nome_passageiro = input("Informe o nome do passageiro: ")
    
    nova_reserva = {
        "numero_aviao": num_aviao,
        "nome_passageiro": nome_passageiro
    }
    
    reservas.append(nova_reserva)
    assentos[indice_aviao] -= 1
    
    print("\n Reserva realizada com sucesso!")

def consultar_por_aviao(avioes, reservas):
    limpar_tela()
    print("--- Consulta por Avião ---\n")
    num_aviao = input("Informe o número do avião para consulta: ")

    if num_aviao not in avioes:
        print(" Este avião não existe!")
        return

    encontrou_reserva = False
    print(f"\n Passageiros com reserva no avião {num_aviao}:")
    
    for reserva in reservas:
        if reserva["numero_aviao"] == num_aviao:
            print(f"- {reserva['nome_passageiro']}")
            encontrou_reserva = True

    if not encontrou_reserva:
        print("Não há reservas realizadas para este avião!")

def consultar_por_passageiro(reservas):
    limpar_tela()
    print("--- Consulta por Passageiro ---\n")
    nome_passageiro = input("Informe o nome do passageiro para consulta: ")

    encontrou_reserva = False
    print(f"\n Reservas encontradas para o passageiro '{nome_passageiro}':")
    
    for reserva in reservas:
        if reserva["nome_passageiro"].lower() == nome_passageiro.lower():
            print(f"- Voo no Avião: {reserva['numero_aviao']}")
            encontrou_reserva = True

    if not encontrou_reserva:
        print("Não há reservas realizadas para este passageiro!")

def main():
    avioes = [""] * 4
    assentos = [0] * 4
    reservas = []

    while True:
        limpar_tela()
        opcao = exibir_menu()

        if opcao == '1':
            registrar_avioes(avioes)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '2':
            registrar_assentos(avioes, assentos)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '3':
            reservar_passagem(avioes, assentos, reservas)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '4':
            consultar_por_aviao(avioes, reservas)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '5':
            consultar_por_passageiro(reservas)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '6':
            limpar_tela()
            print("\nEncerrando o sistema Sweet Flight. Até logo! \n")
            break
        else:
            print("\n Opção inválida! Por favor, escolha um número de 1 a 6.")
            input("\nPressione ENTER para tentar novamente...")

if __name__ == "__main__":
    main()
