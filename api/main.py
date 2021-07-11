import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from validator import MessageValidator
from route_solver import RouteSolver

app = FastAPI()

origins = [
    "*",
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


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
