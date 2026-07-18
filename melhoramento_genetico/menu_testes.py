
def exibir_menu():
    """Exibe o menu de opções no terminal."""
    print("\n" + "=" * 40)
    print("      SISTEMA DE MELHORAMENTO GENÉTICO")
    print("=" * 40)
    print("1. Carregar Arquivo de Dados (CSV)")
    print("2. Configurar Parâmetros do Algoritmo")
    print("3. Executar Simulação Evolucionária")
    print("0. Sair")
    print("=" * 40)


def executar_sistema():
    """Ciclo de execução principal do menu."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n[Aviso] A carregar dados do arquivo 'dados/animais_iniciais.csv'...")
            # Futura chamada da função de leitura de dados
        elif opcao == "2":
            print("\n[Aviso] Configuração de taxas de mutação e gerações.")
        elif opcao == "3":
            print("\n[Aviso] A iniciar o motor de Computação Evolucionária.")
        elif opcao == "0":
            print("\nA terminar o programa. Até à próxima!")
            break
        else:
            print("\nOpção inválida! Por favor, tente novamente.")


# Executa o menu se o arquivo for rodado diretamente
if __name__ == "__main__":
    executar_sistema()