from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# supports many more optional parameters. Hover on your `ChatOllama(...)`
# class to view the latest available supported parameters
llm = ChatOllama(
    base_url="http://10.10.6.4:11434",
    model="llamafamily/llama3-chinese-8b-instruct:latest")

# 定义提prompt模板
prompt = ChatPromptTemplate.from_template("告诉我一个短的笑话，关于{topic}")

# using LangChain Expressive Language chain syntax
# learn more about the LCEL on
# /docs/concepts/#langchain-expression-language-lcel
# langchain调用链，提示词 -> llm -> 字符串输出
chain = prompt | llm | StrOutputParser()

# for brevity, response is printed in terminal
# You can use LangServe to deploy your application for
# production
print(chain.invoke({"topic": "户外运动"}))
