import car_node
print_flag = 1
'''此处利用的是假设情况，即速度都一致，正常应该利用前进距离除以速度乘上所有速度的最小公倍数'''
speed = 5
speed_mul = 5
def schedule_running_cars(car_run_list, road_list, cross_list, set_time):

    #建立vruntime
    vruntime = 0
    #第一次优先级分割将未上路汽车与上路汽车分开,在路上的汽车优先处理，运行完之后再去安排车库中车辆
    in_gara_car_list = car_node.car_list()
    cur = car_run_list.head
    while cur != None:
        if cur.on_road:
            cur.nowhere = 0
            cur.time_out = 0
            #cur.vruntime = vruntime
            cur = cur.car_next
        else:
            car_run_list.remove(cur.id)
            temp = cur.car_next
            in_gara_car_list.append(cur)
            cur = temp
    #按照优先级进行排序
    '''sort here'''
    #调度车辆,假定经过排序后的队列是按最合适的优先级进行排列的
    while True:
        schedule_flag = 1  #检测是否所有车辆都调度完成
        cur = car_run_list.head
        #遍历list，移动所有能运动的车
        while cur != None:
            #若车的运行时间未耗尽
            if cur.time_out == 0:
                #重置nowhere标志位
                cur.nowhere = 0
                #若不是channel上为第一辆车
                if cur.prev_car_on_channel != None:
                    #计算到前车的距离
                    dis_prev_car = cur.prev_car_on_channel.position - cur.position
                    #若距离为1说明不可移动，置位nowhere
                    if dis_prev_car == 1:
                        cur.nowhere = 1
                    #若大于1
                    else:
                        #如果可移动距离小于最大移动距离,更新vruntime以及position，置位nowhere
                        if dis_prev_car < cur.speed_now:
                            cur.vruntime = cur.vruntime + (dis_prev_car - 1)/cur.speed_now*speed_mul
                            cur.position = cur.prev_car_on_channel.position - 1
                            cur.nowhere = 1
                        #若可移动距离大于最大移动距离，更新vruntime以及position，置位nowhere
                        else:
                            cur.vruntime = cur.vruntime + cur.speed_now/cur.speed_now*speed_mul
                            cur.position = cur.position +cur.speed_now
                            cur.time_out = 1
                #若是channel上为第一辆车
                else:
                    #若在目的道路上
                    if cur.is_on_dest_road():
                        #若可移动距离超过上限，认为入库
                        if cur.position + cur.speed_now > cur.to_ptr.length:
                            car_run_list.remove(cur.id)
                            temp = cur.next_car_on_channel
                            cur.channel_ptr.remove_car(cur)
                            cur = temp
                        #否则正常行驶
                        else:
                            dis_max = cur.position + cur.speed_now
                            cur.vruntime = cur.vruntime + cur.speed_now / cur.speed_now * speed_mul
                            cur.position = dis_max
                            cur.time_out = 1
                        if cur == None:
                            break
                    #若不在目的道路上
                    else:
                        dis_max = cur.position + cur.speed_now
                        #最大可移动距离是否超出道路
                        #若未超出，更新虚拟运行时间vruntime，当前位置position，时间耗尽标志位time_out
                        if dis_max <= cur.from_ptr.length:
                            cur.vruntime = cur.vruntime + cur.speed_now / cur.speed_now * speed_mul
                            cur.position = cur.position + cur.speed_now
                            cur.time_out = 1
                        #若已超出，记录切换road之前进过多少距离，所花费的vruntime
                        else:
                            dis_before_switch = cur.from_ptr.length - cur.position
                            vruntime_before_switch = dis_before_switch / cur.speed_now * speed_mul
                            #选择目标road上可进入的channel，根据channel中最后一辆车的postition判断是否还有位置
                            channel_switch = cur.to_ptr.channel_ptr
                            while channel_switch != None:
                                if channel_switch.position < 1:
                                    channel_switch = channel_switch.channel_next
                                else:
                                    break
                            #若没有可用的channel，更新vruntime和position，并将无处移动标志位nowhere置位
                            if channel_switch == None:
                                cur.vruntime = cur.vruntime + vruntime_before_switch
                                cur.position = cur.from_ptr.length
                                cur.nowhere = 1
                            #若有可用channel，计算在该channel上能移动的距离dis_after_switch
                            else:
                                #若不是第一辆车
                                if cur.prev_car_on_channel != None:
                                    dis_after_switch = channel_switch.speed - dis_before_switch
                                    #若dis_after_switch小于0，则说明不能通过路口，情况同没有channel可用一样
                                    if dis_after_switch <= 0:
                                        cur.vruntime = cur.vruntime + vruntime_before_switch
                                        cur.position = cur.from_ptr.length
                                        cur.nowhere = 1
                                    #若dis_after_switch大于0，则说明可以通过路口
                                    else:
                                        #将当前车从当前channel移动到切换的channel中
                                        cur.channel_ptr.remove_car(cur)
                                        channel_switch.append_car(cur)
                                        #初始化车的位置，channel以及speed信息
                                        cur.channel_ptr = channel_switch
                                        cur.position = 1
                                        cur.channel = channel_switch.id
                                        cur.speed_now = min(cur.speed_now, channel_switch.speed)
                                        #切换channel后到运行到前车后方行驶的vruntime
                                        vruntime_after_switch = (cur.prev_car_on_channel.position - 1) / cur.speed_now * speed_mul
                                        #若在新channel上的可行驶距离小于切换后可行驶的最大距离，更新vruntime，position以及置位标志位nowhere
                                        if cur.prev_car_on_channel.position - 1 < dis_after_switch:
                                            cur.vruntime = cur.vruntime + vruntime_before_switch + vruntime_after_switch
                                            print(cur.vruntime, vruntime_before_switch, vruntime_after_switch)
                                            cur.position = cur.prev_car_on_channel.position - 1
                                            cur.nowhere = 1
                                        #若可行驶距离大于最大距离，则更新相关信息
                                        else:
                                            cur.vruntime = cur.vruntime + vruntime_before_switch + dis_after_switch / cur.speed_now * speed_mul
                                            cur.position = dis_after_switch
                                            cur.time_out = 1
                                #若是第一辆车
                                else:
                                    channel_switch.speed = min(cur.speed, channel_switch.speed)
                                    cur.speed_now = channel_switch.speed
                                    dis_after_switch = channel_switch.speed - dis_before_switch
                                    # 若dis_after_switch小于0，则说明不能通过路口，情况同没有channel可用一样
                                    if dis_after_switch <= 0:
                                        cur.vruntime = cur.vruntime + vruntime_before_switch
                                        cur.position = cur.from_ptr.length
                                        cur.nowhere = 1
                                    # 若dis_after_switch大于0，则说明可以通过路口
                                    else:
                                        # 将当前车从当前channel移动到切换的channel中
                                        cur.channel_ptr.remove_car(cur)
                                        channel_switch.append_car(cur)
                                        # 初始化车的位置，channel以及speed信息
                                        cur.channel_ptr = channel_switch
                                        cur.position = 1
                                        cur.channel = channel_switch.id
                                        cur.speed_now = min(cur.speed_now, channel_switch.speed)
                                        #默认路长大于车速
                                        cur.vruntime = cur.vruntime + vruntime_before_switch + dis_after_switch / cur.speed_now * speed_mul
                                        cur.position = dis_after_switch
                                        cur.time_out = 1
                #若当前车辆是当前channel最后一辆车，则更新channel的position，speed信息
                if cur.next_car_on_channel == None:
                    cur.channel_ptr.position = cur.position
                    cur.channel_ptr.speed = min(cur.channel_ptr.speed, cur.speed_now)
                #当所有的车都时间耗尽或无法移动时，本次schedule结束
                schedule_flag = (schedule_flag and cur.nowhere)
            #若运行时间耗尽，直接下一辆车
            else:
                cur = cur.car_next
        #若schedule_flag为1，说明所有车都无法再继续移动（时间耗尽或者无处移动）
        if schedule_flag:
            break
        #将list重新根据优先级排序
        '''sort here'''

    #安排车辆出库
    cur = in_gara_car_list.head
    while cur != None:
        if cur.set_time <= set_time:
            #找到目标道路上和可进入车道
            channel_on = cur.from_ptr.channel_ptr
            while channel_on != None:
                if channel_on.position < 1:
                    channel_on = channel_on.channel_next
                else:
                    break
            if channel_on:
                cur.channel_ptr = channel_on
                cur.channel = channel_on.id
                channel_on.speed = min(cur.speed, channel_on.speed)
                cur.speed_now = min (cur.speed, channel_on.speed)
                cur.position = max(1, min(channel_on.position, channel_on.speed))
                cur.vruntime = vruntime + cur.position/cur.speed_now*speed_mul
                channel_on.position = cur.position - 1
                cur.on_road =1
                channel_on.append_car(cur)
                in_gara_car_list.remove(cur.id)
                temp = cur.car_next
                car_run_list.append(cur)
                cur = temp
            else:
                cur = cur.car_next
        else:
            cur = cur.car_next
    #打印测试用
    if print_flag:
        cur = car_run_list.head
        if cur == None:
            print('no car', ' ')
        while cur != None:
            print(cur.id, cur.position)#, cur.vruntime, cur.channel_ptr, cur.prev_car_on_channel, cur)
            cur = cur.car_next
        print('running...')
        cur = in_gara_car_list.head
        if cur == None:
            print('no car', ' ')
        while cur != None:
            print(cur.id)
            cur = cur.car_next
        print('in garage...')
    #将in_garage与list合并
    cur = car_run_list.head
    if cur != None:
        while cur.car_next != None:
            cur = cur.car_next
        cur.car_next = in_gara_car_list.head
        in_gara_car_list.head = None
    return None

def schedule_waiting_cars(car_run_list, car_wait_list, road_list, cross_list, set_time):
    cur = car_wait_list.head
    if cur == None:
        print('no car',' ')
    while cur:
        print(cur.id)
        if cur.set_time == set_time:
            temp = cur.car_next
            car_wait_list.remove(cur.id)
            car_run_list.append(cur)
            cur = temp
        else:
            cur = cur.car_next

    print('waiting...')
    return None

