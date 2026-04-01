from enum import Enum


class GetSystemsSystemIDIncludeItem(str, Enum):
    ACCOUNTS = "accounts"
    APPLIANCEPRIORITIES = "appliancePriorities"
    GATEWAYS = "gateways"
    LOCATION = "location"
    PARENTID = "parentID"
    PRIORITIES = "priorities"
    PRODUCTOPTION = "productOption"
    STATUS = "status"
    VISIBLEAPPLIANCES = "visibleAppliances"
    VISIBLEFIELDS = "visibleFields"

    def __str__(self) -> str:
        return str(self.value)
