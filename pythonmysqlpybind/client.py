import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # 发送消息给服务端
        message = "Hello, WebSocket Server!111"
        await websocket.send(message)
        print(f"Sent to server: {message}")

        # 接收服务端响应
        response = await websocket.recv()
        print(f"Received from server: {response}")

# 运行事件循环
asyncio.get_event_loop().run_until_complete(send_message())

