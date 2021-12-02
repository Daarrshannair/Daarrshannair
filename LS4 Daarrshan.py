import dweepy
import random
from time import sleep

light_intensity = 0.0
max_intensity = 60
bulb_status = True # boolean for lampu
statement3 = ("It is dark outside")
statement4 = ("It is bright outside")




# data for light sensor
data_light = [11.5, 95.6, 23.6, 36.4, 80.5, 65.5, 44.2, 23.5, 15.9, 30.5]

def update_iot(intensity, status, statement):
	
	iot_data = {
	#	key		:	Value
	"light_intensity"	:	intensity,
	"bulb_status"	:	status,
	"Unit Statement":	statement,
	}
	
	# publish the data
	dweepy.dweet_for("Kg_Sakai",iot_data)	


while True:
	
	for y in data_light:
		
		light_intensity = y
		
		if light_intensity < max_intensity:
			bulb_status = True
			unit_statement = statement3
			light_status_text = "Lights on"
			
		else:
			bulb_status = False
			unit_statement = statement4
			light_status_text = "Lights off"
			
		print ("Brightness: " + str (light_intensity) + ", " + light_status_text)		
		update_iot(light_intensity, bulb_status, unit_statement)	
