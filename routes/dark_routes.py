from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from config.database import cookie_banner_collection, collection_second_part
from models.CookieBannerModel import CookieBannersList, CookieBanner
from schemas.cookie_banners_schema import cookie_banners_serializer

api_router = APIRouter()


@api_router.post("/cookie_banner")
async def save_one_cookie_banner(cookie_banner: CookieBanner):
    cookie_banner_collection.insert_one(cookie_banner.dict())
    return JSONResponse(status_code=status.HTTP_200_OK, content={"msg": "banner correctly added"})


@api_router.get("/", response_description="List all banners")
async def get_cookie_banners():
    cookie_banners = cookie_banners_serializer(cookie_banner_collection.find())
    return cookie_banners


@api_router.delete("/delete_banners")
def delete_all_banners():
    cookie_banner_collection.delete_many({})
    return JSONResponse(status_code=status.HTTP_200_OK, content={"msg": "banners correctly deleted"})


@api_router.get("/get_banners_sorted")
def get_banner_sorted():
    cookie_banners = cookie_banners_serializer(cookie_banner_collection.find().sort("url", 1))
    return cookie_banners


@api_router.get("/get_banners_sorted_second")
def get_banner_sorted():
    cookie_banners = cookie_banners_serializer(collection_second_part.find().sort("url", 1))
    return cookie_banners

@api_router.post("/save_second_part")
def save_second_part_banners(cookie_banner: CookieBanner):
    collection_second_part.insert_one(cookie_banner.dict())
    return JSONResponse(status_code=status.HTTP_200_OK, content={"msg": "banners correctly added"})

