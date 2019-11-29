import csv
import errno
import urllib.request
from datetime import datetime 

def download_file():
    """
    This function is to download the file from the Url link
    :return: File in date_and_time format
    """
    try:
        with urllib.request.urlopen('http://www.google.com') as f_open:
            csv_read_data = f_open.readlines()[4:]
        download_filename = datetime.strftime(datetime.now(),'vpn_%Y-%m-%d_%H_%M_%S.csv')
        with open(download_filename, "w") as csvFile:
            csv_file_writer = csv.writer(csvFile)
            csv_file_writer.writerow(['Description', 'Router IP', 'CMD', 'Location', 'Customer'])
            for line in csv_read_data:
                line = line.decode()
                replace_line = line.replace(' | ', ',').strip('|').lstrip().replace(' |','')
                csvFile.write(replace_line)

        ''' Check the list of vpn files in the Current directory and took the lastest file as input file '''
        input_file_list = os.listdir('.')
        #Check the list of files in  Temp Directory
        # input_file_list = os.listdir('output_dir')
        input_file_list.sort()
        input_file_len = len(input_file_list)
        while input_file_len > 0:
            if 'vpn_20' in input_file_list[input_file_len - 1]:
                input_filename = input_file_list[input_file_len - 1]
                break
            input_file_len -=1
    except urllib.error.URLError as url_error:
        logging.error("No network connection or No route to the specified server or"
                      " The specified server does not exist --> %s" % url_error.reason)
    except urllib.error.HTTPError as http_error:
        logging.info("The server couldn\'t fulfill the request.")
        logging.error("Http Error Code --> %d" % http_error.code)
        logging.error("http Error Text --> %s" % http_error.read())
    return input_filename

#To call the Function
input_filename = download_file()
