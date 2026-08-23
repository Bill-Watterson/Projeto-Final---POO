from excecoes.lanchonete_error import LanchoneteError

class MesaOcupadaError(LanchoneteError):
    """Lançada ao tentar abrir atendimento em uma mesa já ocupada."""
    def __init__(self, numero: int) -> None:
        super().__init__(f"A mesa {numero} já está ocupada.")

class AtendimentoEncerradoError(LanchoneteError):
    """Lançada ao tentar alterar comanda já fechada."""
    def __init__(self) -> None:
        super().__init__("Não é possível realizar operações em um atendimento encerrado.")

class PagamentoInvalidoError(LanchoneteError):
    """Lançada quando o pagamento é menor/igual a zero ou maior que o saldo."""
    def __init__(self, mensagem: str = "Valor de pagamento inválido.") -> None:
        super().__init__(mensagem)

class AtendimentoNaoQuitadoError(LanchoneteError):
    """Lançada ao tentar encerrar uma comanda com saldo devedor."""
    def __init__(self, saldo: float) -> None:
        super().__init__(f"Não é possível encerrar. Saldo pendente: R$ {saldo:.2f}")
        