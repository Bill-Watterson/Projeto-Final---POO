from typing import TYPE_CHECKING
from interface.tela import Tela
from excecoes.lanchonete_error import LanchoneteError

if TYPE_CHECKING:
    from lanchonete import Lanchonete


class TelaMesas(Tela):
    def cadastrar_mesa(self) -> None:
        print("\n--- CADASTRO DE MESA ---")
        try:
            numero: int = int(input("Número da mesa: "))
            self._lanchonete.cadastrar_mesa(numero)
            print(f"\n[✓] Mesa {numero} cadastrada com sucesso!")
        except ValueError:
            print("\n[!] Erro: O número da mesa deve ser um valor inteiro válido.")
        except LanchoneteError as e:
            print(f"\n[!] Erro: {e}")

    def listar_mesas(self) -> None:
        print("\n--- LISTA DE MESAS ---")
        mesas = self._lanchonete.listar_mesas()
        if not mesas:
            print("Nenhuma mesa cadastrada.")
            return

        for mesa in mesas:
            status = "Ocupada" if mesa.ocupada else "Disponível"
            print(f"Mesa Nº {mesa.numero} | Status: {status}")
