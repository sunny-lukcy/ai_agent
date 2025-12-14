## 一、使用langchain调用通义千问模型
### 1.实例化大模型

### 2.初始化提示词模板
#### PromptTemplate
#### ChatPromptTemplate
#### FewShotPromptTemplate

### 3.链式调用大模型
chain = prompt | model


## 二、绑定自定义工具
### 1.开发工具函数
### 2.将工具函数转为Langchain Tool对象
  方法一：使用Tool.from_function()生成
  方法二：使用@ tool装饰器生成
  
### 3.将大模型和Tool对象绑定
  llm_with_tools = llm.bind_tools([add_tools])
  
### 4.调用大模型，尝试让大模型调用工具
  此时并不会调用工具函数， response返回结果中只有tool message（包含tool_calls）
  
### 5.调用工具函数
根据大模型返回的tools结果执行函数


## 三、智能体开发流程
    具备调用大模型能力（包含提示词模板）
    具备大模型调用工具能力
        创建智能体，用智能体调用Tool并返回结果

### 1.初始化工具

### 2.初始化大模型
### 3.创建智能体
### 4.调用智能体
