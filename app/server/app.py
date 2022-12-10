from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.routes.attraction import router as AttractionRouter


app = FastAPI(
    title="Touristy API",
    description="Touristy API was built to help you find the best attractions in your city. It is a simple API that returns a list of attractions based on your location. This was initially built as a REDi school project by AGWA Euphemia, but will further be enhanced to include more features.",
    version="1.0.0",
)

# allow all origins to access the API (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#todo: Remove CORS middleware in production

app.include_router(AttractionRouter, tags=["Attractions"], prefix="/attraction")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to touristy API!"}