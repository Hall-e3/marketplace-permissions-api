from rest_framework.exceptions import APIException

class BusinessNotFound(APIException):
    status_code = 404
    default_detail = "The requested business does not exist"

class NotYourBusiness(APIException):
    status_code = 403
    default_detail = "You do not have permission to access this business's data"

class ProductNotFound(APIException):
    status_code = 404
    default_detail = "The requested product does not exist"
