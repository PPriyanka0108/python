import logging
from datetime import datetime

''' Creating filename with time stamp '''
datetimeStamp = datetime.datetime.now().strftime('%m%d%y_%H%M%S')
file_name = os.path.abspath(__file__).split("/")[-1].split('.py')[0] + '_' + datetimeStamp
log_filename = '/tmp/%s.log' % file_name
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: %(message)s', datefmt='%m%d%y %H:%M:%S')

''' Setup logging over console '''
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
