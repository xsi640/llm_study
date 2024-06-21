from langchain_community.document_loaders import TextLoader

loader = TextLoader("biography-of-john-doe.txt")
docs = loader.load()
print(docs)