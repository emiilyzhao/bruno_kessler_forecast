## Variables

1. **Geospatial Series**

Visualizes data points on a world map. Each point represents a specific geographic location, and the variable being plotted is indicated by a color scale. This allows for easy identification of spatial patterns and trends across different regions.

2. **Time Series**

Displays data points over a continuous time interval. The x-axis represents time in UTC and milliseconds, while the y-axis represents the variable being measured. This type of graph is ideal for observing how a variable changes over time, identifying trends, and forecasting future values.

3. **Spectrograph**

Time is plotted on the x-axis and another variable on the y-axis. The density of occurrences for each point is represented using a color scale. This type of graph is useful for visualizing how the distribution of a variable changes over time, highlighting areas of higher density or frequency.

| Instrument | Geospatial Series | Time Series | Spectrograph
|-|-|-|-|
| EFD | N/A | X/Y/Z/Vector Waveforms <br> Polar/Azimuth Angles | X/Y/Z Power Spectrum
| SCM | Electric Field Magnitude | N/A | X/Y/Z/Vector Waveforms <br> Polar/Azimuth Angles | X/Y/Z Power Spectrum |
| LAP | Electron Density/Temperature | Electron Density/Temperature | N/A |
| HEPP-L | Electron/Proton Counts | Electron/Proton Counts | Electron/Proton Energy <br> Electron Pitch Angle |
| HEPP-H | Electron/Proton Counts | Electron/Proton Counts |Electron/Proton Energy <br> Electron/Proton Pitch Angle 
| HEPP-X | N/A | X-Ray Counts | X-Ray Energy 
| HEPD | Electron/Proton Counts | Electron/Proton Counts | Electron/Proton Energy 

## Filters
1. **Geospatial Map** 

Draw a polygon on a map, defining a specific area of interest. The webapp will return data points that are located within the coordinates of the drawn polygon. This filter is useful for focusing on data from particular geographic regions.

2. **Time**

Specify a start and end time. The webapp will return data that falls within this defined time range. This filter is ideal for analyzing data over a selected period, allowing users to observe trends and patterns within the chosen timeframe.

3. **Payload**

Select one or multiple sensor types. The webapp will then return data collected from the specified sensors. This filter helps users focus on data from particular types of sensors, providing insights based on the selected sensor data.

4. **Orbit**

Choose one or multiple orbits. The webapp will return data from the selected orbits. This filter is beneficial for examining data collected during specific orbital paths, enabling targeted analysis based on the chosen orbits.

## Graphical Analysis 

1. **Statistical Summary**

Plots key statistical measures over time, including the lowest value, 1st quartile, median, mean, 3rd quartile, and highest value. This analysis provides a comprehensive overview of the data distribution and its central tendency, helping users understand the range and spread of their data over time.

2. **Aggregated** 

Combines multiple files and plots them together on a single graph with latitude on the x-axis. This method is used for time series line graphs, enabling users to compare data from different files in a consolidated view, highlighting geographical trends and patterns.


3. **Sequential**

Takes multiple files and plots them next to each other with time on the x-axis. This analysis works for all types of graphs, including geospatial, time series, and spectrograph. It allows users to observe and compare data from different files in a sequential manner, facilitating the identification of temporal trends and changes.

3. **Point Density**

Plots a spectrogram with map with latitude on the y-axis and longitude on the x-axis. The grids are colored using a color scale that represents the frequency of data points in each location. This analysis helps users visualize the density and distribution of data points geographically, making it easier to identify areas with higher concentrations of data.