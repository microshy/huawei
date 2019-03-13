class channel_node(object):
    def __init__(self, id, max_entries):
        #info need
        self.id = id if id > 0 else 0   #record the channel id
        self.speed = 999  #record the minimum speed in channel
        self.max_entries = max_entries if max_entries > 0 else 0    #record the maximum number of cars that can move in channel
        self.entries = 0    #number of cars present in channel
        self.position = 999   #position of the last car in channel
        #ptr need
        self.channel_next = None    #pointer to the next channel
        self.car_ptr = None
    # 判断线路指针是否为空
    def is_car_empty(self):
        return self.car_ptr == None
    # 向channel节点添加car节点
    def append_car(self, car_node):
        car_node.next_car_on_channel = None
        if self.is_car_empty():
            self.car_ptr = car_node
            car_node.prev_car_on_channel = None
        else:
            cur = self.car_ptr
            while cur.next_car_on_channel != None:
                cur = cur.next_car_on_channel
            car_node.prev_car_on_channel = cur
            cur.next_car_on_channel = car_node
    # 遍历channel的car
    def travel_car(self):
        cur = self.car_ptr
        while cur != None:
            print(cur.id, '')
            cur = cur.next_car_on_channel
        print('')
    # 搜索是否有car节点，若有就返回该节点
    def search_car(self, id):
        cur = self.car_ptr
        while cur != None:
            if cur.id == id:
                return cur
            cur = cur.next_car_on_channel
    # 移除car节点
    def remove_car(self, car_node):
        cur = self.car_ptr
        while cur:
            if cur != car_node:
                cur = cur.next_car_on_channel
            else:
                pre = cur.prev_car_on_channel
                if pre == None:
                    self.car_ptr = cur.next_car_on_channel
                    cur.next_car_on_channel.prev_car_on_channel = None
                else:
                    pre.next_car_on_channel = cur.next_car_on_channel
                    cur.next_car_on_channel.prev_car_on_channel = pre
                cur.next_car_on_channel = None
                cur.prev_car_on_channel = None
                break

