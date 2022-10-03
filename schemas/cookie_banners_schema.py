def cookie_banner_serializer(cookie_banner) -> dict:
    return {
        "id": str(cookie_banner["_id"]),
        "status": cookie_banner["status"],
        "buttons": buttons_serializer(cookie_banner["buttons"]),
        "url": cookie_banner["url"]

    }


def cookie_banners_serializer(cookie_banner_list) -> list:
    return [cookie_banner_serializer(cookie_banner) for cookie_banner in cookie_banner_list]


def buttons_serializer(btn):
    if btn["cookie_policy"]:
        cookie_policy_btn = button_feature_serializer(btn["cookie_policy"])
    else:
        cookie_policy_btn = None

    if btn["more_btn"]:
        more_btn = button_feature_serializer(btn["more_btn"])
    else:
        more_btn = None

    if btn["deny_btn"]:
        deny_btn = button_feature_serializer(btn["deny_btn"])
    else:
        deny_btn = None

    if btn["approve_btn"]:
        approve_btn = button_feature_serializer(btn["approve_btn"])
    else:
        approve_btn = None

    return {
        "more_btn": more_btn,
        "deny_btn": deny_btn,
        "approve_btn": approve_btn,
        "cookie_policy": cookie_policy_btn,

    }


def button_feature_serializer(btn_feature):
    return {
        "text": btn_feature["text"],
        "ambiguous_text": btn_feature["ambiguous_text"],
        "color": btn_feature["color"],
        "text_color": btn_feature["text_color"],
        "type": btn_feature["type"],
        "redirect": btn_feature["redirect"],
        "html": btn_feature["html"],
        "size": btn_feature["size"],
        "second_layer": btn_feature["second_layer"]
    }
