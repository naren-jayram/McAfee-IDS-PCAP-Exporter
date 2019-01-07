import requests
import csv
import re
import graylog_pcap_link_exporter
import config
import urllib3
from termcolor import colored

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #Suppress InsecureRequestWarning


nsm_host = config.nsm_host  	# NSM Hostname
session = requests.Session()  	# Establishing HTTPS Session to grab PCAPs
http_data = {"iaction": "login", "node": "", "bwVer": "999", "Login%20ID": config.nsm_username, "password": config.nsm_password}
url = "https://%s/intruvert/jsp/module/Login.jsp" %(nsm_host) 
headers = {"Host": nsm_host,
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.5", "Content-Type": "application/x-www-form-urlencoded",
           "Upgrade-Insecure-Requests": "1"}
request = session.post(url, headers=headers, data=http_data, cookies=session.cookies, verify=False)

# PCAP files will be saved as 'AlertID(uuid).pcap' which is unique to each Graylog message
print(colored("Stage 1 of 2: Exporting PCAP links from Graylog... ", 'red'))
pkt_capture_list = graylog_pcap_link_exporter.graylog_export()
print ("PCAP links from Graylog has been exported! ")
print(colored("Stage 2 of 2:  Writing PCAP files to disk... ", 'red'))

for pcap_url in pkt_capture_list:
    PCAP = session.get(pcap_url, cookies=session.cookies)
    alert_ID = re.search('.*sensorAlertUUID\=([\d]+)&.*', pcap_url)
    alert = alert_ID.groups()[0]
    with open("%s.pcap" %alert, "wb") as pcap_file:
        pcap_file.write(PCAP.content)

print ("PCAP files are now stored in a repository!")