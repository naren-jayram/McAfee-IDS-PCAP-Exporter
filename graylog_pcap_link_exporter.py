import re
import config
import commands
import json
import csv

# Manual Configuration
graylog_host = config.graylog_hostname
token = config.graylog_token
stream_id = config.graylog_stream
temp_from_date = config.from_date 		# If Manual Time Frame Selection in config
temp_to_date = config.to_date           # If Manual Time Frame Selection in config
# End of Manual Configuration

def graylog_export(): 
	pkt_capture= []
	# auto_config_timeframe = config.cron_config()	# If Automated Time Frame Selection in config
	# temp_from_date = auto_config_timeframe[0]		# If Automated Time Frame Selection in config
	# temp_to_date = auto_config_timeframe[1]		# If Automated Time Frame Selection in config

	from_regex = re.search('(.*)[\s]+(\d\d):(\d\d):(\d\d)',temp_from_date)
	from_date = from_regex.groups()[0]
	from_hour = from_regex.groups()[1]
	from_mins = from_regex.groups()[2]
	from_secs = from_regex.groups()[3]
	to_regex = re.search('(.*)[\s]+(\d\d):(\d\d):(\d\d)',temp_to_date)
	to_date = to_regex.groups()[0]
	to_hour = to_regex.groups()[1]
	to_mins = to_regex.groups()[2]
	to_secs = to_regex.groups()[3]

	url = "https://{}:9000/api/search/universal/absolute?query=device_vendor%3AMcAfee%20AND%20streams%3A{}&from={}%20{}%3A{}%3A{}&to={}%20{}%3A{}%3A{}&fields=Packet_Capture_Link_RT".format(graylog_host,stream_id,from_date,from_hour,from_mins,from_secs,to_date,to_hour,to_mins,to_secs)
	curlCmd = "curl -k -u %s:token -X GET '%s' > packet_capture.csv" %(token,url)
	output = commands.getoutput(curlCmd)
	
	with open('packet_capture.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		reader.next()
		for row in reader:
			pkt_capture.append(row[1])
	
	return list(pkt_capture)
		

if __name__ == '__main__':
  func = graylog_export()