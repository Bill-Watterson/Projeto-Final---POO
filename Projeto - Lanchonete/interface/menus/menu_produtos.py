from typing import TYPE_CHECKING
from interface.menu import Menu
from interface.telas.tela_produtos import TelaProdutos

if TYPE_CHECKING:
    from lanchonete import Lanchonete


class MenuProdutos(Menu):
    def __init__(self, lanchonete: "Lanchonete") -> None:
        super().__init__(lanchonete)
        self.__tela = TelaProdutos(lanchonete)

    def executar(self) -> None:
        opcao: str = ""
        while opcao != "0":
            print("\n--- MENU DE PRODUTOS ---")
            print("1 - Cadastrar Produto")
            print("2 - Listar Produtos")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.__tela.cadastrar_produto()
            elif opcao == "2":
                self.__tela.listar_produtos()
            elif opcao == "0":
                pass
            else:
                print("\nOpção inválida! Tente novamente.")
