import httplib
class helperModel():
    @classmethod
    def _request(cls, method, host, path, headers={}, data= []):
        conn = httplib.HTTPSConnection(host, timeout = 100)
        conn.request(method, path, data, headers)
        response = conn.getresponse()
        return response.read()