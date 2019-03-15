class car_node(object):
    def __init__(self, data):
        #oringin info
        self.id = data[0]   #car id
        self.leave = data[1]    #departure
        self.arrive = data[2]   #destination
        self.speed = data[3]    #highest speed
        self.set_time = data[4]   #time set to start moving
        #info need
        self.position = 0   #at the position on channel now
        self.channel = 0    #on the channel on road now
        self.speed_now = 0  #speed to move now
        self.on_road = 0  #1 means on road while 0 refers to in garage
        self.vruntime = 0  #vitural running time
        self.arrive_time = 0
        self.dir = 0  # straight 0 turn left 1 turn right 2
        self.time_out = 0
        self.nowhere = 0
        self.dis_max = 0
        self.dis_before_switch = 0
        self.dis_after_switch = 0
        self.vruntime_before_switch = 0
        # #pointer need
        self.from_ptr = None
        self.to_ptr = None
        self.car_next = None    #pointer to the next car_node in car_run_list
        self.channel_ptr = None
        self.next_car_on_channel = None
        self.prev_car_on_channel = None

    def link(self, road_list):
        self.from_ptr = road_list.search(self.leave)
        self.to_ptr = road_list.search(self.arrive)
    def is_on_dest_road(self):
        cur_channel = self.to_ptr.channel_ptr
        while cur_channel:
            if cur_channel == self.channel_ptr:
                return 1
            else:
                return 0
    def is_turn(self):
        cur = self.from_ptr.to_cross_ptr
        #1=north,2=east,3=south,4=west
        road_from_dir = 0
        road_to_dir = 0
        if cur != None:
            if cur.road_north == self.from_ptr:
                road_from_dir = 1
            elif cur.road_north == self.to_ptr:
                road_to_dir = 1
            if cur.road_east == self.from_ptr:
                road_from_dir = 2
            elif cur.road_east == self.to_ptr:
                road_to_dir = 2
            if cur.road_south == self.from_ptr:
                road_from_dir = 3
            elif cur.road_south == self.to_ptr:
                road_to_dir = 3
            if cur.road_west == self.from_ptr:
                road_from_dir = 4
            elif cur.road_west == self.to_ptr:
                road_to_dir = 4
        dif = road_to_dir - road_from_dir
        if dif == 2 or dif == -2:
            self.dir = 0
        elif dif == 1 or dif == -3:
            self.dir = 1
        elif dif == -1 or dif == 3:
            self.dir = 2


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
    #添加连接路径
    def link(self, road_list):
        cur = self.head
        while cur != None:
            cur.link(road_list)
            cur = cur.car_next
    # 添加下个路口方向
    def dir(self):
        cur = self.head
        while cur != None:
            cur.is_turn()
            cur = cur.car_next