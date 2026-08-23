from modelos.mesa import Mesa
from modelos.produto import Produto, Suco, Sanduiche, SaladaDeFrutas
from modelos.atendimento import Atendimento
from modelos.pedido import Pedido
from modelos.pagamento import Pagamento
from excecoes.lanchonete_error import (
    MesaOcupadaError,
    MesaNaoEncontradaError,
    ProdutoNaoEncontradoError,
    AtendimentoNaoEncontradoError,
    QuantidadeInvalidaError,
)


class Lanchonete:
    """Classe principal de gerenciamento do sistema em memória."""

    def __init__(self) -> None:
        self.__mesas: list[Mesa] = []
        self.__produtos: list[Produto] = []
        self.__atendimentos: list[Atendimento] = []
        self.__historico: list[Atendimento] = []

    # --- Mesas ---
    def cadastrar_mesa(self, numero: int) -> Mesa:
        if self.buscar_mesa(numero):
            raise MesaOcupadaError(f"Mesa {numero} já está cadastrada.")
        mesa = Mesa(numero)
        self.__mesas.append(mesa)
        return mesa

    def buscar_mesa(self, numero: int) -> Mesa | None:
        for mesa in self.__mesas:
            if mesa.numero == numero:
                return mesa
        return None

    def listar_mesas(self) -> list[Mesa]:
        return self.__mesas

    # --- Produtos ---
    def cadastrar_suco(self, codigo: int, nome: str, preco: float, tamanho: str) -> Suco:
        if self.buscar_produto(codigo):
            raise ProdutoNaoEncontradoError(f"Produto {codigo} já existe.")
        suco = Suco(codigo, nome, preco, tamanho)
        self.__produtos.append(suco)
        return suco

    def cadastrar_sanduiche(self, codigo: int, nome: str, preco: float, pao: str) -> Sanduiche:
        if self.buscar_produto(codigo):
            raise ProdutoNaoEncontradoError(f"Produto {codigo} já existe.")
        sanduiche = Sanduiche(codigo, nome, preco, pao)
        self.__produtos.append(sanduiche)
        return sanduiche

    def cadastrar_salada_frutas(self, codigo: int, nome: str, preco: float, adicional: str) -> SaladaDeFrutas:
        if self.buscar_produto(codigo):
            raise ProdutoNaoEncontradoError(f"Produto {codigo} já existe.")
        salada = SaladaDeFrutas(codigo, nome, preco, adicional)
        self.__produtos.append(salada)
        return salada

    def buscar_produto(self, codigo: int) -> Produto | None:
        for prod in self.__produtos:
            if prod.codigo == codigo:
                return prod
        return None

    def listar_produtos(self) -> list[Produto]:
        return self.__produtos

    # --- Atendimentos ---
    def abrir_atendimento(self, num_mesa: int) -> Atendimento:
        mesa = self.buscar_mesa(num_mesa)
        if not mesa:
            raise MesaNaoEncontradaError(f"Mesa {num_mesa} não cadastrada.")
        if mesa.ocupada:
            raise MesaOcupadaError(f"Mesa {num_mesa} já está ocupada.")

        atendimento = Atendimento(mesa)
        self.__atendimentos.append(atendimento)
        return atendimento

    def buscar_atendimento_ativo_por_mesa(self, num_mesa: int) -> Atendimento:
        mesa = self.buscar_mesa(num_mesa)
        if not mesa:
            raise MesaNaoEncontradaError(f"Mesa {num_mesa} não cadastrada.")

        for at in self.__atendimentos:
            if at.mesa.numero == num_mesa and at.ativo:
                return at
        raise AtendimentoNaoEncontradoError(f"Não há atendimento ativo para a Mesa {num_mesa}.")

    def registrar_pedido(self, num_mesa: int, cod_produto: int, quantidade: int) -> Pedido:
        if quantidade <= 0:
            raise QuantidadeInvalidaError("A quantidade deve ser maior que zero.")

        atendimento = self.buscar_atendimento_ativo_por_mesa(num_mesa)
        produto = self.buscar_produto(cod_produto)

        if not produto:
            raise ProdutoNaoEncontradoError(f"Produto {cod_produto} não encontrado.")

        pedido = Pedido(produto, quantidade)
        atendimento.adicionar_pedido(pedido)
        return pedido

    def registrar_pagamento(self, num_mesa: int, valor: float) -> Pagamento:
        atendimento = self.buscar_atendimento_ativo_por_mesa(num_mesa)
        pagamento = Pagamento(valor)
        atendimento.registrar_pagamento(pagamento)
        return pagamento

    def encerrar_atendimento(self, num_mesa: int) -> None:
        atendimento = self.buscar_atendimento_ativo_por_mesa(num_mesa)
        atendimento.encerrar()
        self.__historico.append(atendimento)

    def consultar_historico(self) -> list[Atendimento]:
        return self.__historico
