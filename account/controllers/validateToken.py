import json

from google.auth.transport import requests
from google.oauth2 import id_token
from config import CLIENT_ID
from models.helperModel import helperModel


class validateToken:
    @classmethod
    def validate_token(cls, token, flag):
        # facebook token
        if flag == 0:
            info = json.loads(helperModel._request("GET", "graph.facebook.com", "/me?access_token=" + token))
            if "id" in info:
                # print info
                userid = info['id']
            else:
                return None
        # google token
        elif flag == 1:
            try:
                # Specify the CLIENT_ID of the app that accesses the backend:
                idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

                # Or, if multiple clients access the backend server:
                # idinfo = id_token.verify_oauth2_token(token, requests.Request())
                # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
                #     raise ValueError('Could not verify audience.')

                if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                    raise ValueError('Wrong issuer.')

                # If auth request is from a G Suite domain:
                # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
                #     raise ValueError('Wrong hosted domain.')

                # ID token is valid. Get the user's Google Account ID from the decoded token.
                userid = idinfo['sub']
            except ValueError:
                # Invalid token
                return None
        else:
            return None
        return userid
