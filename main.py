from fastapi import FastAPI
import chat_controller

app = FastAPI()

# include websocket controller
app.include_router(chat_controller.router)