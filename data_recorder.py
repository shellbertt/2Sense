# manage data recording
# based off of https://brainflow.readthedocs.io/en/stable/Examples.html#python-get-data-from-a-board

import argparse
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
import numpy

def save_data():
    data = board.get_board_data()  # get all data and remove it from internal buffer
    eeg_channels = BoardShim.get_eeg_channels(args.board_id)
    time_stamp_channel = BoardShim.get_timestamp_channel(args.board_id)
    marker_channel = BoardShim.get_marker_channel(args.board_id)
    rows_of_interest = eeg_channels + [time_stamp_channel] + [marker_channel]
    rows = numpy.stack([data[row] for row in rows_of_interest])
    numpy.savetxt('data', rows)

def begin_recording():
    pass

def end_recording():
    board.stop_stream()
    board.release_session()

def main():
    BoardShim.enable_dev_board_logger()

    parser = argparse.ArgumentParser()
    # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False,
                        default=0)
    parser.add_argument('--ip-port', type=int, help='ip port', required=False, default=0)
    parser.add_argument('--ip-protocol', type=int, help='ip protocol, check IpProtocolType enum', required=False,
                        default=0)
    parser.add_argument('--ip-address', type=str, help='ip address', required=False, default='')
    parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='')
    parser.add_argument('--mac-address', type=str, help='mac address', required=False, default='')
    parser.add_argument('--other-info', type=str, help='other info', required=False, default='')
    parser.add_argument('--serial-number', type=str, help='serial number', required=False, default='')
    parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards',
                        required=True)
    parser.add_argument('--file', type=str, help='file', required=False, default='')
    parser.add_argument('--master-board', type=int, help='master board id for streaming and playback boards',
                        required=False, default=BoardIds.NO_BOARD)
    parser.add_argument('--preset', type=int, help='preset for streaming and playback boards',
                        required=False, default=BrainFlowPresets.DEFAULT_PRESET)
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.ip_port = args.ip_port
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    params.other_info = args.other_info
    params.serial_number = args.serial_number
    params.ip_address = args.ip_address
    params.ip_protocol = args.ip_protocol
    params.timeout = args.timeout
    params.file = args.file
    params.master_board = args.master_board
    params.preset = args.preset
    board = BoardShim(args.board_id, params)
    board.prepare_session()
    board.start_stream()
    time.sleep(.5)
    save_data()

if __name__ == "__main__":
    main()

