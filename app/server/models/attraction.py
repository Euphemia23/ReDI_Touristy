from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, Field

#Define the model for Image
class Image(BaseModel):
    url: HttpUrl
    source: str = Field(..., example="Wikimedia Commons")

#Define the model for Address
class Address(BaseModel):
    street: str = Field(..., example="123 Main St")
    city: str = Field(..., example="Anytown")
    state: str = Field(..., example="CA")
    zip: str = Field(..., example="12345")

#Define the model for Attraction
class AttractionSchema(BaseModel):
    name: str = Field(..., example="The Louvre")
    description: str = Field(..., example="The world's largest museum")
    rating: float = Field(..., gt=0, lt=6, example=4.5)
    official_site: HttpUrl = Field(..., example="https://www.louvre.fr/en")
    address: Address = Field(..., example={
        "street": "75058 Paris",
        "city": "Paris",
        "state": "France",
        "zip": "75058"
    })
    images: Optional[List[Image]] = Field(None, example=[
        {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Louvre_Pyramid_2012.jpg/1200px-Louvre_Pyramid_2012.jpg",
            "source": "Wikimedia Commons"
        },
        {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Louvre_Pyramid_2012.jpg/1200px-Louvre_Pyramid_2012.jpg",
            "source": "Wikimedia Commons"
        }
    ])
    classifications: str = Field(..., example="art")


    #class Configuration
    class Config:
        schema_extra = {
            "example": {
                "name": "The Louvre",
                "description": "The world's largest museum",
                "rating": 4.5,
                "official_site": "https://www.louvre.fr/en",
                "address": {
                    "street": "75058 Paris",
                    "city": "Paris",
                    "state": "France",
                    "zip": "75058"
                },
                "images": [
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Louvre_Pyramid_2012.jpg/1200px-Louvre_Pyramid_2012.jpg",
                        "source": "Wikimedia Commons"
                    },
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Louvre_Pyramid_2012.jpg/1200px-Louvre_Pyramid_2012.jpg",
                        "source": "Wikimedia Commons"
                    }
                ],
                "classifications":"art, history"
            }
        }
    

#Update the Attraction model
class UpdateAttractionModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    rating: Optional[float]
    official_site: Optional[HttpUrl]
    address: Optional[Address]
    images: Optional[List[Image]]
    classifications: Optional[str]

    #class Configuration
    class Config:
        schema_extra = {
            "example": {
                "name": "The Louvre",
                "description": "The world's largest museum",
                "rating": 4.5,
                "official_site": "https://www.louvre.fr/en",
                "address": {
                    "street": "75058 Paris",
                    "city": "Paris",
                    "state": "France",
                    "zip": "75058"
                },
                "images": [
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Louvre_Pyramid_2012.jpg/1200px-Louvre_Pyramid_2012.jpg",
                        "source": "Wikimedia Commons"
                    },
                    {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Louvre_Pyramid_2012.jpg/1200px-Louvre_Pyramid_2012.jpg",
                        "source": "Wikimedia Commons"
                    }
                ],
                "classifications": "art, history"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}