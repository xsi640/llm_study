from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import MarkdownifyTransformer

urls = ["https://lilianweng.github.io/posts/2023-06-23-agent/"]
loader = AsyncHtmlLoader(urls)
docs = loader.load()

md = MarkdownifyTransformer()
converted_docs = md.transform_documents(docs)

print(converted_docs[0].page_content[:1000])