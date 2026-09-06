from servicos.mesa_service import MesaService
from servicos.produto_service import ProdutoService
from servicos.atendimento_service import AtendimentoService
from interface.menus.menu_mesas import MenuMesas
from interface.menus.menu_produtos import MenuProdutos
from interface.menus.menu_atendimentos import MenuAtendimentos


class MenuPrincipal:
    def __init__(self, mesa_service: MesaService, produto_service: ProdutoService, atendimento_service: AtendimentoService) -> None:
        self.__menu_mesas = MenuMesas(mesa_service)
        self.__menu_produtos = MenuProdutos(produto_service)
        self.__menu_atendimentos = MenuAtendimentos(atendimento_service)

    def executar(self) -> None:
        opcao: str = ""
        while opcao != "0":
            print("\n" + "=" * 40)
            print("   SABOR DA ORLA - SISTEMA DE COMANDAS")
            print("=" * 40)
            print("1 - Gerenciar Mesas")
            print("2 - Gerenciar Produtos")
            print("3 - Gerenciar Atendimentos")
            print("0 - Sair")
            print("=" * 40)

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.__menu_mesas.executar()
            elif opcao == "2":
                self.__menu_produtos.executar()
            elif opcao == "3":
                self.__menu_atendimentos.executar()
            elif opcao == "0":
                print("\nEncerrando a aplicação...")
            else:
                print("\nOpção inválida! Tente novamente.")
                