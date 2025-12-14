import json

from langchain.agents import create_agent
from langchain_core.output_parsers import JsonOutputParser
from pydantic import Field, BaseModel

from app.bailian.common import create_calc_tools, llm

class ContactInfo(BaseModel):
    args: str = Field(description="工具的入参")
    result: str = Field(description="计算结果")
    think: str = Field(description="思考过程")

# parser = JsonOutputParser(pydantic_object=ContactInfo)
# format_instructions = parser.get_format_instructions()

# 智能体的初始化 - 使用正确的参数格式
agent = create_agent(
    model=llm,
    tools=create_calc_tools(),
    system_prompt=f"""你是一个数学计算专家""",#，你必须按照以下格式返回结果：{format_instructions}
    response_format=ContactInfo
)

inputs = {"messages": [{"role": "user", "content": "2*200=？"}]}
# {"domain":"数学","context": "1+1199=？"}
resp = agent.invoke(inputs)
print(resp)
print(type(resp["structured_response"]),resp["structured_response"])
print(resp["structured_response"].result)