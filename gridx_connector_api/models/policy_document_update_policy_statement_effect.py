from enum import Enum


class PolicyDocumentUpdatePolicyStatementEffect(str, Enum):
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
