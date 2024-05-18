from socket import *
import time 

# Creating a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# configuring port numbers
source_port_number = 8000
destination_port_number = 12000
destination_ip_address = "127.0.0.1"

# Assigning IP address and port number to socket
clientSocket.bind(('', source_port_number))

# Setting the timeout to one second, as the client will wait for one second for the response
clientSocket.settimeout(1)

rtt_times = []

num_packets = 10

for i in range(num_packets):

    sequence_number = i + 1
    send_time = time.time()

    # Creating the message object
    message_ascii = f"Ping {sequence_number} {send_time}"
    message = bytes(message_ascii, encoding = 'utf-8')

    # Sending the message
    clientSocket.sendto(message, (destination_ip_address, destination_port_number))

    # Implementing the receive mechanism along with timeout
    try:
        response_message, response_address = clientSocket.recvfrom(1024)
        print(response_message) 

        # Calcluating the round trip time
        received_time = time.time()
        rtt = received_time - send_time
        print(f"Round trip time for ping {sequence_number} is {rtt:.6f} seconds")

        rtt_times.append(rtt)
    except:
        print("Request timed out")


# Closing the socket
clientSocket.close()

# Calculating the average round trip time
avg_rtt = sum(rtt_times) / len(rtt_times)
print(f"Average round trip time is {avg_rtt:.6f} seconds")

# Calculating the minimum round trip time
min_rtt = min(rtt_times)
print(f"Minimum round trip time is {min_rtt:.6f} seconds")

# Calculating the maximum round trip time
max_rtt = max(rtt_times)
print(f"Maximum round trip time is {max_rtt:.6f} seconds")

# Calculating the packet loss rate
packet_loss_rate = (num_packets - len(rtt_times)) / num_packets
print(f"Packet loss rate is {packet_loss_rate:.2f}")