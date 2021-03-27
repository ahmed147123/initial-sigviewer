import h5py
import numpy as np

import matplotlib.pyplot as plt




h5file = h5py.File("sampleECG.h5", 'r')


x=list(h5file.keys())
print(x[0])
h5_group = h5file.get(x[0])
sampling_rate = h5_group.attrs.get("sampling rate")
h5_sub_group = h5_group.get("raw")
h5_data = h5_sub_group.get("channel_1")

data_list = [item for sublist in h5_data for item in sublist]

# time = bsnb.generate_time(data_list, sampling_rate)

# print (array([item for sublist in h5_data for item in sublist]))

# bsnb.plot([time], [data_list], x_axis_label="Time (s)", y_axis_label="Raw Data")
