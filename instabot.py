from time import sleep
import os
import sys
import pathlib
from timeit import default_timer as timer
import datetime
import pandas as pd

import time
import threading

import urllib3
import instaloader

# Get instance
L = instaloader.Instaloader()

# Login or load session

log = open("login_info.txt","r").read().split("\n")




L.login(log[0],log[1])

pathlib.Path('downloads/').mkdir(parents=True, exist_ok=True)

http = urllib3.PoolManager()


start = timer()
curr = str(datetime.datetime.now())    

f = open('input.txt','r')
accounts = f.read()
p = accounts.split('\n')


# input()
#print('Resuming from:',p[0])
PROFILE = p[:]
print(PROFILE)
print('Total accounts:',len(PROFILE))

gen = []

def gon(i,count):

	j = str(i).split(" ")
	#print(j[1],count)
	#df = df.append({'username': j[1]}, ignore_index=True)
	#yield j[1]
	print(count,j[1])
	gen.append(j[1])
	#df = df.append({'username': j[1]}, ignore_index=True)





def test(ind):
    pro = PROFILE[ind]
    try:
#         wait_for_internet_connection()
        print('\n\nGetting followers from',pro)
        filename = 'downloads/'+pro+'.csv'
        '''with open(filename,'a',newline='',encoding="utf-8") as csvf:

            csv_writer = csv.writer(csvf)
            csv_writer.writerow(['username'])
        df = pd.read_csv(filename)'''
        
        
        
    
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
        



        '''for g,no in enumerate(gen):
        	print(g,no)
        	df = df.append({'username': no}, ignore_index=True)'''




    except Exception as e:

        print('Skipping',pro,e)





        #print("total followers: ",count )


    df = pd.DataFrame({"username":gen})
    df.to_csv(filename, index=False)   




    
threads = []
for ind in range(len(PROFILE)):
	t1 = threading.Thread(target=test,args=[ind])
	t1.start()

