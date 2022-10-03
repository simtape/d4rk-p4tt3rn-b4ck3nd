from pydantic import BaseModel


# describes all features of a button
class ButtonFeatures(BaseModel):
    text: str
    ambiguous_text: bool
    second_layer: bool
    color: str
    text_color: str
    type: str
    redirect: str | None = None
    html: str
    size: object


# standards buttons that should be in a banner
class Buttons(BaseModel):
    more_btn: ButtonFeatures | None = None
    deny_btn: ButtonFeatures | None = None
    approve_btn: ButtonFeatures | None = None
    cookie_policy: ButtonFeatures | None = None
