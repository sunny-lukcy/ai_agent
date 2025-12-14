from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

llm = ChatOpenAI(
    model="qwen3-max",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-d6dba8cb664f419da9bb93dfe491bedd",
    streaming=True,
)

system_messages_prompt = ChatMessagePromptTemplate.from_template(
    template="你是一个{domain}专家",
    role="system",
)
human_messages_prompt = ChatMessagePromptTemplate.from_template(
    template="请回答{context}",
    role="user",
)

# 创建提示词模板
chat_prompt_template = ChatPromptTemplate.from_messages([
    system_messages_prompt,
    human_messages_prompt
])


# 初始化工具函数
class AddInputArgs(BaseModel):
    a: int = Field(description="the first number")
    b: int = Field(description="the second number")

@tool(
    description="add two numbers",
    args_schema=AddInputArgs,
    return_direct=False
)
def add(a, b):
    return a + b


def create_calc_tools():
    return [add]


calc_tools = create_calc_tools()
