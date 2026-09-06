from servicos.produto_service import ProdutoService
from excecoes.lanchonete_error import LanchoneteError


class TelaProdutos:
    """Tela responsável pela interação com o usuário para gestão do cardápio."""

    def __init__(self, produto_service: ProdutoService) -> None:
        self.__service: ProdutoService = produto_service

    def cadastrar_suco(self) -> None:
        print("\n--- CADASTRAR SUCO ---")
        try:
            codigo: int = int(input("Código: "))
            nome: str = input("Nome do suco: ").strip()
            preco: float = float(input("Preço (R$): ").replace(",", "."))
            tamanho: str = input("Tamanho (Ex: 300ml, 500ml): ").strip()
            
            self.__service.cadastrar_suco(codigo, nome, preco, tamanho)
            print("\n[✓] Suco cadastrado com sucesso!")
        except ValueError:
            print("\n[!] Valores inválidos inseridos.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def cadastrar_sanduiche(self) -> None:
        print("\n--- CADASTRAR SANDUÍCHE ---")
        try:
            codigo: int = int(input("Código: "))
            nome: str = input("Nome do sanduíche: ").strip()
            preco: float = float(input("Preço (R$): ").replace(",", "."))
            pao: str = input("Tipo de Pão: ").strip()
            
            self.__service.cadastrar_sanduiche(codigo, nome, preco, pao)
            print("\n[✓] Sanduíche cadastrado com sucesso!")
        except ValueError:
            print("\n[!] Valores inválidos inseridos.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def cadastrar_salada_frutas(self) -> None:
        print("\n--- CADASTRAR SALADA DE FRUTAS ---")
        try:
            codigo: int = int(input("Código: "))
            nome: str = input("Nome: ").strip()
            preco: float = float(input("Preço (R$): ").replace(",", "."))
            adicional: str = input("Adicional (Ex: Leite condensado, Granola): ").strip()
            
            self.__service.cadastrar_salada_frutas(codigo, nome, preco, adicional)
            print("\n[✓] Salada de frutas cadastrada com sucesso!")
        except ValueError:
            print("\n[!] Valores inválidos inseridos.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def listar_produtos(self) -> None:
        print("\n--- CARDÁPIO ---")
        produtos = self.__service.listar_produtos()
        
        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        for prod in produtos:
            print(prod.descricao_detalhada())
            