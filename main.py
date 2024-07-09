import asyncio
import tornado.web
import os
import logging

PORT = os.getenv("PYTHON_APP_PORT", 8888)
logging.getLogger().setLevel(logging.INFO)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("I was called: " + PORT)
        self.write("Hello, world: " + PORT)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(PORT)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
