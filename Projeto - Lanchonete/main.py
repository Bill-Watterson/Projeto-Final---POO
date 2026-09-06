from lanchonete import Lanchonete
from servicos.mesa_service import MesaService
from servicos.produto_service import ProdutoService
from servicos.atendimento_service import AtendimentoService
from interface.menus.menu_principal import MenuPrincipal


def main() -> None:
    # 1. Instancia a Aplicação (Dados em memória)
    app = Lanchonete()

    # 2. Instancia os Serviços (Regras de negócio)
    mesa_service = MesaService(app)
    produto_service = ProdutoService(app)
    atendimento_service = AtendimentoService(app, mesa_service, produto_service)

    # 3. Instancia a Interface (Injetando os serviços)
    menu = MenuPrincipal(mesa_service, produto_service, atendimento_service)
    
    # 4. Executa o sistema
    menu.executar()


if __name__ == "__main__":
    main()