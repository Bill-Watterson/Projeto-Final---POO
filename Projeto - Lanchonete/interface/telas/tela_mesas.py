from servicos.mesa_service import MesaService
from excecoes.lanchonete_error import LanchoneteError


class TelaMesas:
    """Tela responsável pela interação com o usuário para gestão de mesas."""

    def __init__(self, mesa_service: MesaService) -> None:
        self.__service: MesaService = mesa_service

    def cadastrar_mesa(self) -> None:
        print("\n--- CADASTRAR MESA ---")
        try:
            numero: int = int(input("Digite o número da nova mesa: "))
            self.__service.cadastrar_mesa(numero)
            print(f"\n[✓] Mesa {numero} cadastrada com sucesso!")
        except ValueError:
            print("\n[!] Número inválido. Digite apenas números inteiros.")
        except LanchoneteError as e:
            print(f"\n[!] Erro de Negócio: {e}")

    def listar_mesas(self) -> None:
        print("\n--- LISTA DE MESAS ---")
        mesas = self.__service.listar_mesas()
        
        if not mesas:
            print("Nenhuma mesa cadastrada no sistema.")
            return

        for mesa in mesas:
            status = "Ocupada" if mesa.ocupada else "Livre"
            print(f"Mesa {mesa.numero} - Status: {status}")