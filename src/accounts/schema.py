from drf_spectacular.extensions import OpenApiAuthenticationExtension


class KnoxTokenShema(OpenApiAuthenticationExtension):
    name = "KnoxAuthentication"
    target_class = "knox.auth.TokenAuthentication"

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey", 
            "name": "Authorization", 
            "in": "header",
            "description": f"Token-based authentication with required prefix 'Token'"
            }