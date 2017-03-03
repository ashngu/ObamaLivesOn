from bs4 import BeautifulSoup
import requests
import csv

with open ('obamaschedule.txt', 'wb') as txtfile:
	obamawriter = csv.writer(txtfile, delimiter='\t')
	# creates txt file with content, url, publish date columns
	csvrow = []
	for urlNum in range(1, 183):
		url = "https://obamawhitehouse.archives.gov/blog?page=" + str(urlNum)
		r  = requests.get(url)

		data = r.text

		soup = BeautifulSoup(data, "lxml")

		# for daily schedule summaries
		for schedule in soup.find_all('div', class_='views-field-field-daily-guidance-date'):
			schedule = schedule.parent
			dayDate = schedule.find('div', class_='views-field-field-daily-guidance-date').find('span', class_='date-display-single')['content']
			description = schedule.find('div', class_='views-field-field-forall-body').find('div', class_='field-content').get_text().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').encode('utf-8').strip('\n')
			obamawriter.writerow([description, url, dayDate])

		# for daily events
			for event in schedule.find_all('tr'):
				if event.find('span', class_='date-display-single'):
					event_date = event.find('span', class_='date-display-single')['content']
					event_name = event.find('p', class_='schedule-event-name').string.encode('utf-8')
					event_location = event.find('span',class_='event-info-location')
					if event_location:
						event_location = event_location.string.encode('utf-8')
					else:
						event_location = ''
					event_description = event_name + ". " + event_location
					obamawriter.writerow([event_description, url, event_date])