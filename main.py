import anthropic
from dotenv import load_dotenv

# Load environment keys, the anthropic one
load_dotenv()

client = anthropic.Anthropic() # Actual client for anthropic

# An API call
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024, # Max length of response
    messages=[
        {
            "role": "user",
            "content": "Hey, are you a scam? Reply suspiciously."
        }
    ]
)

print(message.content[0].text)