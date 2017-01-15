import wolframalpha

class Wolfram(object):

    app_id = "V9XL3G-LGEUTAX9YK"
    client = None

    def __init__(self):
        self.client = wolframalpha.Client(self.app_id)

    def query(self, query):
        res = self.client.query(query)
        if res.pods == 0:
            return None
        for pod in res.pods:
            print pod
            if "@primary" in pod.keys():
                for sub in pod.subpods:
                    return sub["plaintext"]
            if "@title" in pod.keys() and pod["@title"] == "Notable facts":
                for sub in pod.subpods:
                    return sub["plaintext"]
