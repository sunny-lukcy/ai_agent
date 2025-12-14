from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate, PromptTemplate

llm = ChatOpenAI(
    model="qwen3-max",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-d6dba8cb664f419da9bb93dfe491bedd",
    streaming=True,
)

system_messages_prompt = ChatMessagePromptTemplate.from_template(
    template= "你是一个{domain}专家",
    role="system",
)
human_messages_prompt = ChatMessagePromptTemplate.from_template(
    template="请回答{context}",
    role="user",
)

# 创建提示词模板
# promptTemplate = ChatPromptTemplate.from_messages([
#     ("system", "你是一个{domain}专家"),
#     ("human", "请回答{context}")
# ])
promptTemplate = ChatPromptTemplate.from_messages([
    system_messages_prompt,
    human_messages_prompt
])
# prompt=promptTemplate.format_messages(domain="多模态", context="VLM是什么")
# print(prompt)

example_template="""
输入：{text}
翻译结果：{translation}
"""
examples = [{"text": "将你好翻译成英文", "translation": "hello"},
            {"text": "将世界翻译成英文", "translation": "world"}]
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_template),
    prefix="请将以下中文翻译成英文：",
    suffix="输入：{text}\n翻译结果：",
    input_variables=["text"],
)
# print(few_shot_prompt_template)
# prompt=few_shot_prompt_template.format(text="多么美好的一天啊！")
# print(prompt)

# 链式调用大模型
chain = few_shot_prompt_template | llm
resp = chain.invoke(input={"text": "多么美好的一天啊！"})

# 直接调用大模型
# prompt = few_shot_prompt_template.format(text="多么美好的一天啊！")
# resp = llm.invoke(prompt)
# resp = llm.invoke(prompt)
print(resp.content)

# resp = llm.stream(prompt)
# for chunk in resp:
#     print(chunk.content, end='', flush=True)
