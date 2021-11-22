import websockets
import asyncio

connected = set()

async def sendMsg(websocket, path):
    connected.add(websocket)

    try:
        async for message in websocket:
            for con in connected:
                if con != websocket:
                    await con.send(message)
    except websockets.exceptions.ConnectionClosed as e:
        print('Client disconnected')

    finally:
        connected.remove(websocket)
        
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(sendMsg, "10.83.10.98", 3639):
        await asyncio.Future()

asyncio.run(main())