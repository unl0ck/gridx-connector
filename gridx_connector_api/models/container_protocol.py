from enum import Enum


class ContainerProtocol(str, Enum):
    EEBUS = "EEBUS"
    HTTP_REST = "HTTP_REST"
    MODBUS_RTU = "MODBUS_RTU"
    MODBUS_TCP = "MODBUS_TCP"
    OCPP = "OCPP"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
