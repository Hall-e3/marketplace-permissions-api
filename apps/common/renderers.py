import json
from rest_framework.renderers import JSONRenderer

class BaisoftJSONRenderer(JSONRenderer):
    charset = "utf-8"
    object_label = "object"

    def render(self, data, accepted_media_types=None, renderer_context=None):
        if data is None:
            return b""
            
        errors = data.get("errors", None)

        if errors is not None:
            return super(BaisoftJSONRenderer, self).render(data)

        return json.dumps({self.object_label: data})
