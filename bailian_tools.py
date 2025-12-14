from pydantic import BaseModel, Field

from app.bailian.common import chat_prompt_template, llm
from langchain_core.tools import tool

class AddInputArgs(BaseModel):
    a: int = Field(description="the first number")
    b: int = Field(description="the second number")
# 1.工具函数
@tool(
    description="add two numbers",
    args_schema=AddInputArgs,
)
def add(a,b):
    """add two numbers"""
    return a+b

# 将工具函数转为langchain Tool对象
# add_tools = Tool.from_function(
#     func=add,
#     name="add",
#     description="add two numbers"
# )

tool_dict = {
    "add": add
}
# 3.将大模型和Tool对象绑定
llm_with_tools = llm.bind_tools([add])

# 4.链式调用大模型
chain = chat_prompt_template | llm_with_tools

resp = chain.invoke(input={"domain":"数学","context": "1+1199=？"})
print(resp)

# 5.调用工具函数
for tool_calls in resp.tool_calls:
    print(tool_calls)
    args = tool_calls["args"]
    print(args)
    func_name = tool_calls["name"]
    print(func_name)

    tools_func = tool_dict[func_name]
    # tool_content = tools_func(int(args['__arg1']), int(args['example_parameter_2']))
    tool_content = tools_func.invoke(args)
    print(tool_content)
