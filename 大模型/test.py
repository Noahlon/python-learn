import ollama
response = ollama.generate(
    model="qwen3:0.6b",  # 模型名称
    prompt="你是谁。",# 提示文本
     # 是否流式输出
)
# json 输出
print(response["response"])
