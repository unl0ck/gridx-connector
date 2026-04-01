from enum import Enum


class GetSystemsIncludeItem(str, Enum):
    ACCOUNTS = "accounts"
    GATEWAYS = "gateways"
    GATEWAYS_ADDITIONALIDENTIFIERS = "gateways.additionalIdentifiers"
    GATEWAYS_APPLIANCECOMPOSITION = "gateways.applianceComposition"
    GATEWAYS_CONNECTIONSTATUS = "gateways.connectionStatus"
    LOCATION = "location"
    PARENTID = "parentID"
    PRODUCTOPTION = "productOption"
    STATUS = "status"
    VISIBLEAPPLIANCES = "visibleAppliances"
    VISIBLEFIELDS = "visibleFields"

    def __str__(self) -> str:
        return str(self.value)
