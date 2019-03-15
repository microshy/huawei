import data_io
import car_node
import road_node
import cross_node
import scheduler

def main():
    #导入数据
    car_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/car.txt')
    road_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/road.txt')
    cross_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/cross.txt')
    #1 初始化相关
    #1.1 完成了汽车、道路以及路口各自的链表连接
    #1.2 完成了每条道路各自拥有的线路连接
    #1.3 完成了路口与相通道路的连接
    print('start initializing...')
    car_run_list = car_node.car_list()
    car_wait_list = car_node.car_list()
    for item in car_data:
        car_wait_list.append_raw(item)
    road_list = road_node.road_list()
    for item in road_data:
        road_list.append_raw(item)
    cross_list = cross_node.cross_list()
    for item in cross_data:
        cross_list.append_raw(item)
    print('initialization complete!')
    #2 将路径规划内容导入汽车节点
    '''
    路径规划相关暂不考虑，假定现在car_node中的出发地和终点即为规划中的一步
    route_data = data_io.data_input_from_file('SDK/SDK/SDK/SDK_python/CodeCraft-2019/config/answer.txt')
    '''
    cross_list.link(road_list)
    car_wait_list.link(road_list)
    car_wait_list.dir()
    #3 开始调度
    print('start schedule...')
    set_time = 0

    while(car_run_list.head or car_wait_list.head):
        print('set_time =', set_time)
        #if set_time == 6:
        #    break
        scheduler.schedule_running_cars(car_run_list, road_list, cross_list, set_time)
        set_time += 1
        scheduler.schedule_waiting_cars(car_run_list, car_wait_list, road_list, cross_list, set_time)

    print('schedule complete!')


if __name__ == '__main__':
    main()