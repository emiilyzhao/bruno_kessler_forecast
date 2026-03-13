# %% [markdown]
# Requirements: **numpy**, **matplotlib**, **h5py**, **datetime**, (scipy, pandas, ...)
# 
# I assume you know how to install these packages if you do not have them already. In anaconda they should be already installed by default. In python you simply do 
# 
# 
# ```
# pip3 install h5py datetime numpy matplotlib
# ```
# 
# Let's begin with finding where our files are located

# %%
import numpy as np
import pylab as plt
import h5py
from glob import glob
from datetime import datetime,timedelta
from efdpy.utils import *
data_folder = 'C:\\Users\\darmo\\PowerFolders\\POSTPHD\\Lectures\\webvalley2024Trento\\Small_samples\\'
files = glob(data_folder+'*.h5')


# %% [markdown]
# We can parse our filename to get some useful info: we do it with a special parsing function `parse_CSES_filename`

# %% [markdown]
# We now take one file and see the information we can get from its file name

# %%
ifile = files[0]
strfile = ifile.split('\\')[-1]

file_info = parse_CSES_filename(strfile)
file_info

# %% [markdown]
# Now we look how the file is made. It is an HDF5 file format. So we need the **h5py** package, that we already imported.

# %%
fil = h5py.File(ifile,'r')

fil.keys()

fil['A111_W'].shape

# %% [markdown]
# It does not look like a timeseries, is a 2D array. Why? The reason is that EFD waveforms (also SCM) are subdivided in packets (256 in ULF, 2048 in ELF). The timeseries is actually the flattened array.

# %%
ifile
plt.plot(fil['A111_W'].flatten())

# %% [markdown]
# We got an error because fil['A111_W'] is not exactly our array, but is the hdf5 dataset containing the array. To plot it we need to add ```[...]``` to the syntax: 

# %%
fil['A111_W']

# %%
Ex=fil['A111_W'][...]

Ex

# %%
Ex.flatten()


# %%
Ex.flatten().shape

plt.plot(Ex.flatten())

# %% [markdown]
# 
# Now we need to add the information about time and what goes on the y-axis. Fortunately, the hdf5 format allows to also insert metadata infos about what is in the data (granted that someone put that information). We can see the information about the field 'A111_W' with the following command

# %%
fil['A111_W'].attrs['units']

# %% [markdown]
# The information tells us that this dataset is in units of mV/m, i.e. $10^-3$ V/m.
# The array containing the time information is TIME_VERSE, and it gives the time of the first datapoint of each packet. Since our field 'A111_W' is subdivided in (1001,256), TIME_VERSE will be a 1D array of 1001 elements, each of them gives the time of, e.g., fil['A111_W'][:,0].
# 
# VERSE_TIME is given in milliseconds, and is the time since midnight of january 1, 2009. We can convert such number to a more useful format by using `datetime`. We now show a way to do it.

# %%
verse_time0 = datetime(2009,1,1) #UTC time offset of verse time

vtime = fil['VERSE_TIME'][...].flatten() #getting a flattened array of VERSE_TIMES in milliseconds

utime = verse_time0 + vtime*timedelta(milliseconds=1)


# %% [markdown]
# This is the plot with VERSE_TIME in milliseconds on the x-axis

# %%
plt.plot(fil['VERSE_TIME'][...],Ex[:,0])
plt.xlabel('VERSE_TIME (ms)')
plt.ylabel('mV/m')

# %%
plt.plot(utime,Ex[:,0])
plt.xlabel('UT time')
plt.ylabel('mV/m')

# %% [markdown]
# ## Problem 1
# Build a time array (can be datetime array or numpy array in seconds or whatever) of the same size of 'A111_W' so that we have the temporal position of each datapoint. 
# 
# **Question 1**: How would you do it?

# %%
dt = 1/125 #ULF sampling time

#using vtime
vtimefull = np.zeros(Ex.shape)
packetsize = vtimefull.shape[1]
for i,itime in enumerate(vtime):
    vtimefull[i] = np.arange(packetsize)*dt + itime


#using datetime
utimefull = [i+dt*timedelta(seconds=1)*np.arange(packetsize) for i in utime]

utimefull = np.array(utimefull)

# %%
plt.plot(utimefull.flatten(),Ex.flatten())

# %% [markdown]
# There is another issue related to timing: VERSE_TIME is an integer in milliseconds. This bring some issues in the discretization of timing, as can be easily seen here.
# 
# **Question 2**: How would you solve it? Is it so terrible to keep this error?
# 

# %%
np.diff(vtime)

# %% [markdown]
# While solving the issue related to the presence of this "bug", you have to keep in mind that gaps are present in the data:
# 

# %%
plt.plot(np.diff(vtime)/1000)

# %% [markdown]
# ## Problem 2
# 
# The data contains gaps of length 6.138 seconds. Why is that? 
# 
# The reason is that there are some telemetry packets that are lost. (It is an EFD issue to be aware of).
# 
# This gaps are not randomly distributed, so it seems it is something systematic happening to EFD
# 
# How do we see that?  [do it interactively with the following commands]
# 
# ```
# plt.ion()
# plt.plot(utimefull.flatten(),fil['A111_W'][...].flatten(),'.')
# plt.show()
# ```
# 
# Is this really an issue? Maybe not for everything you need to do in this school, but for time frequency analysis it can be an issue.
# 
# One thing is sure: you must be aware of the presence of jumps.
# 
# 

# %% [markdown]
# ### Reminder
# 
# Jumps/gaps are always followed by a spike in EFD data. These data should be excluded from any analysis.
# 

# %%
plt.plot(utimefull.flatten(),Ex.flatten(),linestyle='-',marker='.')
plt.xlim((utimefull[780][0],utimefull[810,0]))
plt.ylim((200,230))

# %%
### Problem 3

There are jumps present at every packet start. We can verify that this is true by typing the following commands

# %%
plt.plot(utimefull.flatten(),Ex.flatten())
plt.xlim((datetime(2019,12,19,23,59,30),datetime(2019,12,19,23,59,30)+timedelta(seconds=40)))
plt.ylim([-60,-35])
[plt.axvline(i,color='red',linestyle=':') for i in utime]

# %% [markdown]
# These jumps are an error of the processing pipeline of the Cses Chinese Ground Segment! (see slides)
# 
# The solution to this problem is conceptually easy to understand, but complicated to implement in a short python script.
# 
# Steps:
# 
# 1. calculate rotational gap (is a rotation matrix) $A$
# 2. calculate a linear increment in rotation along the packet such that $R(t=0) = 1$ and $R(t=\mathrm{endpacket}) = A$.
# 3. apply the rotation to get the modified vector electric field with no jumps $E_{good}(t) = R(t) E_{bad}(t)$

# %% [markdown]
# Doing all of that can be complicated. Fortunately, I have prepared a python script that does all that: **efd01_reprocessbin.py**.
# 
# **DISCLAIMER**: no warranty that the issues are all corrected, but that's real life when dealing with data.
# 
# the script takes in input one EFD .h5 file, and returns an .h5 file containing the same fields but with the above issues corrected
# 
# the command syntax is
# 
# `python3 efd01_reprocessbin.py --input <input_filename> [--output <output_filename>] [...]`

# %% [markdown]
# 


