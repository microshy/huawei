
a=1
b=a
a=a+1
print(b)
print(a)
''' io功能测试
data_list = [[1001, 1, 501, 502, 503, 516, 506, 505, 518, 508, 509, 524],
             [1002, 1, 513, 504, 518, 508, 509, 524],
             [1003, 1, 513, 517, 507, 508, 509, 524],
             [1004, 1, 501, 502, 515, 519, 509, 524],
             [1005, 1, 501, 514, 504, 517, 507, 508, 509, 524],
             [1006, 1, 513, 517, 521, 510, 511, 512],
             [1007, 1, 513, 504, 518, 507, 521, 510, 511, 512],
             [1008, 1, 501, 502, 503, 516, 506, 519, 508, None, 522, 511, 512]]
data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/road.txt')
data_output_to_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/answer.txt', data_list)
'''

'''链表功能测试
car = car_node.car_node([1,2,3,4,5])
car_run_list.append(car)
car = car_node.car_node([123456, 2, 3, 4, 5])
car_run_list.insert(99,car)
car_run_list.remove(10001)
print(car_run_list.search(10023))
print(car_run_list.search(12222))
car_run_list.travel()

road = road_node.road_node([1, 2, 3, 4, 5, 6, 7])
road_list.append(road)
road = road_node.road_node([1233, 2, 3, 4, 5, 6, 7])
road_list.insert(53,road)
road_list.remove(5059)
print(road_list.search(5050))
print(road_list.search(5099))
road_list.travel()
print((road_list.search(5058)).search_channel(2))
print(((road_list.search(5050)).search_channel(1)).max_entries)
(road_list.search(5058)).travel_channel()

cross = cross_node.cross_node([1, 2, 3, 4, 5], road_list)
cross_list.append(cross)
cross = cross_node.cross_node([123456, 2, 3, 4, 5], road_list)
cross_list.insert(10, cross)
cross_list.remove(25)
print(cross_list.search(10023))
print(cross_list.search(12))
cross_list.travel()

print((cross_list.search(12)).south)
print(cross_list.search(12).road_south)
print(road_list.search(5015))
'''

'''链表append修正，解决了remove的节点再次append时存在的next指针指向原处的小bug
print(car_wait_list.head)
print(car_wait_list.head.car_next)
print(car_wait_list.head.car_next.car_next)
cur = car_wait_list.head
car_wait_list.remove(car_wait_list.head.id)
car_run_list.append(cur)
print(car_run_list.head)
print(car_run_list.head.car_next)
print(car_wait_list.head)
print(car_wait_list.head.car_next)
'''
'''测试schedule的退出是否正常
if car_run_list.head:
    print(car_run_list.head.id)
    car_run_list.remove(car_run_list.head.id)
else:
    print('no car')
    
if car_wait_list.head:
    cur = car_wait_list.head
    car_wait_list.remove(car_wait_list.head.id)
    car_run_list.append(cur)
    print(car_run_list.head.id)
else:
    print('no car')
'''
'''
#若车已经到位，移除出run_list
cur_channel = cur.to_ptr.channel_ptr
while cur_channel:
    if cur_channel == cur.channel_ptr:
        if cur.position == cur.to_ptr.length:
            #时间耗尽的默认不进车库，不然进车库
            if not cur.time_out:
                break
            else:
                car_run_list.remove(cur.id)
                temp = cur.next_car_on_channel
                cur.channel_ptr.remove_car(cur)
                cur = temp
        break
    else:
        cur_channel = cur_channel.channel_next
if cur == None:
    break
'''
'''其他
cur.channel_ptr.position = min(cur.channel_ptr.position, cur.position)

def auto_name():
    basic = road_data[0][0]
    print(basic)
    for i in range(basic,basic+len(road_data)):
        name = 'road'+str(i)
        print(name)
        print(road_data[i-basic])
        locals()['road'+str(i)] = road_node.road_node(road_data[i-basic])
    print(road5005)
'''