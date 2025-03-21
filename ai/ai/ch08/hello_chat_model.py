from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

messages = [
    SystemMessage('Translate the following from English to Chinese'),
    HumanMessage('Hello, everyone! I love you all!')
]

## 使用 init_chat_model
def run_init_chat_model():
    ## lang chain 通用的 chat model
    ## 需要指定 provider
    model = init_chat_model('gpt-4o-mini', model_provider='openai')
    result = model.invoke(messages)
    print(result)


## 直接使用 ChatOpenAI
def run_chat_openai():
    ## 这是 openai 提供好的 chat model 实现
    model = ChatOpenAI(model='gpt-4o-mini')
    result = model.invoke(messages)
    print(result)

## 假定环境变量 OPENAI_API_KEY 已经存在
if __name__ == '__main__':
    # run_init_chat_model()
    run_chat_openai()