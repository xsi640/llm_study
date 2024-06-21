# import
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
import langchain

langchain.debug = True

# load the document and split it into chunks
loader = TextLoader("./state_of_the_union.txt", encoding="utf8")
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embeddings = OllamaEmbeddings(
    base_url="http://10.10.6.4:11434",
    model="llamafamily/llama3-chinese-8b-instruct:latest",
)

# load it into Chroma
db = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db")

# query it
query = "What did the president say about Ketanji Brown Jackson"
# docs = db.similarity_search(query)
docs = db.similarity_search_with_score(query)

# print results
print(docs[0])
