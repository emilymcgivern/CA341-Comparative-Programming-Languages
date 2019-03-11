#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#importing the date and creating a list of those dates. Need to check against list to ensure date entered by user is in the list and is within the week.
import time
import datetime 
from datetime import timedelta
from time import gmtime, strftime
dates = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
base = datetime.date.today()
new_base = base.strftime("%d/%m/%Y")
current_time = datetime.datetime.now()
current_time = current_time.strftime("%H:%M:%S")


print ("Appointment Calendar\n--------------------\nWelcome to your personal appointment calendar!\nPlease follow the instructions below to begin organising your week!\nToday's date is: " + str(new_base) + "\nThe current time is: " + str(current_time) + "\nYou can schedule appointments for a week period starting from today\nYou can schedule appointments between 9am and 9pm\n")
times_list = [['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`']]
#making, deleting or checking appointments
appointments = {}

def choose_option(welcome_message):
	if welcome_message == 1:
		while True:
			print ("Available Dates: ")
			print (', '.join(dates))
			apptDate = input('Enter day from the above list\n')
			if apptDate not in dates:
				print ('Please choose day from the above list!')
				for line in dates:
					print (line)
				continue
			else:
				date_index = dates.index(apptDate)
				break

		while True:
			start_time_list = times_list[date_index]
			if start_time_list == []:
				dates.remove(apptDate)
			print ("Available times: ") 
			print (', '.join(start_time_list))
			apptStartTime = input('Enter start time (hh:mm) from the list of times: \n')
			if apptStartTime not in start_time_list:
				print ('Appointment already scheduled, please choose a start time from the following list: ' )
				continue
			else:
				start_index = start_time_list.index(apptStartTime)
				#start_time_list.remove(apptStartTime)
				break

		while True:
			apptEndTime = raw_input('Enter end time (hh:mm)\n')
			if apptEndTime not in start_time_list:
					print ('Appointment already scheduled, please choose an end time from the following list: ')
					continue
			else:
				end_index = start_time_list.index(apptEndTime)
				start_time_list[start_index:end_index+1] = []
				break

		apptDesc = input('Enter a general description of the appointment:\n')

		#Checking to see if key in dictionary
		newAppt = str(apptStartTime) + ' -> ' + str(apptEndTime) + ' - ' + apptDesc
		appointments[apptDate] = newAppt
		print ("\nAppointment confirmed: You have scheduled an appointment on " + apptDate + " at " + apptStartTime + " to " + apptEndTime + " for " + apptDesc)
		new_appointment = input('\nWould you like to or view add another appointment? y or n\n')
		if new_appointment == 'y':
			return choose_option(welcome_message = int(input('Please type an option: \n To schedule an appointment press 1 \n To delete an appointment press 2 \n To view appointments press 3 \n')))
		else:
			print ("Exiting Appointment Calendar...")
			time.sleep(1) 
			pass


	elif welcome_message == 2:
		for date,details in appointments.items():
			print (date, details)
		to_delete = input('What should we delete? : ').strip() 
		if to_delete in appointments:
			del appointments[to_delete]
    

	elif welcome_message == 3:
		if not appointments:
			new_appointment = input('Appointment calendar is empty!\nWould you like to add another appointment? y or n\n')
			if new_appointment == 'y':
				return choose_option(welcome_message = int(input('Please type an option: \n To schedule an appointment press 1 \n To delete an appointment press 2 \n To view appointments press 3 \n')))
			else:
				print ("Exiting Appointment Calendar...")
				time.sleep(1) 
				pass
		else: 
			choice = int(input("To view all appointments, press 1.\nTo view a certain day, press 2\n"))
			if choice == 1:
				for date,details in appointments.items():
					print (date, details)
					new_appointment = input('Would you like to add or view another appointment? y or n\n')
					if new_appointment == 'y':
						return choose_option(welcome_message = int(input('Please type an option: \n To schedule an appointment press 1 \n To delete an appointment press 2 \n To view appointments press 3 \n')))
					else:
						print ("Exiting Appointment Calendar...")
						time.sleep(1) 
						pass

			else:
				choice2 = input("Please enter a day from the list above\n")
				if choice2 in appointments:
					print (appointments[choice2])
					new_appointment = input('Would you like to add or view another appointment? y or n\n')
					if new_appointment == 'y':
						return choose_option(welcome_message = int(input('Please type an option: \n To schedule an appointment press 1 \n To delete an appointment press 2 \n To view appointments press 3 \n')))
					else:
						print ("Exiting Appointment Calendar...")
						time.sleep(1) 
						pass
					


choose_option(welcome_message = int(input('Please type an option: \n To schedule an appointment press 1 \n To delete an appointment press 2 \n To view appointments press 3 \n')))

