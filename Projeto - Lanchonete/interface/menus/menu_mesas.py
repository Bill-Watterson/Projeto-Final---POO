from servicos.mesa_service import MesaService
from interface.telas.tela_mesas import TelaMesas


class MenuMesas:
    def __init__(self, mesa_service: MesaService) -> None:
        self.__tela = TelaMesas(mesa_service)

    def executar(self) -> None:
        opcao: str = ""
        while opcao != "0":
            print("\n--- MENU DE MESAS ---")
            print("1 - Cadastrar mesa")
            print("2 - Listar mesas")
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
                