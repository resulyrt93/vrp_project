from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from parser import MessageValidator
from route_solver import RouteSolver

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/solve")
async def solve(request: Request):
    data = await request.json()

    message_validator = MessageValidator(data)
    message_validator.validate()
    parser = message_validator.get_parser()

    route_solver = RouteSolver(parser)
    return route_solver.solve()


@app.get("/check")
def check():
    return {"status": "I am alive!"}
