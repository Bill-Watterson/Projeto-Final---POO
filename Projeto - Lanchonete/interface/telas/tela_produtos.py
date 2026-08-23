from typing import TYPE_CHECKING
from interface.tela import Tela
from excecoes.lanchonete_error import LanchoneteError

if TYPE_CHECKING:
    from lanchonete import Lanchonete


class TelaProdutos(Tela):
    def cadastrar_produto(self) -> None:
        print("\n--- CADASTRO DE PRODUTO ---")
        print("1 - Suco")
        print("2 - Sanduíche")
        print("3 - Salada de Frutas")
        tipo: str = input("Escolha o tipo: ").strip()

        try:
            codigo: int = int(input("Código: "))
            nome: str = input("Nome: ").strip()
            preco: float = float(input("Preço (R$): ").replace(",", "."))

            if tipo == "1":
                tamanho: str = input("Tamanho (ex: 300ml): ").strip()
                self._lanchonete.cadastrar_suco(codigo, nome, preco, tamanho)
            elif tipo == "2":
                pao: str = input("Tipo de pão: ").strip()
                self._lanchonete.cadastrar_sanduiche(codigo, nome, preco, pao)
            elif tipo == "3":
                adicional: str = input("Adicional: ").strip()
                self._lanchonete.cadastrar_salada_frutas(codigo, nome, preco, adicional)
            else:
                print("\n[!] Tipo inválido.")
                return

            print(f"\n[✓] Produto '{nome}' cadastrado com sucesso!")
        except ValueError:
            print("\n[!] Erro: Código e preço devem ser valores numéricos.")
        except LanchoneteError as e:
            print(f"\n[!] Erro: {e}")

    def listar_produtos(self) -> None:
        print("\n--- CARDÁPIO DE PRODUTOS ---")
        produtos = self._lanchonete.listar_produtos()
        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        for prod in produtos:
            print(f"Cód: {prod.codigo} | {prod.descricao_detalhada()} | R$ {prod.preco:.2f}")
