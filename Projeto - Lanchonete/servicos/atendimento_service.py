from lanchonete import Lanchonete
from modelos.atendimento import Atendimento
from modelos.pedido import Pedido
from modelos.pagamento import Pagamento
from servicos.mesa_service import MesaService
from servicos.produto_service import ProdutoService
from excecoes.lanchonete_error import (
    MesaNaoEncontradaError,
    MesaOcupadaError,
    AtendimentoNaoEncontradoError,
    ProdutoNaoEncontradoError,
    QuantidadeInvalidaError
)


class AtendimentoService:
    """Serviço responsável por coordenar a abertura, pedidos, pagamentos e encerramento de comandas."""

    def __init__(self, app: Lanchonete, mesa_service: MesaService, produto_service: ProdutoService) -> None:
        self.__app: Lanchonete = app
        self.__mesa_service: MesaService = mesa_service
        self.__produto_service: ProdutoService = produto_service

    def abrir_atendimento(self, num_mesa: int) -> Atendimento:
        mesa = self.__mesa_service.buscar_mesa(num_mesa)
        if not mesa:
            raise MesaNaoEncontradaError(f"Mesa {num_mesa} não cadastrada.")
        if mesa.ocupada:
            raise MesaOcupadaError(f"Mesa {num_mesa} já está ocupada.")

        atendimento = Atendimento(mesa)
        self.__app.atendimentos.append(atendimento)
        return atendimento

    def buscar_atendimento_ativo(self, num_mesa: int) -> Atendimento:
        mesa = self.__mesa_service.buscar_mesa(num_mesa)
        if not mesa:
            raise MesaNaoEncontradaError(f"Mesa {num_mesa} não cadastrada.")

        for at in self.__app.atendimentos:
            if at.mesa.numero == num_mesa and at.ativo:
                return at
        raise AtendimentoNaoEncontradoError(f"Não há atendimento ativo para a Mesa {num_mesa}.")

    def registrar_pedido(self, num_mesa: int, cod_produto: int, quantidade: int) -> Pedido:
        if quantidade <= 0:
            raise QuantidadeInvalidaError("A quantidade do pedido deve ser maior que zero.")

        atendimento = self.buscar_atendimento_ativo(num_mesa)
        produto = self.__produto_service.buscar_produto(cod_produto)

        if not produto:
            raise ProdutoNaoEncontradoError(f"Produto {cod_produto} não encontrado.")

        pedido = Pedido(produto, quantidade)
        atendimento.adicionar_pedido(pedido)
        return pedido

    def registrar_pagamento(self, num_mesa: int, valor: float) -> Pagamento:
        atendimento = self.buscar_atendimento_ativo(num_mesa)
        pagamento = Pagamento(valor)
        atendimento.registrar_pagamento(pagamento)
        return pagamento

    def encerrar_atendimento(self, num_mesa: int) -> None:
        atendimento = self.buscar_atendimento_ativo(num_mesa)
        atendimento.encerrar()
        self.__app.historico.append(atendimento)

    def consultar_historico(self) -> list[Atendimento]:
        return self.__app.historico
