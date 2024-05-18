import numpy as np
from matplotlib import pyplot as plt

# Packet object to store packet information
class Packet:
    def __init__(self, arrival_time, service_time, id):
        self.id = id
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.served_time = 0
        self.departure_time = None
    
    def serve(self, departure_time):
        self.served_time = self.service_time
        self.departure_time = departure_time

# Queue object to store packets
class Queue:
    def __init__(self, underlying_queue_object, enqueue_function, dequeue_function):
        self.__queue = underlying_queue_object()
        self.__enqueue_function = enqueue_function
        self.__dequeue_function = dequeue_function

    def enqueue(self, packet):
        self.__queue = self.__enqueue_function(self.__queue, packet)

    def dequeue(self):
        self.__queue, packet = self.__dequeue_function(self.__queue)
        return packet

    def __len__(self):
        return len(self.__queue)

    def get_queue(self):
        return self.__queue

# Processor Sharing Queue object to store packets
class PSQueue(Queue):
    def __init__(self):
        self.__queue = list()
        self.__enqueue_function = lambda lis, packet: lis + [packet]

    def enqueue(self, packet):
        self.__queue = self.__enqueue_function(self.__queue, packet)

    def dequeue(self, packet):
        self.__queue.remove(packet)
        return packet

    def __len__(self):
        return len(self.__queue)

    def get_queue(self):
        return self.__queue

# MM1 Queue Simulation class
class MM1QueueSimulation:

    def __init__(self, service_rate, queue_object = list, enqueue_function = lambda lis, packet: lis + [packet], dequeue_function = lambda lis: (lis[1:], lis[0])):
        self.service_rate = service_rate
        self.queue_object = queue_object
        self.enqueue_function = enqueue_function
        self.dequeue_function = dequeue_function        

    def simulate(self, arrival_rate, num_arrivals):

        current_time = 0
        packets_list = []
        
        for i in range(num_arrivals):            
            interarrival_time = np.random.exponential(1 / arrival_rate)
            current_time += interarrival_time               
            service_time = np.random.exponential(1 / self.service_rate)
            packets_list.append(Packet(current_time, service_time, i))

        packets_queue = Queue(self.queue_object, self.enqueue_function, self.dequeue_function)
        last_departure_time = 0
        packets_arrived_index = 0

        while packets_arrived_index < num_arrivals or len(packets_queue) > 0: 

            if len(packets_queue) == 0:
                packets_queue.enqueue(packets_list[packets_arrived_index])
                packets_arrived_index += 1
                continue

            current_packet = packets_queue.dequeue()
            service_time = current_packet.service_time

            if current_packet.arrival_time > last_departure_time:
                departure_time = current_packet.arrival_time + service_time
            else:
                departure_time = last_departure_time + service_time

            last_departure_time = departure_time

            current_packet.serve(departure_time)

            while packets_arrived_index < num_arrivals and packets_list[packets_arrived_index].arrival_time <= last_departure_time:
                packets_queue.enqueue(packets_list[packets_arrived_index])
                packets_arrived_index += 1

        return packets_list

# MM1 Processor Sharing Queue Simulation class
class MM1QueueSimulationProcessorSharing:

    def __init__(self, service_rate, queue_object = list):
        self.service_rate = service_rate
        self.queue_object = queue_object

    def simulate(self, arrival_rate, num_arrivals):

        current_time = 0
        packets_list = []
        
        for i in range(num_arrivals):            
            interarrival_time = np.random.exponential(1 / arrival_rate)
            current_time += interarrival_time
            service_time = np.random.exponential(1 / self.service_rate)
            packets_list.append(Packet(current_time, service_time, i))

        packets_queue = PSQueue()
        packets_arrived_index = 0
        current_time = 0

        while packets_arrived_index < num_arrivals or len(packets_queue) > 0:

            if len(packets_queue) == 0:
                packets_queue.enqueue(packets_list[packets_arrived_index])
                current_time = packets_list[packets_arrived_index].arrival_time
                packets_arrived_index += 1
                continue

            next_packet_arrival_time = (float('inf') if packets_arrived_index >= num_arrivals
                        else packets_list[packets_arrived_index].arrival_time)

            min_time_left = float('inf')
            for packet in packets_queue.get_queue():
                time_left = packet.service_time - packet.served_time
                min_time_left = min(min_time_left, time_left)

            service_time = min_time_left * len(packets_queue)

            if service_time < (next_packet_arrival_time - current_time):
                time_served = service_time
            else:
                time_served = next_packet_arrival_time - current_time

            for packet in packets_queue.get_queue():
                packet.served_time += time_served/len(packets_queue)
                if abs(packet.served_time - packet.service_time) <= 1e-6:
                    packet = packets_queue.dequeue(packet)
                    packet.departure_time = current_time + time_served

            current_time += time_served

            while packets_arrived_index < num_arrivals and (packets_list[packets_arrived_index].arrival_time - current_time) <= 1e-6:
                packets_queue.enqueue(packets_list[packets_arrived_index])
                packets_arrived_index += 1

        return packets_list