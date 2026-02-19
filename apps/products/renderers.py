from apps.common.renderers import BaisoftJSONRenderer

class ProductJSONRenderer(BaisoftJSONRenderer):
    object_label = "product"

class ProductListJSONRenderer(BaisoftJSONRenderer):
    object_label = "products"
