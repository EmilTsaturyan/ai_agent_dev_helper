

class BaseAgent:
    def __init__(self, llm, system_prompt: str):
        self.llm = llm
        self.prompt = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": ""}
            ]
        }

    def run(self, input_text: str):
        self.prompt["messages"][1]["content"] = input_text
        return self.llm.invoke(self.prompt).get("messages")[-1].text