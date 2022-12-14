from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_attraction,
    delete_attraction,
    retrieve_attraction,
    retrieve_attractions,
    update_attraction,
    get_search_results,
)

from server.models.attraction import (
    ErrorResponseModel,
    ResponseModel,
    AttractionSchema,
    UpdateAttractionModel,
)

router = APIRouter()

@router.post("/", response_description="Attraction data added into the database")
async def add_attraction_data(attraction: AttractionSchema = Body(...)):
    attraction = jsonable_encoder(attraction)
    # new_attraction = await add_attraction(attraction)
    # return ResponseModel(new_attraction, "Attraction added successfully.")

@router.get("/getall", response_description="Attractions retrieved")
async def get_attractions():
    attractions = await retrieve_attractions()
    if attractions:
        return ResponseModel(attractions, "Attractions data retrieved successfully")
    return ResponseModel(attractions, "Empty list returned")

@router.get("/{id}", response_description="Attraction data retrieved")
async def get_attraction_data(id):
    attraction = await retrieve_attraction(id)
    if attraction:
        return ResponseModel(attraction, "Attraction data retrieved successfully")
    return ErrorResponseModel(
        "An error occurred.", 404, "Attraction doesn't exist."
    )

@router.put("/{id}")
async def update_attraction_data(id: str, req: UpdateAttractionModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    # updated_attraction = await update_attraction(id, req)
    # if updated_attraction:
    #     return ResponseModel(
    #         "Attraction with ID: {} name update is successful".format(id),
    #         "Attraction name updated successfully",
    #     )
    # return ErrorResponseModel(
    #     "An error occurred",
    #     404,
    #     "There was an error updating the attraction data.",
    # )

@router.delete("/{id}", response_description="Attraction data deleted from the database")
async def delete_attraction_data(id: str):
    deleted_attraction = "deleted attraction" #remove this line for real delete
    # deleted_attraction = await delete_attraction(id)
    # if deleted_attraction:
    #     return ResponseModel(
    #         "Attraction with ID: {} removed".format(id), "Attraction deleted successfully"
    #     )
    # return ErrorResponseModel(
    #     "An error occurred", 404, "Attraction with id {0} doesn't exist".format(id)
    # )

#search for attractions or location and GET all match
@router.get("/search/{query}", response_description="Attractions data retrieved")
async def search_attractions(query: str):
    attractions = await get_search_results(query)
    if attractions:
        return ResponseModel(attractions, "Attractions data retrieved successfully")
    return ResponseModel(attractions, "Empty list returned")