import time
import datetime 
from datetime import timedelta

class Appointment:
    global appointments
    global times_list
    global days

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    appointments = {}
    times_list = [['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`'],['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00`']]

    def choose_option(self):  
        user_input = int(input('Welcome! Please type an option: \n To schedule an appointment press 1 \n To delete an appointment press 2 \n To view appointments press 3 \n'))
        if user_input == 1:
            print (self.add_appointment(times_list, days))
        elif user_input == 2:
            print (self.delete_appointment(appointments))
        else:
            print(self.view_appointment(appointments))

    def check(self):
        new_appointment = input('\nWould you like to add an appointment? y or n\n')
        if new_appointment == 'y':
            return self.add_appointment(times_list, days)
        elif new_appointment == 'n':
            new_activity = input('Would you like view or edit appointments? y or n\n') 
            if new_activity == 'y':
                return self.choose_option()
            else:
                print ("Exiting Appointment Calendar...")
                time.sleep(1) 
                pass

    def add_appointment(self, times_list, days):
        while True:
            print ("\nAvailable Days: ")
            print (', '.join(days))
            date = input('Enter day from the above list\n')
            if date not in days:
                print ('Please choose day from the above list!')
                for line in days:
                    print (line)
                continue
            else:
                date_index = days.index(date)
                break

        while True:
            start_time_list = times_list[date_index]
            if start_time_list == []:
                days.remove(date)

            print ("Available times: ") 
            print (', '.join(start_time_list))
            start_time = input("Enter start time (hh:mm)\n")
            if start_time not in start_time_list:
                print ('Appointment already scheduled, please choose a start time from the following list: ' )
                continue
            else:
                start_index = start_time_list.index(start_time)
                break

        while True:
            end_time = input('Enter end time (hh:mm)\n')
            if end_time not in start_time_list:
                print ('Appointment already scheduled, please choose an end time from the following list: ' )
                continue
       
            else:
                end_index = start_time_list.index(end_time)
                start_time_list[start_index:end_index+1] = []
                break
                

        desc = input('Enter a general description of the appointment:\n')
        newAppt = '{} to {} - {}'.format(start_time, end_time, desc)
        appointments[date] = newAppt
        print ("\nAppointment confirmed: You have scheduled an appointment on {} at {} to {} for {}".format(date, start_time, end_time, desc))
        return self.check()

    def view_appointment(self, appointments):
        if not appointments:
            print('Appointment calendar is empty!\n')
            return self.check()
        else:
            choice = int(input("To view all appointments, press 1.\nTo view a certain day, press 2\n"))
            if choice == 1:
                for date,details in appointments.items():
                    print (date, details)
                    return self.choose_option()
            else:
                choice2 = input("Please enter a day from the list above\n")
                if choice2 in appointments:
                    print (appointments[choice2])
                    return self.choose_option()
                    

    def delete_appointment(self, appointments):
        for date,details in appointments.items():
            print (date, details)
        to_delete = input('What should we delete? : ')
        if to_delete in appointments:
            del appointments[to_delete]
        print (appointments)

class Date:
    def get_current_time(self):
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M:%S")
        return current_time

    def get_today_date(self):
        base = datetime.date.today()
        new_base = base.strftime("%d/%m/%Y")
        return new_base

def main():
    d = Date()
    print ("Appointment Calendar\n--------------------\nWelcome to your personal appointment calendar!\nPlease follow the instructions below to begin organising your week!\nToday's date is: {} \nThe current time is: {} \nYou can schedule appointments for a week period starting from today\nYou can schedule appointments between 9am and 9pm\n".format(d.get_today_date(), d.get_current_time()))
    a1 = Appointment()
    a1.choose_option()

if __name__ == "__main__":
    main()
