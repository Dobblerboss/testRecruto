from fastapi import FastAPI, Response
app = FastAPI()


@app.get("/")
async def read_user_item(name: str, message: str):
    data = f'Hello {name}!\n{message}!'
    return Response(content=data, media_type="text/plain")
