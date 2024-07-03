import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

class AnthropicClient:
    def __init__(self):
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        self.client = Anthropic(api_key=self.api_key)

    def query_claude(self, prompt):
        response = self.client.completions.create(
            model="claude-3-opus-20240229",
            max_tokens_to_sample=1000,
            prompt=prompt
        )
        return response.completion