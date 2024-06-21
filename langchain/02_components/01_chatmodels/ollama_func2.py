from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.llms.ollama_functions import OllamaFunctions
import langchain

langchain.debug = True

# 通过schema格式化输出
# 定义schema
class Person(BaseModel):
    name: str = Field(description="姓名", required=True)
    height: float = Field(description="身高", required=True)
    hair_color: str = Field(description="头发颜色")


# Prompt template
prompt = PromptTemplate.from_template(
    """张三身高180cm,
    李四比张三高20cm，跳的比他高，
    张三是黑色头发，李四是金色头发。
    
人名: {question}
AI: """
)

# Chain
llm = OllamaFunctions(base_url="http://10.10.6.4:11434",
                      model="llamafamily/llama3-chinese-8b-instruct:latest",
                      format="json", temperature=0)
structured_llm = llm.with_structured_output(Person)
chain = prompt | structured_llm

alex = chain.invoke("描述张三")
print(alex)

claudia = chain.invoke("描述李四")
print(claudia)
