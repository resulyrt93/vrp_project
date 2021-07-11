import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from exceptions import SolverException, ValidationException
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
    try:
        message_validator.validate()
    except ValidationException as e:
        raise HTTPException(status_code=400, detail=str(e))
    parser = message_validator.get_parser()

    route_solver = RouteSolver(parser)
    try:
        return route_solver.solve()
    except SolverException as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
