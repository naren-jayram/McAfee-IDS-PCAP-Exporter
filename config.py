import datetime

nsm_host = " "          	# NSM Hostname, ex: nsm.xyz.com
nsm_username = " "		    # NSM Username
nsm_password = " "		    # NSM Password
graylog_hostname = " "  	# Graylog Hostname
graylog_token = " "  		# Enter the graylog token here
graylog_stream = " "		# Graylog Stream ID; PCAPS part of this stream will be downloaded

# Edit below time frame details in case you need a manual date and time selection
from_date = "2018-08-20 00:00:00" #YYYY-MM-DD HH:MM:SS
to_date = "2018-08-26 00:00:00"   #YYYY-MM-DD HH:MM:SS


#Below code is for automation (Cron Job). If you wish to enable below automated time frames then please disable the above manual time frames (both here as well as 'graylog_pcap_link_exporter.py') and enable appropriate lines in graylog_pcap_link_exporter.py
# def cron_config():
# 	time_frame = []
# 	now = datetime.datetime.now()
# 	roundoff_today = now.replace(hour=00,minute=00,second=00)
# 	to_date = roundoff_today.strftime('%Y-%m-%d %H:%M:%S')

# 	yesterday_time = now - datetime.timedelta(days=1)
# 	roundoff_yesterday = yesterday_time.replace(hour=00,minute=00,second=00)
# 	from_date = roundoff_yesterday.strftime('%Y-%m-%d %H:%M:%S')
	
# 	time_frame.append(from_date)
# 	time_frame.append(to_date)
# 	return time_frame

# if __name__ == '__main__':
#   func = cron_config()
