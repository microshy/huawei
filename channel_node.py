class channel_node(object):
    def __init__(self, id, max_entries):
        #info need
        self.id = id if id > 0 else 0   #record the channel id
        self.speed = 0  #record the minimum speed in channel
        self.max_entries = max_entries if max_entries > 0 else 0    #record the maximum number of cars that can move in channel
        self.entries = 0    #number of cars present in channel
        self.position = 0   #position of the last car in channel
        #ptr need
        self.channel_next = None    #pointer to the next channel

