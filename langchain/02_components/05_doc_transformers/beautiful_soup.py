from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer

# Load HTML
loader = AsyncChromiumLoader(["https://www.baidu.com"])
html = loader.load()

bs_transformer = BeautifulSoupTransformer()
docs_transformed = bs_transformer.transform_documents(
    html, tags_to_extract=["p", "a"]
)

print(docs_transformed[0].page_content[0:500])
