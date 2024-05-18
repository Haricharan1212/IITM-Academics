from scapy.all import *
import csv

def get_networks(pcap_file):
    """This function gets all the Wi-Fi networks available, along with their parameters."""

    # initializing empty network set and output table
    networks = set()
    RSSI_values = dict()
    output_table = [["SSID", "BSSID", "Channel", "Capability", "Band", "Average RSSI"]]

    # rdpcap reads the pcap file
    packets = rdpcap(pcap_file)

    # iterating over all the packets
    for packet in packets:

        # Checking if it is a beacon frame
        if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):

            # getting all the desired parameters
            ssid = packet[Dot11Elt].info.decode("utf-8")
            bssid = packet[Dot11].addr3
            channel = int(ord(packet[Dot11Elt:3].info))
            capability = packet.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}{Dot11ProbeResp:%Dot11ProbeResp.cap%}").strip()                
            rssi_value = packet.dBm_AntSignal

            if (ssid not in RSSI_values):
                RSSI_values[ssid] = [rssi_value]
            else:
                RSSI_values[ssid].append(rssi_value)

            if packet[RadioTap].ChannelFrequency < 2484:
                band = "2.4 GHz"
            else:
                band = "5 GHz"

            # adding to table if it is not in networks
            if ssid not in networks:
                networks.add(ssid)
                output_table.append([ssid, bssid, channel, capability, band, -1])

    # Calculating average RSSI for each SSID
    for i in range(1, len(output_table)):

        rssi_values_ssid = RSSI_values[output_table[i][0]]
        output_table[i][5] = sum(rssi_values_ssid) / len(rssi_values_ssid)

    return output_table

# Example
for pcap_file in ["captured.pcap", "my_capture.pcap"]:

    networks = get_networks(pcap_file)

    with open (f'output_{pcap_file}.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(networks)

    print(f"Available networks in {pcap_file}:")
    for network in networks:
        print(network)