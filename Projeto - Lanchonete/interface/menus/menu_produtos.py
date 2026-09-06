from servicos.produto_service import ProdutoService
from interface.telas.tela_produtos import TelaProdutos


class MenuProdutos:
    def __init__(self, produto_service: ProdutoService) -> None:
        self.__tela = TelaProdutos(produto_service)

    def executar(self) -> None:
        opcao: str = ""
        while opcao != "0":
            print("\n--- MENU DE PRODUTOS ---")
            print("1 - Cadastrar Suco")
            print("2 - Cadastrar Sanduíche")
            print("3 - Cadastrar Salada de Frutas")
            print("4 - Listar Cardápio")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.__tela.cadastrar_suco()
            elif opcao == "2":
                self.__tela.cadastrar_sanduiche()
            elif opcao == "3":
                self.__tela.cadastrar_salada_frutas()
            elif opcao == "4":
                self.__tela.listar_produtos()
            elif opcao == "0":
                pass
            else:
                print("\nOpção inválida! Tente novamente.")
                