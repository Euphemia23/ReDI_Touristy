from bson.objectid import ObjectId

from decouple import config

import motor.motor_asyncio

import certifi


MONOGO_DETAILS = config("MONGO_DETAILS")

#client = motor.motor_asyncio.AsyncIOMotorClient(MONOGO_DETAILS)

client = motor.motor_asyncio.AsyncIOMotorClient(MONOGO_DETAILS, tlsCAFile=certifi.where())

database = client.attractions

attraction_collection = database.get_collection("attractions_collection")

#helpers

def attraction_helper(attraction) -> dict:
    return {
        "id": str(attraction["_id"]),
        "name": attraction["name"],
        "description": attraction["description"],
        "rating": attraction["rating"],
        "official_site": attraction["official_site"],
        "address": attraction["address"],
        "images": attraction["images"],
        "classifications": attraction["classifications"],
    }

#Retrieve attractions present in the database
async def retrieve_attractions():
    attractions = []
    async for attraction in attraction_collection.find():
        attractions.append(attraction_helper(attraction))
    return attractions

#Add a new attraction into to the database
async def add_attraction(attraction_data: dict) -> dict:
    attraction = await attraction_collection.insert_one(attraction_data)
    new_attraction = await attraction_collection.find_one({"_id": attraction.inserted_id})
    return attraction_helper(new_attraction)

#Retrieve a attraction with a matching ID
async def retrieve_attraction(id: str) -> dict:
    attraction = await attraction_collection.find_one({"_id": ObjectId(id)})
    if attraction:
        return attraction_helper(attraction)

#Update a attraction with a matching ID
async def update_attraction(id: str, data: dict):
    #Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    attraction = await attraction_collection.find_one({"_id": ObjectId(id)})
    if attraction:
        updated_attraction = await attraction_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_attraction:
            return True
        return False

#Delete a attraction from the database
async def delete_attraction(id: str):
    attraction = await attraction_collection.find_one({"_id": ObjectId(id)})
    if attraction:
        await attraction_collection.delete_one({"_id": ObjectId(id)})
        return True


#search for attractions or location and GET all match
async def get_search_results(query: str):
    attractions = []
    async for attraction in attraction_collection.find({
        "$or": [
            {"name": {"$regex": query, "$options": "i"}},
            {"description": {"$regex": query, "$options": "i"}},
            {"address.street": {"$regex": query, "$options": "i"}},
            {"address.city": {"$regex": query, "$options": "i"}},
            {"address.state": {"$regex": query, "$options": "i"}},
        ]
    }):
        attractions.append(attraction_helper(attraction))
    return attractions