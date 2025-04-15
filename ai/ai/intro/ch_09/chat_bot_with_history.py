from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

## 按照 session_id 存储会话历史
session_store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


## 能记住聊天历史的机器人
## 这里使用了基于内存的消息历史记忆
def run_chat_bot_with_history():
    model_with_msg_history = RunnableWithMessageHistory(
        ChatOpenAI(model='gpt-4o-mini'),
        get_session_history
    )
    config = {'configurable': {'session_id': 'Tao'}}

    while True:
        user_input = input('您 >> ')
        if user_input.lower() == 'exit':
            break

        stream = model_with_msg_history.stream(
            [HumanMessage(content=user_input)],
            config=config
        )

        for resp in stream:
            print(resp.content, end='', flush=True)

        print()


## 通过提示词模板，给系统设定角色
def run_chat_bot_with_history_as_LuXun():
    chat_model = ChatOpenAI(model='gpt-4o-mini')

    ## 实际上，我们设定好的提示词每次都会与用户的实际输入，一起发送给大模型
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', '你现在扮演鲁迅，以他的口吻和风格跟我进行对话'),
            MessagesPlaceholder(variable_name='msg') ## 消息列表占位符
        ]
    )

    model = RunnableWithMessageHistory(
        prompt | chat_model,
        get_session_history
    )

    config = {'configurable': {'session_id': 'TAO'}}

    while True:
        user_input = input('您> ')
        if user_input.lower() == 'exit':
            break

        stream = model.stream(
            {'msg': [HumanMessage(content=user_input)]},
            config
        )

        for resp in stream:
            print(resp.content, end='', flush=True)
        print()


if __name__ == '__main__':
    # run_chat_bot_with_history()
    run_chat_bot_with_history_as_LuXun()