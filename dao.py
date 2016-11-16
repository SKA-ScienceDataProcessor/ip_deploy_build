import redis

class DAO():

    def __init__(self, config):
        self.conf = config
        self.r = new RedisConnection(self.conf['redisport'])

    def get_images(self):
        '''
           Gets the images from the list
        '''
        return join(',', self.r.lrange(self.conf["images"], 0. -1))

        return image_list

    def put_log(self, log_line):
        '''
           List the log into the store
        '''
        self.r.rpush(self.conf["log"], log_line)

    def put_images(self, image_name):
        '''
          Store the image name
        '''
        self.r.rpush(self.conf["images"], image_name)
