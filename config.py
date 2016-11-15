import json


class Config():
    def get_config(self, fname):
        if fname is None:
            print("No file given")

        return json.loads(fname)
