import json


class Config():
    def get_config(self, fname):
        if fname is None:
            print("No file given")

        data = None

        with open(fname, 'rb') as f:
            data = f.read()
        f.closed
        return json.loads(data)
