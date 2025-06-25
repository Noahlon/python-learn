import ollama

ollama.api_url = "http://127.0.0.1:11434"
def chat_with_ollama(msg):
    # 构建消息体，使用用户输入
    msg = msg
    # 正确调用 ollama.chat 方法
    response = ollama.chat(model="qwen3:0.6b", messages=messages)
    # 获取模型回复
    reply = response["message"]["content"]
    return reply

if __name__ == "__main__":
    # 设置初始消息
    messages = [{"role": "system", "content": "你是一个有用的助手"}]
    
    while True:
        user_input = input("请输入您的问题（输入'退出'结束对话）：")
        if user_input.lower() == '退出':
            print("对话结束。")
            break
        
        # 将用户输入添加到消息列表
        messages.append({"role": "user", "content": user_input})
        
        # 调用函数获取模型回复
        reply = chat_with_ollama(user_input)
        
        # 打印模型回复
        print(f"模型回复：{reply}")
        
        # 将模型回复添加到消息列表
        messages.append({"role": "assistant", "content": reply})