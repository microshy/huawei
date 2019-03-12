import car_node
print_flag = 1
'''此处利用的是假设情况，即速度都一致，正常应该利用前进距离除以速度乘上所有速度的最小公倍数'''
speed = 5
speed_mul = 5
def schedule_running_cars(car_run_list, road_list, cross_list, set_time):
    #打印测试用
    if print_flag:
        cur = car_run_list.head
        if cur == None:
            print('no car', ' ')
        while cur != None:
            print(cur.id)
            cur = cur.car_next
    #建立vruntime
    vruntime = 0
    #第一次优先级分割将未上路汽车与上路汽车分开,在路上的汽车优先处理，运行完之后再去安排车库中车辆
    in_gara_car_list = car_node.car_list()
    cur = car_run_list.head
    while cur != None:
        if cur.on_road:
            cur.vruntime = vruntime
            cur = cur.car_next
        else:
            car_run_list.remove(cur.id)
            temp = cur.car_next
            in_gara_car_list.append(cur)
            cur = temp
    #按照优先级进行排序

    #调度车辆,假定经过排序后的队列是按最合适的优先级进行排列的
    schedule_flag = 0  #检测是否所有车辆都调度完成
    while not schedule_flag:
        cur = car_run_list.head
        while cur != None:
            if cur.channel_ptr.car_ptr != cur:
                dis_prev_car = cur.prev_car_on_channel.position - cur.position
                if dis_prev_car == 1:
                    cur.nowhere = 1
                else:
                    if dis_prev_car < cur.speed_now:
                        cur.vruntime = cur.vruntime + (cur.prev_car_on_channel.position - 1 - cur.position)/speed*speed_mul
                        cur.position = cur.prev_car_on_channel.position - 1
                        cur.nowhere = 1
                    else:
                        cur.vruntime = cur.vruntime + cur.speed_now/speed*speed_mul
                        cur.position = cur.position +cur.speed_now
                        cur.timeout = 1
            else:
                dis_max = cur.position + cur.speed_now
                if dis_max <= cur.from_ptr.length:
                    cur.vruntime = cur.vruntime + cur.speed_now / speed * speed_mul
                    cur.position = cur.position + cur.speed_now
                    cur.timeout = 1
                else:
                    dis_before_switch = cur.from_ptr.length - cur.position
                    vruntime_before_switch = dis_before_switch / speed * speed_mul
                    channel_switch = cur.to_ptr.channel_ptr
                    while channel_switch != None:
                        if channel_switch.position <= 1:
                            channel_switch = channel_switch.next_channel
                        else:
                            break
                    if channel_switch == None:
                        cur.vruntime = cur.vruntime + vruntime_before_switch
                        cur.position = cur.from_ptr.length
                        cur.nowhere = 1
                    else:
                        dis_after_switch = channel_switch.speed - dis_before_switch
                        if dis_after_switch <= 0:
                            cur.vruntime = cur.vruntime + vruntime_before_switch
                            cur.position = cur.from_ptr.length
                            cur.nowhere = 1
                        else:
                            cur.channel_ptr.remove(cur)
                            channel_switch.append_car(cur)
                            cur.position = 1
                            cur.channel = channel_switch.id
                            cur.speed_now = min(cur.speed_now, channel_switch.speed)
                            vruntime_after_swtch = (cur.prev_car_on_channel.position - 1 - cur.position) / speed * speed_mul
                            if cur.prev_car_on_channel.position - cur.position < dis_after_switch:
                                cur.vruntime = cur.vruntime + vruntime_before_switch + vruntime_after_swtch
                                cur.position = cur.prev_car_on_channel.position - 1
                                cur.nowhere = 1
                            else:
                                cur.vruntime = cur.vruntime + dis_after_switch / speed * speed_mul
                                cur.position = cur.position + dis_after_switch
                                cur.timeout = 1
            if cur.next_car_on_channel == None:
                cur.channel_ptr.position = cur.position
                cur.channel_ptr.speed = min(cur.channel_ptr.speed, cur.speed_now)
            schedule_flag = (schedule_flag and cur.nowhere) or (schedule_flag and cur.timeout)
            cur = cur.car_next

    #安排车辆出库

    print('running...')
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

