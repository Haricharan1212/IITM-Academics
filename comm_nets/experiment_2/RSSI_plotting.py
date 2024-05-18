from scapy.all import *
import os
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np

def get_avg_rssi(pcap_file, username):
    # getting average RSSI

    RSSI_values = []
    packets = rdpcap(pcap_file)

    for packet in packets:
        if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp) and packet.haslayer(Dot11Elt):

            ssid = packet[Dot11Elt].info.decode("utf-8")

            # Checking if SSID is the desired one
            if (ssid == username):
                rssi_value = packet[RadioTap].dBm_AntSignal
                RSSI_values.append(rssi_value)
        
    # Computing average RSSI
    avg_rssi_value = sum(RSSI_values) / len(RSSI_values)

    return avg_rssi_value

def analyze_pcaps():

    freqs = [["2.4ghz", "wyfy"], ["5ghz", "iitmwifi"]]

    datas = []
    distances = set()

    for freq, username in freqs:

        data = []

        # analysing the pcap file
        for pcap_file in os.listdir(freq):

            print(pcap_file)

            distance, num_walls, _ = pcap_file.split("_")
            distance = float(distance[:-1])
            num_walls = int(num_walls[:-1])

            avg_rssi = get_avg_rssi(f"{freq}/{pcap_file}", username)
            distances.add(distance)

            print(f"{distance=}, {num_walls=}, {avg_rssi=}")
            data.append([float(freq[:-3]), distance, num_walls, avg_rssi])

        datas.append(data)

    datas = np.array(datas)
    np.save("data", datas)

def plot_cdf(data, freq):

    for num_walls in [0, 1, 2]:

        data_plot = data[data[:, 2] == num_walls][:, 3]

        n, bins, patches = plt.hist(data_plot, 100,
                            cumulative=True, label=f'Number of walls = {num_walls}')

    plt.title(f"CDF for {freq}")
    plt.ylabel("CDF")
    plt.xlabel("RSSI value (dBm)")
    plt.legend(loc='upper left')
    plt.savefig(f"cdf_{freq}.png")    
    plt.clf()

def scatter_plot(data_0, data_1):

    xs = []
    ys = []

    for num_walls in [0, 1, 2]:
        x = []
        y = []
        for i in data_0:
            for j in data_1:
                if (i[1] == j[1]) and (i[2] == j[2]) and (i[2] == num_walls):
                    x.append(i[3])
                    y.append(j[3])
                    xs.append(i[3])
                    ys.append(j[3])
                    num_walls = i[2]

        
        if (len(x) == 0): continue

        plt.scatter(x, y, label = f"Number of Walls = {num_walls}")
        
        # plot fit line

    popt = np.polyfit(xs, ys, 1)
    print(f"The coefficients of the linear relation was: {popt}")

    plt.plot(np.unique(xs), np.poly1d(np.polyfit(xs, ys, 1))(np.unique(xs)))
    plt.xlabel("2.4GHz")
    plt.ylabel("5GHz")
    plt.title(f"Scatter plot")
    plt.legend()
    plt.savefig(f"scatter_plot.png")

# Function for scipy curve fit
def rssi_predictor(vector, RSSIref, path_loss_exp, walls_attenuation_factor):

    distance, num_walls = vector

    return RSSIref + 10 * path_loss_exp * np.log(distance) + walls_attenuation_factor * num_walls

def path_loss_relation(data):

    data = np.array(data)

    new_data = []
    for i in data:
        if (i[2] <= 2):
            new_data.append(i)

    data = np.array(new_data)

    x = data[:, [1, 2]]
    y = data[:, 3]

    popt, pcov = curve_fit(rssi_predictor, x.T, y)

    RSSIref, path_loss_exp, walls_attenuation_factor = popt
    print(f"{RSSIref=}, {path_loss_exp=}, {walls_attenuation_factor=}")

def signal_interferer_power(pcap_file):
    """This function gets all the Wi-Fi networks available, along with their parameters."""

    # initializing empty network set and output table
    networks = set()
    signal_RSSI_values = []
    interferer_RSSI_values = []

    # rdpcap reads the pcap file
    packets = rdpcap(pcap_file)

    # iterating over all the packets
    for packet in packets:

        # Checking if it is a beacon frame
        if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):

            # getting all the desired parameters
            ssid = packet[Dot11Elt].info.decode("utf-8")
            rssi_value = packet.dBm_AntSignal

            if ssid == "iitmwifi":
                signal_RSSI_values.append(rssi_value)
            else:
                interferer_RSSI_values.append(rssi_value)

    # Calculating average RSSI for each SSID
    try:
        signal_avg_RSSI = sum(signal_RSSI_values) / len(signal_RSSI_values)
        interferer_avg_RSSI = sum(interferer_RSSI_values) / len(interferer_RSSI_values)
    except:
        signal_avg_RSSI = 0
        interferer_avg_RSSI = 0    
    interferer_avg_RSSI = sum(interferer_RSSI_values) / len(interferer_RSSI_values)


    return signal_avg_RSSI, interferer_avg_RSSI

def signal_interferer_scatter_plot(freq):

    x = []
    y = []

    for pcap_file in os.listdir(freq):

        signal_avg_RSSI, interferer_avg_RSSI = signal_interferer_power(f"{freq}/{pcap_file}")

        if (signal_avg_RSSI == 0 or interferer_avg_RSSI == 0):
            continue

        x.append(signal_avg_RSSI)
        y.append(interferer_avg_RSSI)


    plt.scatter(x, y)
    plt.xlabel("Signal RSSI")
    plt.ylabel("Interferer RSSI")
    plt.title("Signal vs Interferer RSSI")
    plt.savefig(f"signal_interferer_scatter_plot_{freq}.png")
    plt.cla()

# analyze_pcaps()

# Part 1, Part 2
datas = np.load("data.npy", allow_pickle = True)
data_0 = np.array(datas[0])
data_1 = np.array(datas[1])

# Part 3a
plot_cdf(data_0, "2.4GHz")
plot_cdf(data_1, "5GHz")

# Part 3b
scatter_plot(data_0, data_1)

# Part 3c
path_loss_relation(datas[0])
path_loss_relation(datas[1])

# Part 3d
signal_interferer_scatter_plot("2.4ghz")
signal_interferer_scatter_plot("5ghz")