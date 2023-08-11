import logging
import datetime
import os

class FEN_Eval_Collector():

    def __init__(self, file_path, file_info):
        current_datetime = self.datetime2str()  
        filename = "fen_eval_" +file_info + "_" + current_datetime + ".csv"
        self.outfile = open(os.path.join(file_path, filename), "w")
        logging.debug(f"Stats File created {filename} in {file_path}")
        self.index = 0

    def __del__(self):
        self.outfile.flush()
        self.outfile.close()

    def datetime2str(self):
        # Get the current datetime
        current_datetime = datetime.datetime.now()

        # Convert it to a string with a specific format
        # For example, to display the date and time in ISO 8601 format:
        return current_datetime.strftime('%Y_%m_%d_%H_%M_%S')

    def write_pos(self, pos, eval, mate):
        self.outfile.write(f"{pos};{eval};{mate}\n")
        self.index += 1
        if self.index == 100:
            self.index = 0
            self.outfile.flush()