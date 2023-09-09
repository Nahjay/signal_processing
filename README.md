# signal_processing


## Overview
This Python script demonstrates signal filtering using the SciPy library. It generates and plots two signals: an original sine wave with a frequency of 1 Hz and a filtered sine wave with a frequency of 2 Hz. The filtering process is performed using a Butterworth low-pass filter.

## Dependencies
- Python 3
- NumPy
- Matplotlib
- SciPy

## How to Use
1. Make sure you have Python and the required libraries installed.
2. Clone this repository or download the script (`signal_filtering.py`) to your local machine.
3. Run the script using a Python interpreter.

## Code Description
- The script creates two sine waves: one for the original signal and another for the filtered signal.
- It defines a Butterworth low-pass filter with specified filter order and cutoff frequency.
- The filter is applied to the filtered sine wave using the `signal.filtfilt` function.
- Two separate plots are generated: one for the original signal and one for the filtered signal.
- The plots display amplitude over time.

## Screenshots
![Original Signal](original_signal.png)
*Original Signal (1 Hz sine wave)*

![Filtered Signal](filtered_signal.png)
*Filtered Signal (2 Hz sine wave after applying the Butterworth filter)*

## License
This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to use and modify this code for educational or personal projects.

For more information, visit my [GitHub portfolio](https://github.com/nahjay).

## Contact
- Email: nahjaybattieste@gmail.com
- LinkedIn: [Nahjay Battieste](https://www.linkedin.com/in/nahjay-battieste-a84655224)
