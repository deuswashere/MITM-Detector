import os
import re
import time
import colorama
from colorama import Fore, Style
import winsound

frequency = 2500  # Hz
duration = 300  # millisecond


def find_mac(ip_address):
    output = os.popen('arp -a').read()
    lines = output.split('\n')
    for line in lines:
        if ip_address in line:
            mac = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line)
            if mac:
                return mac.group(0)
    return None

def check_mitm():
    # Modem IP address
    modem_ip = "192.168.1.1"
    
    colorama.init()
    print(Fore.GREEN + "[+] You are safe now." + Style.RESET_ALL)
    stop = False
    last=False
    while not stop:
        
            output = os.popen('arp -a').read()
            lines = output.split('\n')
            mitm_detected = False
            for line in lines:
                # Find IP address
                ip_address = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
                if ip_address:
                    ip_address = ip_address[0]
                    
                    if ip_address == modem_ip:
                        continue
                    mac_address = find_mac(ip_address)
                    modem_mac = find_mac(modem_ip)
                    # If the MAC address is the same as the modem address, give a warning
                    if mac_address == modem_mac:
                        mitm_detected = True
                        last=mitm_detected
                        winsound.Beep(frequency, duration)
                        winsound.Beep(frequency, duration)
                        winsound.Beep(frequency, duration)
                        winsound.Beep(frequency, duration)
                        winsound.Beep(frequency, duration)
                        winsound.Beep(frequency, duration)
                        print(Fore.RED + f"[!] It could be a MITM attack! There is an anomaly between the device at {ip_address} and the modem." + Style.RESET_ALL)
                        time.sleep(5)
                        break
            if not mitm_detected and mitm_detected!=last:
                print(Fore.GREEN + "[+] You are safe now." + Style.RESET_ALL)
                last=mitm_detected
                time.sleep(5)

if __name__ == '__main__':
    check_mitm()