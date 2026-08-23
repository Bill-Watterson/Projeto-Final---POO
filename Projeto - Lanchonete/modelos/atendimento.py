from modelos.mesa import Mesa
from modelos.pedido import Pedido
from modelos.pagamento import Pagamento
from excecoes.lanchonete_error import (
    AtendimentoEncerradoError,
    PagamentoInvalidoError,
    AtendimentoNaoQuitadoError,
)


class Atendimento:
    """Representa a comanda associada a uma mesa."""

    def __init__(self, mesa: Mesa) -> None:
        self.__mesa: Mesa = mesa
        self.__pedidos: list[Pedido] = []
        self.__pagamentos: list[Pagamento] = []
        self.__ativo: bool = True
        self.__mesa.ocupar()

    @property
    def mesa(self) -> Mesa:
        return self.__mesa

    @property
    def pedidos(self) -> list[Pedido]:
        return self.__pedidos.copy()

    @property
    def pagamentos(self) -> list[Pagamento]:
        return self.__pagamentos.copy()

    @property
    def ativo(self) -> bool:
        return self.__ativo

    @property
    def total(self) -> float:
        return sum(pedido.valor_total for pedido in self.__pedidos)

    @property
    def total_pago(self) -> float:
        return sum(pagamento.valor for pagamento in self.__pagamentos)

    @property
    def saldo(self) -> float:
        return self.total - self.total_pago

    def adicionar_pedido(self, pedido: Pedido) -> None:
        if not self.__ativo:
            raise AtendimentoEncerradoError("Não é possível adicionar pedidos a um atendimento encerrado.")
        self.__pedidos.append(pedido)

    def registrar_pagamento(self, pagamento: Pagamento) -> None:
        if not self.__ativo:
            raise AtendimentoEncerradoError("Não é possível registrar pagamentos em um atendimento encerrado.")
        if pagamento.valor <= 0:
            raise PagamentoInvalidoError("O valor do pagamento deve ser maior que zero.")
        if pagamento.valor > self.saldo:
            raise PagamentoInvalidoError(f"Valor (R$ {pagamento.valor:.2f}) excede o saldo restante (R$ {self.saldo:.2f}).")

        self.__pagamentos.append(pagamento)

    def encerrar(self) -> None:
        if not self.__ativo:
            raise AtendimentoEncerradoError("O atendimento já está encerrado.")
        if self.saldo > 0:
            raise AtendimentoNaoQuitadoError(f"Não é possível encerrar atendimento com saldo pendente de R$ {self.saldo:.2f}.")

        self.__ativo = False
        self.__mesa.desocupar()
