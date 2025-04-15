from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

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


## 直接使用【ChatOpenAI】
def run_chat_openai():
    ## 这是 openai 提供好的 chat model 实现
    model = ChatOpenAI(model='gpt-4o-mini')
    result = model.invoke(messages)
    print(result)


## 【异步】模式接收结果
def run_chat_openai_async():
    model = ChatOpenAI(model='gpt-4o-mini')
    stream = model.stream(messages)

    for response in stream:
        print(response.content, end='|')


## 试试【提示词模板】
def run_with_prompt_template():
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', '请将下列中文翻译成英语'),
            ('user', '{text}')
        ]
    )

    model = ChatOpenAI(model='gpt-4o-mini')

    prompt = prompt_template.invoke({
        'text': '床前明月光，疑是地上霜！'
    })
    print(f"prompt 的实际内容是 {prompt}")

    chain = prompt_template | model
    stream = chain.stream({
        'text': '床前明月光，疑是地上霜！'
    })

    for response in stream:
        print(response.content, end='|')


## 试试 【Output Parser】
def run_with_output_parser():
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', '请将下列中文翻译成英语'),
            ('user', '{user-text}')
        ]
    )

    model = ChatOpenAI(model='gpt-4o-mini')
    parser = StrOutputParser()

    chain = prompt | model | parser

    stream = chain.stream({
        'user-text': '离离原上草，一岁一枯荣！'
    })

    # 输出结果被直接解析成了字符串
    for resp_content in stream:
        print(resp_content, end='|')


## 试试【JsonOutputParser】
def run_with_JsonOutputParser():
    # 这里声明了返回格式
    class Book(BaseModel):
        title: str = Field(description='作品名称')
        description: str = Field(description='作品简介')

    parser = JsonOutputParser(pydantic_object=Book)

    # 指定要求返回的格式
    prompt = PromptTemplate(
        template='列举 3 部 {author} 的作品。\n{my_format_instructions}',
        input_variables=['author'],
        partial_variables={'my_format_instructions': parser.get_format_instructions()}
    )

    model = ChatOpenAI(model='gpt-4o-mini')

    chain = prompt | model | parser

    # 返回的 result 直接就是满足 Book 的格式的 JSON 字符串，如下
    # [
    #     {
    #         "title": "狂人日记",
    #         "description": "这是鲁迅的第一部小说，也是中国现代文学的重要作品，通过一个狂人的视角揭示了社会的黑暗和人性的扭曲。"
    #     },
    #     {
    #         "title": "阿Q正传",
    #         "description": "此作品通过对阿Q的生动描绘，讽刺了社会的虚伪和封建主义，深刻反映了当时中国社会的病态。"
    #     },
    #     {
    #         "title": "故乡",
    #         "description": "这篇小说表达了鲁迅对故乡的复杂情感，以及对乡土社会的批判，展现了农村的落后与残酷。"
    #     }
    # ]
    result = chain.invoke({'author': '鲁迅'})
    print(result)



## 假定环境变量 OPENAI_API_KEY 已经存在
if __name__ == '__main__':
    # run_init_chat_model()
    # run_chat_openai()
    # run_chat_openai_async()
    # run_with_prompt_template()
    # run_with_output_parser()
    run_with_JsonOutputParser()