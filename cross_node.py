class cross_node(object):
    def __init__(self, data):
        #origin info
        self.id = data[0]   #id of cross
        self.north = data[1] if data[1] >= 0 else 0 #id of road in the north
        self.east = data[2] if data[2] >= 0 else 0  #id of road in the east
        self.south = data[3] if data[3] >= 0 else 0 #id of road in the south
        self.west = data[4] if data[4] >= 0 else 0  #id of road in the west
        #info need
        #ptr need
        self.cross_next = None
        self.road_north = None
        self.road_east = None
        self.road_south = None
        self.road_west = None
    #连接路口与道路
    def link(self, road_list):
        self.road_north = road_list.search(self.north) if self.north != 0 else None
        self.road_east = road_list.search(self.east) if self.east != 0 else None
        self.road_south = road_list.search(self.south) if self.south != 0 else None
        self.road_west = road_list.search(self.west) if self.west != 0 else None

class cross_list(object):
    #初始化
    def __init__(self):
        self.head = None#car_list head pointer
    #判断是否为空
    def is_empty(self):
        return self.head == None
    #计算长度
    def length(self):
        count = 0
        cur = self.head
        while cur != None:
            count += 1
            cur = cur.cross_next
        return count
    #遍历链表
    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.id, '')
            cur = cur.cross_next
        print('')
    #添加原始数组进入队列，初始化时使用
    def append_raw(self, item):
        node = cross_node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.cross_next != None:
                cur = cur.cross_next
            cur.cross_next = node
    #添加节点至队尾
    def append(self, node):
        node.cross_next = None
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.cross_next != None:
                cur = cur.cross_next
            cur.cross_next = node
    #插入节点
    def insert(self, pos, node):
        if pos <= 0:
            cur = self.head
            self.head = node
            node.cross_next = cur
        elif pos > (self.length() - 1):
            self.append(node)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.cross_next
            node.cross_next = pre.cross_next
            pre.cross_next = node
    #移除节点
    def remove(self, id):
        cur = self.head
        pre = None
        while cur != None:
            if cur.id == id:
                if not pre:
                    self.head = cur.cross_next
                else:
                    pre.cross_next = cur.cross_next
                break
            else:
                pre = cur
                cur = cur.cross_next
    #搜索是否有节点，若有就返回该节点
    def search(self, id):
        cur = self.head
        while cur != None:
            if cur.id == id:
                return cur
            cur = cur.cross_next
        return False
    # 添加连接路径
    def link(self, road_list):
        cur = self.head
        while cur != None:
            cur.link(road_list)
            cur = cur.cross_next