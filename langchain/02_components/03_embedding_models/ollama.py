from langchain_community.embeddings import OllamaEmbeddings

embeddings = (
    OllamaEmbeddings(
        base_url="http://10.10.6.4:11434",
        model="llamafamily/llama3-chinese-8b-instruct:latest",
    )
)

text = "这是一个测试文档"
# 查询单个文本
query_result = embeddings.embed_query(text)
print(query_result[:5])

# 查询文本列表
doc_result = embeddings.embed_documents([text])
print(doc_result[0][:5])
