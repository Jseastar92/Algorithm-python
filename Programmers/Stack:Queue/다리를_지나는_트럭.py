def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리위, 도착, 거리 Queue
    on_bridge,arrival,distance = [],[],[]
    truck_count = len(truck_weights)
    i = 0
    while( len(arrival) != truck_count ):
        if on_bridge :
            if distance[0] == 0:
                arrival.append(on_bridge[0])
                del distance[0]
                del on_bridge[0] # collection deque의 popleft로 대체가능
    
        if sum(on_bridge) <= weight:
            if truck_weights :
                if sum(on_bridge) + truck_weights[0] <= weight :
                    on_bridge.append(truck_weights[0])
                    del truck_weights[0]
                    distance.append(bridge_length)
        
        for d_index, v in enumerate(distance):
            distance[d_index] -= 1
        i+=1

    answer = i
    return answer