from apps.common.renderers import BaisoftJSONRenderer

class UserJSONRenderer(BaisoftJSONRenderer):
    object_label = "user"

class UserListJSONRenderer(BaisoftJSONRenderer):
    object_label = "users"
