import unittest
from libs.ip_lib import get_local_ip
from libs.log_lib import setup_logging
import logging

class Tests_IP(unittest.TestCase):

    valid_ip_list = ["192.168.178.25"]
    def test_uci_to_square(self):
        ip = get_local_ip()
        print(f"IP: {ip}")
        result = (ip in self.valid_ip_list)
        self.assertEqual(result, True)
        
if __name__ == '__main__':
    setup_logging()
    logging.info("Start Tests")
    unittest.main()
    logging.info("End Tests")

