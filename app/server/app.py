from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from server.routes.attraction import router as AttractionRouter

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(
    middleware=middleware,
    title="Touristy API",
    description="Touristy API was built to help you find the best attractions in your city. It is a simple API that returns a list of attractions based on your location. This was initially built as a REDi school project by AGWA Euphemia, but will further be enhanced to include more features.",
    version="1.0.0",
)




app.include_router(AttractionRouter, tags=["Attractions"], prefix="/attraction")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to ReDI touristy API! visit https://touristy.azurewebsites.net/docs#/ for documentation"}