class car_node(object):
    def __init__(self, data):
        #oringin info
        self.id = data[0]   #car id
        self.leave = data[1]    #departure
        self.arrive = data[2]   #destination
        self.speed = data[3]    #highest speed
        self.begin_time = data[4]   #time set to start moving
        #info need
        self.position = 0   #position to move to
        self.position_now = 0   #at the position on channel now
        self.channel = 0    #channel to switch to
        self.channel_now = 0    #on the channel on road now
        self.speed_now = 0  #speed to move now
        #pointer need
        self.update_next = None #pointer to the next car_node in car_run_list
        self.car_next = None    #pointer to the following car_node in the same cahnnel on road

class car_list(object):
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
            cur = cur.car_next
        return count
    #遍历链表
    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.id, '')
            cur = cur.car_next
        print('')
    #添加原始数组进入队列，初始化时使用
    def append_raw(self,item):
        node = car_node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.car_next != None:
                cur = cur.car_next
            cur.car_next = node
    #添加节点至队尾
    def append(self,node):
        node.car_next = None
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.car_next != None:
                cur = cur.car_next
            cur.car_next = node
    #插入节点
    def insert(self, pos, node):
        if pos <= 0:
            cur = self.head
            self.head = node
            node.car_next = cur
        elif pos > (self.length() - 1):
            self.append(node)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.car_next
            node.car_next = pre.car_next
            pre.car_next = node
    #移除节点
    def remove(self, id):
        cur = self.head
        pre = None
        while cur != None:
            if cur.id == id:
                if not pre:
                    self.head = cur.car_next
                else:
                    pre.car_next = cur.car_next
                break
            else:
                pre = cur
                cur = cur.car_next
    #搜索是否有节点，若有就返回该节点
    def search(self, id):
        cur = self.head
        while cur != None:
            if cur.id == id:
                return cur
            cur = cur.car_next
        return False