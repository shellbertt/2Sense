# perform filtering on data file and write filtered data

import numpy
import brainflow
import brainflow.board_shim as bs
import brainflow.data_filter as df
import sys

def main(file):
    # Load data
    try:
        data = numpy.loadtxt(file)
    except FileNotFoundError:
        print(f'file "{file}" not found')
        exit()
    eeg = numpy.stack(data[:3]) # channel 3 (4th) not working on our equipment
    time_stamps = data[4]
    markers = data[5]

    # Applu filters to data
    sampling_rate = bs.BoardShim.get_sampling_rate(ID)
    for i in range(len(eeg)):
        # data (NDArray[Float64]), sampling_rate (int), noise_type (int)
        df.DataFilter.remove_environmental_noise(eeg[i], sampling_rate, df.NoiseTypes.SIXTY)
        # data (NDArray[Float64]), sampling_rate (int), start_freq (float), stop_freq (float), order (int), filter_type (int), ripple (float)
        df.DataFilter.perform_bandpass(eeg[i], sampling_rate, .05, 30, 2, df.FilterTypes.BUTTERWORTH, 0)

    # Split data into epochs at proprioceptive stimuli markers
    non_zero_markers = numpy.nonzero(markers)[0]
    split_eeg = numpy.array([numpy.array_split(eeg[j], non_zero_markers) for j in range(len(eeg))])

    # calculate baseline activity before each stimulus
    baselines = numpy.array([[numpy.mean(epoch[:-100]) for epoch in channel[:-1]] for channel in split_eeg])

    # shorten to 500ms where result of stimulus will be most apparent
    split_eeg = numpy.array([[epoch[:200] for epoch in channel[1:]] for channel in split_eeg])

    # subtract baseline
    split_eeg = numpy.array([[split_eeg[i][j] - baselines[i][j] for j in range(len(split_eeg[0]))] for i in range(len(split_eeg))])

    # average across epochs
    avg_egg = numpy.array([numpy.add(*channel) / len(channel) for channel in split_eeg])

    # Save data
    numpy.savetxt(file + '_filtered', numpy.stack([channel for channel in eeg] + [time_stamps] + [markers]))

if __name__ == '__main__':
    ID = bs.BoardIds.GANGLION_BOARD # The id of our board
    try:
        main(sys.argv[1])
    except IndexError:
        print('provide data file as argument')
