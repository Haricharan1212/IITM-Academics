from QueueSimulator import *

FIFOEnqueue = lambda lis, packet: lis + [packet] # packet added to end
FIFODequeue = lambda lis: (lis[1:], lis[0]) # packet removed from start
LIFOEnqueue = lambda lis, packet: lis + [packet] # packet added to end
LIFODequeue = lambda lis: (lis[:-1], lis[-1]) # packet removed from end

def get_avg_num_packets_in_system(packets_list):
    queue_length = 0
    queue_length_values = dict()

    arrival_times = np.array([packet.arrival_time for packet in packets_list])
    departure_times = np.array([packet.departure_time for packet in packets_list])

    i = 0
    j = 0

    current_time = 0
    n = len(arrival_times)

    while i < n and j < n:
        if arrival_times[i] < departure_times[j]:
            if queue_length not in queue_length_values:
                queue_length_values[queue_length] = 0
            queue_length_values[queue_length] += arrival_times[i] - current_time
            current_time = arrival_times[i]
            queue_length += 1
            i += 1
        else:
            if queue_length not in queue_length_values:
                queue_length_values[queue_length] = 0
            queue_length_values[queue_length] += departure_times[j] - current_time
            current_time = departure_times[j]
            queue_length -= 1
            j += 1

    avg_queue_length = 0
    total_time = departure_times[-1]

    for key, value in queue_length_values.items():
        avg_queue_length += key * value / total_time

    return avg_queue_length

service_rate = 10
num_arrivals = 500000
num_points = 20

# Theoretical calculations

def average_waiting_time(lambda_value, ser1vice_rate):
    rho = lambda_value / service_rate
    return ((rho/service_rate)/(1 - rho))

def average_sojourn_time(lambda_value, service_rate):
    ans = (1 / (service_rate - lambda_value))
    assert np.all(ans - (average_waiting_time(lambda_value, service_rate) + lambda_value/service_rate) < 1e-6)
    return ans

# Plotting code
for discipline, enqueue_function, dequeue_function in [("FIFO", FIFOEnqueue, FIFODequeue), ("LIFO", LIFOEnqueue, LIFODequeue), ("PS", None, None)]:

    simulator = MM1QueueSimulation(service_rate, list, enqueue_function, dequeue_function) if discipline != "PS" else MM1QueueSimulationProcessorSharing(service_rate)
    arrival_rate_values = np.linspace(1, 10, num_points, endpoint=False)

    waiting_time_values = []
    sojourn_time_values = []
    num_packets_in_system_values = []

    for arrival_rate in arrival_rate_values:
        packets_list = simulator.simulate(arrival_rate, num_arrivals)
        
        arrival_times = np.array([packet.arrival_time for packet in packets_list])
        departure_times = np.array([packet.departure_time for packet in packets_list])
        service_times = np.array([packet.service_time for packet in packets_list])

        waiting_times = departure_times - arrival_times - service_times
        sojourn_times = departure_times - arrival_times

        # waiting_time_values.append(np.mean(waiting_times))
        sojourn_time_values.append(np.mean(sojourn_times))
        num_packets_in_system_values.append(get_avg_num_packets_in_system(packets_list))

    if discipline != "PS":
        plt.plot(arrival_rate_values/service_rate, sojourn_time_values, marker = 'o')
        plt.plot(arrival_rate_values/service_rate, average_sojourn_time(arrival_rate_values, service_rate))
        plt.xlabel('Load $\lambda/\mu$')
        plt.ylabel('Average Sojourn Time')
        plt.title(discipline + " Sojourn Times")
        plt.legend(["Simulated", "Theoretical"])
        plt.savefig(discipline + "_sojourn_time"+ ".png")
        plt.clf()

        plt.plot(arrival_rate_values/service_rate, num_packets_in_system_values, marker = 'o')
        plt.plot(arrival_rate_values/service_rate, average_sojourn_time(arrival_rate_values, service_rate) * arrival_rate_values)
        plt.xlabel('Load $\lambda/\mu$')
        plt.ylabel('Average Number of Packets in the system')
        plt.title(discipline + " Number of Packets in the system")
        plt.legend(["Simulated", "Theoretical"])
        plt.savefig(discipline + "_num_packets"+ ".png")
        plt.clf()

    else:
        plt.plot(arrival_rate_values/service_rate, sojourn_time_values, marker = 'o')
        plt.xlabel('Load $\lambda/\mu$')
        plt.ylabel('Average Sojourn Time')
        plt.title(discipline + " Sojourn Times")
        plt.legend(["Simulated"])
        plt.savefig(discipline + "_sojourn_time"+ ".png")
        plt.clf()

        plt.plot(arrival_rate_values/service_rate, num_packets_in_system_values, marker = 'o')
        plt.xlabel('Load $\lambda/\mu$')
        plt.ylabel('Average Number of Packets in the system')
        plt.title(discipline + " Number of Packets in the system")
        plt.legend(["Simulated"])
        plt.savefig(discipline + "_num_packets"+ ".png")
        plt.clf()