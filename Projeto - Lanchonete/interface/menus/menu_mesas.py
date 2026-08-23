from typing import TYPE_CHECKING
from interface.menu import Menu
from interface.telas.tela_mesas import TelaMesas

if TYPE_CHECKING:
    from lanchonete import Lanchonete


class MenuMesas(Menu):
    def __init__(self, lanchonete: "Lanchonete") -> None:
        super().__init__(lanchonete)
        self.__tela = TelaMesas(lanchonete)

    def executar(self) -> None:
        opcao: str = ""
        while opcao != "0":
            print("\n--- MENU DE MESAS ---")
            print("1 - Cadastrar Mesa")
            print("2 - Listar Mesas")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.__tela.cadastrar_mesa()
            elif opcao == "2":
                self.__tela.listar_mesas()
            elif opcao == "0":
                pass
            else:
                print("\nOpção inválida! Tente novamente.")
