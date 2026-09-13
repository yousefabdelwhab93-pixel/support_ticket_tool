FEW_SHOT_EXAMPLES = """
### FEW-SHOT EXAMPLES

Example 1:

<donor_message>
I donated $100 last week but I don't see the donation.
</donor_message>

Output:
{
    "category": "donation_issue",
    "priority": "medium",
    "summary": "Donor cannot see a recent donation.",
    "next_action": "Check the donation record and payment status."
}


Example 2:

<donor_message>
Please refund my $50 donation. I changed my mind.
</donor_message>

Output:
{
    "category": "refund_request",
    "priority": "medium",
    "summary": "Donor is requesting a refund.",
    "next_action": "Review the refund policy and process the request if eligible."
}


Example 3:

<donor_message>
I can't log into my donor account. The password reset email never arrives.
</donor_message>

Output:
{
    "category": "account_issue",
    "priority": "high",
    "summary": "Donor cannot access their account.",
    "next_action": "Check the account and password-reset process."
}
"""