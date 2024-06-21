from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
import langchain

langchain.debug = True

# https://api.python.langchain.com/en/latest/llms/langchain_experimental.llms.ollama_functions.OllamaFunctions.html
# OllamaFunctions
model = OllamaFunctions(
    base_url="http://10.10.6.4:11434",
    model="llamafamily/llama3-chinese-8b-instruct:latest")

# 定义并绑定tools
model = model.bind_tools(
    tools=[
        {
            "name": "get_current_weather",
            "description": "获取当前位置的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或者地区, 例如：北京",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["摄氏度", "华氏度"],
                    },
                },
                "required": ["地区"],
            },
        }
    ],
    function_call={"name": "get_current_weather"},
)

answer = model.invoke("北京的天气?")
print("answer: ", answer)
