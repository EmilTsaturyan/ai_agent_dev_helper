from agent.builder import build_agent

    
agent = build_agent()

prompt = "Review the project and give me a summary of the project."
response = agent.invoke({
    "messages": [
        {"role": "user", "content": prompt}
    ]
})
print(response.get("messages")[-1].text)
