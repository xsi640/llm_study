from langchain_community.llms import Ollama

llm = Ollama(
    base_url="http://10.10.6.4:11434",
    model="llamafamily/llama3-chinese-8b-instruct:latest")

# 输出
# answer = llm.invoke("告诉我一个笑话")
# print(answer)


# stream输出
for chunks in llm.stream("告诉我一个笑话"):
    print(chunks)
