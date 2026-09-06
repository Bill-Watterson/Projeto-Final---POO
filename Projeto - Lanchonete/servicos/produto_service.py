from lanchonete import Lanchonete
from modelos.produto import Produto, Suco, Sanduiche, SaladaDeFrutas
from excecoes.lanchonete_error import ProdutoNaoEncontradoError


class ProdutoService:
    """Serviço responsável pelas operações relacionadas ao cardápio e produtos."""

    def __init__(self, app: Lanchonete) -> None:
        self.__app: Lanchonete = app

    def cadastrar_suco(self, codigo: int, nome: str, preco: float, tamanho: str) -> Suco:
        self.__verificar_codigo_existente(codigo)
        suco = Suco(codigo, nome, preco, tamanho)
        self.__app.produtos.append(suco)
        return suco

    def cadastrar_sanduiche(self, codigo: int, nome: str, preco: float, pao: str) -> Sanduiche:
        self.__verificar_codigo_existente(codigo)
        sanduiche = Sanduiche(codigo, nome, preco, pao)
        self.__app.produtos.append(sanduiche)
        return sanduiche

    def cadastrar_salada_frutas(self, codigo: int, nome: str, preco: float, adicional: str) -> SaladaDeFrutas:
        self.__verificar_codigo_existente(codigo)
        salada = SaladaDeFrutas(codigo, nome, preco, adicional)
        self.__app.produtos.append(salada)
        return salada

    def buscar_produto(self, codigo: int) -> Produto | None:
        for prod in self.__app.produtos:
            if prod.codigo == codigo:
                return prod
        return None

    def listar_produtos(self) -> list[Produto]:
        return self.__app.produtos

    def __verificar_codigo_existente(self, codigo: int) -> None:
        if self.buscar_produto(codigo):
            raise ProdutoNaoEncontradoError(f"O Produto com código {codigo} já existe.")
