import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for i in range(5):
            response = f"{i + 1} Сообщение пользователя: {message}"
            await websocket.send(response)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
