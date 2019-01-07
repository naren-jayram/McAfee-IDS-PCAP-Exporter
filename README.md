## McAfee NSM - IDS Alert PCAP Exporter
Downloads the PCAP files associated with the IDS alerts from McAfee NSM in a given time frame.

**Flow:**
McAfee NSM --> Graylog 

### Use Cases
* You are investigating on some incident and want to pull all the relevant PCAP files associated with it. You can achieve this by making appropriate modificatons to the *url* field in *graylog_pcap_link_exporter.py*
* You can use the concerned/interested PCAPs to train a Machine Learning model 
* To retain PCAP files for the later reference. Note: PCAP files will be deleted after certain date/ storage threshold from McAfee NSM.

### Pre-requisites
* McAfee NSM access.
* Graylog has to be installed and it should be receiving alerts from McAfee NSM. Also, One of the alert/message fields should contain the link to alert's PCAP file in McAfee NSM
* Appropriate *Streams* and *Pipelines* should exist in Graylog. Refer *Sample Graylog Pipeline* Rules 

**Why are we pulling PCAP links from *Graylog* instead of downloading it staright from McAfee NSM?**
Graylog concepts, *Streams* and *Pipelines* gives us more flexibility when it comes to searching for particular IDS alerts. If we are downloading the PCAP files from McAfee NSM for a given time frame, we may pull the irrelevant ones as well. Ofcourse, there exist a filtering criterion in McAfee NSM but it is not as granular as discussed Graylog concepts.

### Usage
```
python pcap_exporter.py
```
### Additional Info
1. If you don't have a Graylog access token, Creating one is simple. Just replace user_name with yours.
```
curl -u <user_name>:superpower -H 'Accept: application/json' -H 'X-Requested-By: cli' -X POST 'http://<Graylog IP>:9000/api/users/GM/tokens/mytoken?pretty=true'
```
2. If you are unsure of token existence 
```
curl -u <user_name:password> -k -H 'Accept: application/json' -X GET 'https://<Graylog_IP or Hostname>:9000/api/users/<user_name>/tokens/?pretty=true'
```
