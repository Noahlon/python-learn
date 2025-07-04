import time
import pymysql
import random
import asyncio
import websockets
import handsome

DB_NAME = 'test'

def get_tick():
    """
    模拟获取交易行情数据，固定 symbol 为 xaausd，price 为 xxxx.xx 格式，volume 为 0.01 手。

    :return: 包含行情数据的字典
    """
    data = handsome.get_tick()
    return {
        "volume": data[0],
        "symbol": data[2],
        "price": data[1]
    }

def create_database():
    try:
        # 先不指定数据库，连接到 MySQL 服务
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                               user='root', password='admin123',
                               charset='utf8mb4')
        with conn.cursor() as cursor:
            # 创建数据库
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"数据库 {DB_NAME} 创建成功！")
            # 创建表
            cursor.execute(f"USE {DB_NAME}")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tick_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    symbol VARCHAR(255),
                    price DECIMAL(10, 2),
                    volume DECIMAL(10, 2),
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("表 tick_data 创建成功！")
        return conn
    except pymysql.MySQLError as err:
        print(f"创建数据库或表失败: {err}")
        return None
    finally:
        if conn:
            conn.close()

async def send_message(content):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # 发送消息给服务端
        message = f"Hello, WebSocket Server! {content}"
        await websocket.send(message)
        print(f"Sent to server: {message}")

        # 接收服务端响应
        response = await websocket.recv()
        print(f"Received from server: {response}")
        
def insert_tick_data(data):
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306,
                               user='root', password='admin123',
                               database=DB_NAME, charset='utf8mb4')
        with conn.cursor() as cursor:
            sql = "INSERT INTO tick_data (symbol, price, volume) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data["symbol"], data["price"], data["volume"]))
            conn.commit()
        return True
    except pymysql.MySQLError as err:
        print(f"插入数据失败: {err}")
        return False
    finally:
        if conn:
            conn.close()

def send_tick_data():
    while True:
        tick_data = get_tick()
        # 间隔时间
        time.sleep(1)
        
        #将行情通过 WebSocket 发送给服务端
        print(f"Sending tick data: {tick_data}")
        asyncio.get_event_loop().run_until_complete(send_message(tick_data))
        
        # 将行情数据插入到 MySQL 数据库
        if insert_tick_data(tick_data):
            print("Tick data inserted successfully.")
        else:
            print("Failed to insert tick data.")


if __name__ == "__main__":
    send_tick_data()
    # temp = handsome.get_tick()
    # print(f"Received from C++: {temp}")