from pydantic import BaseModel
from models.ButtonFeatures import Buttons


class CookieBanner(BaseModel):
    status: str
    buttons: Buttons | None = None
    url: str


class CookieBannersList(BaseModel):
    banners: list[CookieBanner] = []
