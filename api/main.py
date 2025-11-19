import sys
from dotenv import load_dotenv
from commands import *
from commands.handler import CommandHandler
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mainRoute():
    return { "message": "Hello, World!" }

@app.get("/numbers/{number}")
def testRoute(number: int):
    return { "message": f"Your number was {number}"}

if __name__ == "__main__":
    load_dotenv()
    cmd_handler = CommandHandler("studyai", [
        ListCommand(),
        ProcessCommand(),
        RemoveCommand(),
        RenameCommand(),
        SearchCommand()
    ])

    cmd_handler.handle(sys.argv[1:])
