# manage data recording
# based off of https://brainflow.readthedocs.io/en/stable/Examples.html#python-get-data-from-a-board

import argparse
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
import numpy
class DataRecorder:
    def __init__(self, board_id, boardshim_params=BrainFlowInputParams):
        self.board_id = board_id
        BoardShim.enable_dev_board_logger()
        self.board = BoardShim(board_id, boardshim_params)
        self.board.prepare_session()

    def save_data(self):
        data = self.board.get_board_data()  # get all data and remove it from internal buffer
        eeg_channels = BoardShim.get_eeg_channels(self.board_id)
        time_stamp_channel = BoardShim.get_timestamp_channel(self.board_id)
        marker_channel = BoardShim.get_marker_channel(self.board_id)
        rows_of_interest = eeg_channels + [time_stamp_channel] + [marker_channel]
        rows = numpy.stack([data[row] for row in rows_of_interest])
        numpy.savetxt('data', rows)

    def begin_recording(self):
        self.board.start_stream()

    def end_recording(self):
        self.board.stop_stream()

    def finish(self):
        self.board.release_session()

def main():
    parser = argparse.ArgumentParser()
    # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False, default=0)
    parser.add_argument('--ip-port', type=int, help='ip port', required=False, default=0)
    parser.add_argument('--ip-protocol', type=int, help='ip protocol, check IpProtocolType enum', required=False, default=0)
    parser.add_argument('--ip-address', type=str, help='ip address', required=False, default='')
    parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='')
    parser.add_argument('--mac-address', type=str, help='mac address', required=False, default='')
    parser.add_argument('--other-info', type=str, help='other info', required=False, default='')
    parser.add_argument('--serial-number', type=str, help='serial number', required=False, default='')
    parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards', required=True)
    parser.add_argument('--file', type=str, help='file', required=False, default='')
    parser.add_argument('--master-board', type=int, help='master board id for streaming and playback boards', required=False, default=BoardIds.NO_BOARD)
    parser.add_argument('--preset', type=int, help='preset for streaming and playback boards', required=False, default=BrainFlowPresets.DEFAULT_PRESET)
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

    dr = DataRecorder(args.board_id, params)
    dr.begin_recording()
    time.sleep(.5)
    dr.save_data()
    dr.end_recording()
    dr.finish()

if __name__ == "__main__":
    main()

