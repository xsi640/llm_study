from langchain_community.document_loaders import AsyncHtmlLoader

loader = AsyncHtmlLoader("https://docs.smith.langchain.com/user_guide")
docs = loader.load()
print(docs)