from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

## 能记住聊天历史的机器人
## 这里使用了基于内存的消息历史记忆
def run_chat_bot_with_history():
    session_store = {}

    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in session_store:
            session_store[session_id] = InMemoryChatMessageHistory()
        return session_store[session_id]

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


if __name__ == '__main__':
    run_chat_bot_with_history()