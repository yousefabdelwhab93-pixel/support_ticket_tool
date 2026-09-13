from pydantic import BaseModel
from typing import Literal


class SupportTicket(BaseModel):
    category: Literal[
        "donation_issue",
        "refund_request",
        "account_issue",
        "general_question",
        "technical_issue"
    ]

    priority: Literal[
        "low",
        "medium",
        "high"
    ]

    summary: str
    next_action: str