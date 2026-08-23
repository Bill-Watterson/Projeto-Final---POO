class LanchoneteError(Exception):
    """Exceção base para erros do sistema."""
    pass


class MesaOcupadaError(LanchoneteError):
    pass


class MesaNaoEncontradaError(LanchoneteError):
    pass


class AtendimentoEncerradoError(LanchoneteError):
    pass


class AtendimentoNaoEncontradoError(LanchoneteError):
    pass


class ProdutoNaoEncontradoError(LanchoneteError):
    pass


class QuantidadeInvalidaError(LanchoneteError):
    pass


class PagamentoInvalidoError(LanchoneteError):
    pass


class AtendimentoNaoQuitadoError(LanchoneteError):
    pass
