#!/usr/bin/python

import MySQLdb
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#execfile('pandasSql.py')

#Reads csv file into pandas, does preprocessing, and writes to mysql

def readCsv(file):
	#Read in csv
	df = pd.read_csv(file)
	#Convert Strings to Dates
	df['start_time'] = pd.to_datetime(pd.Series(df['start_time']))
	#Get rid of duplicates based off start_time
	df = df.drop_duplicates(cols='start_time', take_last=True)
	#get rid of bad data where total_distance is less than one
	df = df[(df['total_distance'] > 1)]
	#sort dataframe based off start_time
	df = df.sort(['start_time'])
	return df

df = readCsv('/home/mike/GarminDataAgent/garmin_data.csv')
conection = MySQLdb.connect(host="localhost",user="root", passwd="",db="garmin")
df.to_sql(con=conection, name='garminData', if_exists='replace', flavor='mysql')
df.plot(x='start_time', y='total_distance', title='Running Distances', style='s')
plt.show()
