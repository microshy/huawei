import channel_node

class road_node(object):
    def __init__(self, data):
        #origin info
        self.id = data[0]   #id of the road
        self.length = data[1]   #length of the road
        self.speed = data[2]    #maximum speed on road
        self.channel = data[3]  #number of channels on road
        self.departure = data[4]    #departure cross
        self.destination = data[5]  #destination cross
        self.is_duplex = data[6]    #whether the road is duplex
        #info need
        #ptr need
        self.road_next = None   #pointer to the next road_node
        self.channel_ptr = None #pointer to the channel_node
        self.to_cross_ptr = None    #pointer to the destination cross_node
        self.from_cross_ptr = None  #pointer to the departure cross_node
    # 判断线路指针是否为空
    def is_channel_empty(self):
        return self.channel_ptr == None
    # 向道路节点添加线路节点
    def append_channel(self):
        if self.is_channel_empty():
            for i in range(self.channel):
                channelx = channel_node.channel_node(i+1, self.length)
                if self.channel_ptr == None:
                    self.channel_ptr = channelx
                else:
                    cur = self.channel_ptr
                    while cur.channel_next != None:
                        cur = cur.channel_next
                    cur.channel_next = channelx
    #遍历道路的channel
    def travel_channel(self):
        cur = self.channel_ptr
        while cur != None:
            print(cur.id, '')
            cur = cur.channel_next
        print('')
    # 搜索是否有线路节点，若有就返回该节点
    def search_channel(self, id):
        cur = self.channel_ptr
        while cur != None:
            if cur.id == id:
                return cur
            cur = cur.channel_next


class road_list(object):
    #初始化
    def __init__(self):
        self.head = None
    #判断是否为空
    def is_empty(self):
        return self.head == None
    #计算长度
    def length(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.road_next
        return count
    #遍历链表
    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.id, '')
            cur = cur.road_next
        print('')
    #添加原始数组进入队列，初始化时使用
    def append_raw(self,item):
        node = road_node(item)
        node.append_channel()
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.road_next != None:
                cur = cur.road_next
            cur.road_next = node
    #添加节点至队尾
    def append(self,node):
        node.append_channel()
        node.road_next = None
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.road_next != None:
                cur = cur.road_next
            cur.road_next = node
    #插入节点
    def insert(self, pos, node):
        node.append_channel()
        if pos <= 0:
            cur = self.head
            self.head = node
            node.road_next = cur
        elif pos > (self.length() - 1):
            self.append(node)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.road_next
            node.road_next = pre.road_next
            pre.road_next = node
    #移除节点
    def remove(self, id):
        cur = self.head
        pre = None
        while cur != None:
            if cur.id == id:
                if not pre:
                    self.head = cur.road_next
                else:
                    pre.road_next = cur.road_next
                break
            else:
                pre = cur
                cur = cur.road_next
    #搜索是否有节点，若有就返回该节点
    def search(self, id):
        cur = self.head
        while cur != None:
            if cur.id == id:
                return cur
            cur = cur.road_next

