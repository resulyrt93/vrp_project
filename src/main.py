from fastapi import FastAPI, Request

from parser import MessageValidator
from route_solver import RouteSolver

app = FastAPI()


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