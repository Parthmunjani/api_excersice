import asyncio

from config import app

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run(debug=True, port=3000))