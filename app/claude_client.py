from anthropic import Anthropic
from app.config import ANTHROPIC_API_KEY, MODEL_NAME

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def send_prompt(prompt: str) -> str:
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text