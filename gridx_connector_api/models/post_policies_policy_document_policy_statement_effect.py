from enum import Enum


class PostPoliciesPolicyDocumentPolicyStatementEffect(str, Enum):
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
