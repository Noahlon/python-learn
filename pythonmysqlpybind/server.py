import asyncio
import websockets

# 处理客户端连接的异步函数
async def handle_connection(websocket, path):
    try:
        # 接收客户端消息
        message = await websocket.recv()
        print(f"Received from client: {message}")

        # 发送响应消息给客户端
        response = f"Server received: {message}"
        await websocket.send(response)
        print(f"Sent to client: {response}")

    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally")
    except Exception as e:
        print(f"An error occurred: {e}")

# 启动 WebSocket 服务器
start_server = websockets.serve(handle_connection, "localhost", 8765)

# 运行事件循环
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
