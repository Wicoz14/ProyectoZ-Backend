class Token():
    def __init__(self, token = None):
        self.token = token

    def json(self):
        return {
            'token': self.token
        }