class AbstractAuth:
    def get_auth_method(self):
        raise NotImplementedError("AbstractAuth is a abstract class")

    def get_params(self):
        raise NotImplementedError("AbstractAuth is a abstract class")
