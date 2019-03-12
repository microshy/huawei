def scheduler(car_run_list, car_wait_list, road_list, cross_list):
    schedule_running_cars(car_run_list, road_list, cross_list)
    schedule_waiting_cars(car_run_list, car_wait_list, road_list, cross_list)
    return None

def schedule_running_cars(car_run_list, road_list, cross_list):
    if car_run_list.head:
        print(car_run_list.head.id)
        car_run_list.remove(car_run_list.head.id)
    else:
        print('no car')
    print('running...')
    return None

def schedule_waiting_cars(car_run_list, car_wait_list, road_list, cross_list):
    if car_wait_list.head:
        cur = car_wait_list.head
        car_wait_list.remove(car_wait_list.head.id)
        car_run_list.append(cur)
        print(car_run_list.head.id)
    else:
        print('no car')
    print('waiting...')
    return None