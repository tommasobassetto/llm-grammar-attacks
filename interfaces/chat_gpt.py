import getpass
from openai import OpenAI

from interfaces.base import BaseInterface

class GPTInterface (BaseInterface):

    client: OpenAI

    """ChatGPT interface, split from the rest of the code for transferability"""
    def getToken(self) -> None:
        api_key = getpass.getpass("Please enter your API key for ChatGPT: ")
        self.client = OpenAI(
            api_key=api_key
        )
        print("Succesfully connected to OpenAI client.")

    def call(self, query: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": query}
            ],
        )

        return response.choices[0].message.content
