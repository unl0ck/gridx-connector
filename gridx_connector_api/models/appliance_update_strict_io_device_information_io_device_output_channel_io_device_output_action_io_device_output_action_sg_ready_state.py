from enum import Enum


class ApplianceUpdateStrictIODeviceInformationIODeviceOutputChannelIODeviceOutputActionIODeviceOutputActionSGReadyState(
    str, Enum
):
    AUTO = "AUTO"
    OFF = "OFF"
    ON = "ON"
    RECOMMEND_ON = "RECOMMEND_ON"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
