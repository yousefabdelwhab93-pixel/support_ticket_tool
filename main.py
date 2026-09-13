import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from prompts import SYSTEM_PROMPT
from models import SupportTicket


# Load environment variables
load_dotenv()


# Create Inception Labs client
client = OpenAI(
    api_key=os.getenv("INCEPTION_API_KEY"),
    base_url="https://api.inceptionlabs.ai/v1"
)


# Messy donor message
donor_message = """
Hi, I donated $50 yesterday but I see two charges
on my bank account. Can you please check this?
"""


# Put the donor message inside a clear data boundary
user_prompt = f"""
<donor_message>
{donor_message}
</donor_message>
"""


# Send the request to the LLM
response = client.chat.completions.create(
    model="mercury-2.5",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    temperature=0.5,
    max_tokens=2000
)


# Get the model response
result = response.choices[0].message.content

print("\nRaw model response:")
print(result)


# Convert JSON string into Python dictionary
data = json.loads(result)


# Validate the output using Pydantic
ticket = SupportTicket(**data)


# Print the final validated ticket
print("\nValidated support ticket:")
print(ticket.model_dump_json(indent=4))