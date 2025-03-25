from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

## 非常简单的聊天机器人
## 无法记住聊天历史
## 输入 exit 即可退出对话
def run_simple_chat_bot():
    model = ChatOpenAI(model='gpt-4o-mini')

    while True:
        user_input = input("你 > ")
        if user_input.lower() == 'exit':
            break

        stream = model.stream([HumanMessage(content=user_input)])

        for resp_chunk in stream:
            print(resp_chunk.content, end='', flush=True)

        print()


if __name__ == '__main__':
    run_simple_chat_bot()