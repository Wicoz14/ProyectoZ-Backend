class Response():

    def __init__(self, success = None, msg = None, data = None):
        self.success = success
        self.msg = msg
        self.data = data
    
    def json(self):
        return {
            'success': self.success,
            'msg': self.msg,
            'data': self.data
        }