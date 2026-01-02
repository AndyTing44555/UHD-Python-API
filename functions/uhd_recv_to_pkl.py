import uhd, os
import pandas as pd

def uhd_recv_to_pkl_v1(shouldsave,samp_rate,num_samps,data_dir):
    """RX samples and write to file"""
    my_usrp = uhd.usrp.MultiUSRP("type=b200")

    raw_data = my_usrp.recv_num_samps(
        num_samps, # Number of samples
        int(2.4e9), # Frequency in Hz
        samp_rate, # Sampling rate
        [0], # Receive on channel 0
        80, # 80 dB of RX gain
    )

    if shouldsave:
        if not os.path.exists(data_dir+"/tests"):
            os.makedirs(data_dir+"/tests")

        raw_data.pd.DataFrame.to_pickle(data_dir+f"/tests/samples_data_{num_samps:.0f}points.pkl")

    return num_samps, raw_data