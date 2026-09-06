from lanchonete import Lanchonete
from modelos.mesa import Mesa
from excecoes.lanchonete_error import MesaOcupadaError


class MesaService:
    """Serviço responsável pelas operações relacionadas às mesas."""

    def __init__(self, app: Lanchonete) -> None:
        self.__app: Lanchonete = app

    def cadastrar_mesa(self, numero: int) -> Mesa:
        if self.buscar_mesa(numero):
            raise MesaOcupadaError(f"Mesa {numero} já está cadastrada.")
        
        mesa = Mesa(numero)
        self.__app.mesas.append(mesa)
        return mesa

    def buscar_mesa(self, numero: int) -> Mesa | None:
        for mesa in self.__app.mesas:
            if mesa.numero == numero:
                return mesa
        return None

    def listar_mesas(self) -> list[Mesa]:
        return self.__app.mesas
