from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

## 展示：
##  - 创建一个向量数据库实例
##  - 从本地文件加载文本信息，生成 documents
##  - 将 documents 进行 split
##  - 把 splits【索引进】向量数据库

loader = TextLoader('story.txt')
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=200)
doc_splits = splitter.split_documents(docs)

# 使用 HuggingFace 的开源模型替代 OpenAIEmbeddings
# 需要设置环境变量 export HF_ENDPOINT=https://hf-mirror.com
# 否则在大陆无法下载 Hugging Face 的模型
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma(
    collection_name='hello_vector',
    embedding_function=embeddings,
    persist_directory='hello-db'
)

vector_store.add_documents(doc_splits)


if __name__ == '__main__':
    # 查询相关文档
    # 它并不返回问题的直接答案
    # 而只是返回与问题最相关的几个文档
    result = vector_store.similarity_search("这个故事里有几个主人公？")
    print(result)