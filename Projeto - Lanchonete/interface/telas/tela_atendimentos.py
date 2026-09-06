from servicos.atendimento_service import AtendimentoService
from excecoes.lanchonete_error import LanchoneteError


class TelaAtendimentos:
    """Tela responsável pela interação com o usuário para gestão de comandas."""

    def __init__(self, atendimento_service: AtendimentoService) -> None:
        self.__service: AtendimentoService = atendimento_service

    def abrir_atendimento(self) -> None:
        print("\n--- ABRIR ATENDIMENTO ---")
        try:
            num_mesa: int = int(input("Número da mesa: "))
            self.__service.abrir_atendimento(num_mesa)
            print(f"\n[✓] Atendimento iniciado para a Mesa {num_mesa}!")
        except ValueError:
            print("\n[!] Número de mesa inválido.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def consultar_atendimento(self) -> None:
        print("\n--- CONSULTAR COMANDA ---")
        try:
            num_mesa: int = int(input("Número da mesa: "))
            atendimento = self.__service.buscar_atendimento_ativo(num_mesa)

            print(f"\n=== COMANDA MESA {num_mesa} ===")
            print("PEDIDOS:")
            if not atendimento.pedidos:
                print("  (Nenhum pedido)")
            else:
                for p in atendimento.pedidos:
                    print(f"  - {p.quantidade}x {p.produto.nome} (R$ {p.valor_total:.2f})")

            print("\nPAGAMENTOS:")
            if not atendimento.pagamentos:
                print("  (Nenhum pagamento)")
            else:
                for i, pag in enumerate(atendimento.pagamentos, 1):
                    print(f"  - {i}º Pagamento: R$ {pag.valor:.2f}")

            print("-" * 30)
            print(f"TOTAL CONSUMIDO: R$ {atendimento.total:.2f}")
            print(f"TOTAL PAGO:      R$ {atendimento.total_pago:.2f}")
            print(f"SALDO RESTANTE:  R$ {atendimento.saldo:.2f}")
            print("-" * 30)
        except ValueError:
            print("\n[!] Número de mesa inválido.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def registrar_pedido(self) -> None:
        print("\n--- REGISTRAR PEDIDO ---")
        try:
            num_mesa: int = int(input("Número da mesa: "))
            cod_produto: int = int(input("Código do produto: "))
            quantidade: int = int(input("Quantidade: "))

            self.__service.registrar_pedido(num_mesa, cod_produto, quantidade)
            print("\n[✓] Pedido adicionado com sucesso!")
        except ValueError:
            print("\n[!] Digite números válidos.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def registrar_pagamento(self) -> None:
        print("\n--- REGISTRAR PAGAMENTO ---")
        try:
            num_mesa: int = int(input("Número da mesa: "))
            valor: float = float(input("Valor pago (R$): ").replace(",", "."))

            self.__service.registrar_pagamento(num_mesa, valor)
            print(f"\n[✓] Pagamento de R$ {valor:.2f} registrado!")
        except ValueError:
            print("\n[!] Valor inválido.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def encerrar_atendimento(self) -> None:
        print("\n--- ENCERRAR ATENDIMENTO ---")
        try:
            num_mesa: int = int(input("Número da mesa: "))
            self.__service.encerrar_atendimento(num_mesa)
            print(f"\n[✓] Atendimento da Mesa {num_mesa} encerrado e mesa liberada!")
        except ValueError:
            print("\n[!] Número de mesa inválido.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def consultar_historico(self) -> None:
        print("\n--- HISTÓRICO DE ATENDIMENTOS ENCERRADOS ---")
        historico = self.__service.consultar_historico()

        if not historico:
            print("Nenhum atendimento encerrado até o momento.")
            return

        for at in historico:
            print(f"Mesa {at.mesa.numero} | Total Quitado: R$ {at.total:.2f} | Status: Encerrado")
            