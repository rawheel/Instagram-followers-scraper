from time import sleep
import os
import sys
import pathlib
from timeit import default_timer as timer
import pandas as pd
import threading
import instaloader

# Get instance
L = instaloader.Instaloader()
pathlib.Path('downloads/').mkdir(parents=True, exist_ok=True)

#http = urllib3.PoolManager()

gen = []

def gon(i,count):

	j = str(i).split(" ")
	#print(count,j[1])
	gen.append(j[1])

def test(targeted_username):
    	
	#pro = PROFILE[ind]
	pro = targeted_username
	try:
#         wait_for_internet_connection()
		print('\n\nGetting followers from',pro)
		filename = 'downloads/'+pro+'.csv'

		profile = instaloader.Profile.from_username(L.context, pro)
		main_followers = profile.followers
		count = 0
		lust = []
		for count,i in enumerate(profile.get_followers()):
			t2 = threading.Thread(target=gon,args=[i,count])
			t2.start()
			lust.append(t2)
		for thread in lust:
			thread.join()
		print(f'account name: {pro}, total followers: {count}')

	except Exception as e:

		ee = str(e).lower()

		if "bad request" in ee:
			df = pd.DataFrame({"username":gen})
			df.to_csv(filename, index=False)
		elif "bad requests" in ee:
			df = pd.DataFrame({"username":gen})
			df.to_csv(filename, index=False)

		elif "400" in ee:
			df = pd.DataFrame({"username":gen})
			df.to_csv(filename, index=False)
		elif "badrequest" in ee:
			df = pd.DataFrame({"username":gen})
			df.to_csv(filename, index=False)

	# TODO: Remove these two lines to remove CSV file handling
	df = pd.DataFrame({"username":gen})
	df.to_csv(filename, index=False)

	return {
		'username':pro,
		'total_followers':count,
		'followers':gen
	}


def get_data(username,password,targeted_username):

	L.login(username,password)
	return test(targeted_username)
