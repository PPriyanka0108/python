import netmiko
import paramiko

def test_ssh_login(ip, hname, uname, paswd):
    """
    Method to fetch the list of context configured on the provided Firewall Device IP
    :param ip: IP address of the Device
    :param hname: Hostname of the device
    :param uname: Username
    :param paswd: Password
    :return: WORKING | NOT WORKING | FAILED
    """
    my_device = {
        "host": ip,
        "username": uname,
        "password": paswd,
        "secret": paswd,
        "device_type": "cisco_ios",
    }

    try:
        net_connect = netmiko.ConnectHandler(**my_device)
        net_connect.enable()
        logging.info("Successfully logged into %s(%s)" % (hname, ip))
        net_connect.disconnect()
        return "WORKING"
    except EOFError as eof_err:
        logging.error("Hit EOFError while accessing %s(%s) via SSH from %s - %s"
                      % (hname, ip, socket.getfqdn(), str(eof_err)))
        return "NOT REACHABLE"
    except OSError as os_err:
        logging.error("Hit OSError while accessing %s(%s) via SSH from %s - %s"
                      % (hname, ip, socket.getfqdn(), str(os_err)))
        return "NOT REACHABLE"
    except netmiko.NetMikoTimeoutException as timeout_err:
        logging.error("Device connection timeout while accessing %s(%s) via SSH from %s - %s"
                      % (hname, ip, socket.getfqdn(), str(timeout_err)))
        return "NOT REACHABLE"
    except netmiko.NetMikoAuthenticationException as net_err:
        logging.error("%s is not authorized to access %s(%s) via SSH from %s - %s"
                      % (uname, hname, ip, socket.getfqdn(), str(net_err)))
        return "NOT WORKING"
    except paramiko.ssh_exception.SSHException as ssh_err:
        logging.error("Signature verification (ssh-rsa) failed for %s(%s) - %s" % (hname, ip, str(ssh_err)))
        return "FAILED"

    
test_ssh_login('10.10.10.10', 'asr', 'priyanka', 'xyz')
