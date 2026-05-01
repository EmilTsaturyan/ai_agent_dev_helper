from langchain_core.prompts import ChatPromptTemplate


class BaseAgent:
    def __init__(self, llm, system_prompt: str):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}")
        ])

    def run(self, input_text: str):
        return self.llm.invoke(self.prompt.format(input=input_text)).get("messages")[-1].text