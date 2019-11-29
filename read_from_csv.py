def get_devices_from_csv(filename=str()):
    """
    This Function is to read the input file and converting to dict
    :param filename: Input filename for reading csv file
    :return: In dict format of router and rest details of csv file
    """
    devices_and_commands = dict()
    logging.info("The input file is %s" % filename)
    try:
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                router_ip = row['Router IP']
                cmd = row['CMD']
                cust_name = row['Customer']
                full_details = (cmd, cust_name)
                if router_ip not in devices_and_commands:
                    devices_and_commands[router_ip] = [full_details]
                else:
                    devices_and_commands[router_ip].append(full_details)
    except (FileNotFoundError, IOError) as file_error:
        logging.error("Wrong file or file path/ No such file or directory --> %s" % file_error)
        return False
    return devices_and_commands
    

input_csv_filename = 'xyz.csv'
devices_and_commands = get_devices_from_csv(input_csv_filename)
