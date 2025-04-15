from operator import itemgetter

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_core.vectorstores import VectorStoreRetriever
from ai.intro.ch11.hello_vector_store import get_vector_store
from ai.intro.tool.chat_models import LOCAL_DEEPSEEK_MODEL

## 这就是 RAG 里面的 "R".
## Retriever 的核心能力是根据文本查询出对应的 Document
## Retriever 是一个接口，除了向量数据库，还可以支持其他的实现，
## 例如 WikipediaRetriever
retriever: VectorStoreRetriever = get_vector_store().as_retriever(search_type='similarity')


session_history_store = {}

def get_session_history(session_id: str):
    if session_id not in session_history_store:
        session_history_store[session_id] = InMemoryChatMessageHistory()
    return session_history_store[session_id]


chat_model = LOCAL_DEEPSEEK_MODEL


## 这个提示词模板，包含了：
##   - 上下文（context），也就是根据问题从向量数据库检索出来的内容
##   - 聊天历史
##   - 用户问题
prompt = ChatPromptTemplate.from_messages([
    (
        'system',
        """你是一个简洁的问题回答助手。请严格遵守以下规则：
        1. 只输出最终答案，不要包含任何思考过程、推理步骤或解释
        2. 如果答案不在提供的上下文中，直接回答【俺不知道】
        3. 回答尽可能简短，不超过2句话
        
        context：{context}"""
    ),
    MessagesPlaceholder(variable_name='history'),
    (
        'human', '{question}'
    )
])


## retriever 检索的结果是一个文档列表，我们必须把它们转化成文本后，
## 才能传给大模型
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

context = itemgetter('question') | retriever | format_docs
first_step = RunnablePassthrough.assign(context=context)
chain = first_step | prompt | chat_model

config = {'configurable': {'session_id': 'TaoXiao'}}

with_rag_and_history = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_history,
    input_messages_key='question',
    history_messages_key='history'
)

if __name__ == '__main__':
    while True:
        user_input = input('你> ')
        if user_input.lower() == 'exit':
            print('再见 👋')
            break

        stream = with_rag_and_history.stream(
            {'question': user_input},
            config=config
        )

        for chunk in stream:
            print(chunk.content, end='', flush=True)

        print()