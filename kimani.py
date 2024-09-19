from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.textfield import MDTextField
from kivy.graphics import Color, Line
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.clock import Clock
from mysql.connector import Error
#from chatterbot import ChatBot
import time
#from chatterbot.trainers import ChatterBotCorpusTrainer
import pytz
import yaml
import collections.abc
collections.Hashable = collections.abc.Hashable
time.clock = time.time
import os
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition,SlideTransition
from kivymd.theming import  ThemableBehavior
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.dropdown import DropDown
from kivy.config import  Config
Config.set('graphics', 'width','550')
Config.set('graphics', 'width','550')
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.list import  OneLineListItem,MDList
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.graphics.texture import Texture
import io
from kivymd.uix.card import MDCard
from kivymd.uix.snackbar import Snackbar
import matplotlib.pyplot as plt
import random
from kivymd.uix.card import MDCard
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.popup import Popup
from kivy.graphics.texture import Texture
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDRaisedButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.filechooser import FileChooserIconView
import time
from io import BytesIO
from kivymd.uix.menu import MDDropdownMenu
import string
from kivy.lang import Builder
from kivymd.uix.bottomnavigation import MDBottomNavigation,MDBottomNavigationItem
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.utils import rgba
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDTextButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.uix.image import Image
from kivy.graphics import Ellipse, Color
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.pickers import MDDatePicker
import mysql.connector
from kivy.uix.togglebutton import ToggleButton
import hashlib
import requests
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.metrics import dp
from kivy.uix.textinput import TextInput
from datetime import datetime,timedelta
from kivy.properties import ObjectProperty
import io
import matplotlib.pyplot as plt
from kivy.network.urlrequest import UrlRequest
import json








class SettingsScreen(Screen):
   pass
class WindowManager(ScreenManager):
    
    pass

class Lof(Screen):
    pass
class KimaniSitemanagerReportOption(Screen):
    def send_report(self, recipient):
        # Logic to send the report to the specified recipient
        # You might use email or other services
        toast(text=f"Report sent to {recipient}")
    
    def download_report(self):
        # Logic to download the report as a document
        # Implement code to generate and save the report as a file
        toast(text="Report downloaded successfully")


    
class KimaniSiteManagerReport(Screen):
    pass
class KimaniDrillingReport(Screen):
    pass

class KimaniDayShiftDrillingReport(Screen):
    
    def create_dayshiftreport(self, location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver, Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintenance_equipment_used, Maintainance_performed, Safety_and_observation, user_id=None):
        if user_id is None:
           toast("User ID is missing")
           return
    # rest of the method

        try:
            if not all([location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver, Store_keeper, Weather]):
                toast("Please fill in all required fields")
                return

            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Replace with your database password
                database="kimani_drilling"
            )
            mycursor = mydb.cursor()

            # SQL query to insert drilling report
            sql = """
            INSERT INTO drilling_reports 
            (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver, Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintenance_equipment_used, Maintainance_performed, Safety_and_observation, user_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            val = (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver, Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintenance_equipment_used, Maintainance_performed, Safety_and_observation, user_id)

            # Debugging: print the query and values to verify
            print(f"SQL Query: {sql}")
            print(f"Values: {val}")

            # Execute the query
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()

            # Display success message
            toast("Report created successfully")

            # Navigate to the options screen
            self.manager.current = 'kimanireportoptions'

        except mysql.connector.Error as err:
            # Corrected error handling with a formatted string
            toast(f"Database connection error: {err}")

    def on_date_select(self, instance, value, date_range):
        formatted_date = value.strftime('%Y-%m-%d')  # Format the date
        self.manager.get_screen('kimanidayshiftdrillingreport').ids.Date_input.text = str(formatted_date)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()


class KimaniNightShiftDrillingReport(Screen):
    
    def create_nightshiftreport(self, location,Date,Drilling_rig,Driller,Assistance_driller,Mechanics,Driver,Store_keeper,Weather,Safety_meeting_time,Safety_meeting_topic_covered,Drilling_progress_start_time,Drilling_progress_end_time,Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle,Total_core_covered, Drilling_bit_type,Drilling_fluid_used,Maintainance_equipment_used,Maintainance_performed,Safety_and_observation):
      try:
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your database password
            database="kimani_drilling"
        )
        mycursor = mydb.cursor()
        sql = """
            INSERT INTO drilling_reports (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver,Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintainance_equipment_used, Maintainance_performed, Safety_and_observation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver,Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintainance_equipment_used, Maintainance_performed, Safety_and_observation)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        
        # Display success message
        toast(text="Report created successfully")

        # Navigate to the options screen
        self.manager.current = 'kimanireportoptions'
        
      except mysql.connector.Error as err:
        toast("Database connection error:", err)
        
        
    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('kimanidayshiftdrillingreport').ids.Date_input.text = str(value)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

#class ChatBotService:
    #def __init__(self):
        #self.chatbot = ChatBot('MyBot')
       # self.trainer = ChatterBotCorpusTrainer(self.chatbot)
       # self.trainer.train('chatterbot.corpus.english')  # Train with English corpus
        
    #def some_method(self):
        #3start_time = time.perf_counter()  # Use time.perf_counter() instead of time.clock()
        # Rest of your code

        
    #def get_response(self, message):
        #return str(self.chatbot.get_response(message))
    
class KimaniReportOptions(Screen):
    
    def send_report(self, recipient):
        # Logic to send the report to the specified recipient
        # You might use email or other services
        toast(f"Report sent to {recipient}").show()
    
    def download_report(self):
        # Logic to download the report as a document
        # Implement code to generate and save the report as a file
        toast("Report downloaded successfully")


class WebView(Widget):
    pass

class DeviceManagerScreen(BoxLayout):
    webview = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DeviceManagerScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.load_map, 1)

    def load_map(self, dt):
        self.webview.load_url('https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=latitude,longitude')

    def fetch_gps_data(self):
        # Replace with actual endpoint URL to fetch GPS data from your backend
        endpoint = "https://api.example.com/gps_data"
        headers = {
            'Authorization': 'Bearer YOUR_API_TOKEN'  # If authentication is required
        }

        try:
            response = requests.get(endpoint, headers=headers)
            if response.status_code == 200:
                gps_data = response.json()  # Assuming data is in JSON format
                return gps_data
            else:
                print(f"Error fetching GPS data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching GPS data: {e}")
            return None

    def update_map_markers(self, dt):
        gps_data = self.fetch_gps_data()
        if gps_data:
            # Assuming gps_data is a list of dictionaries with 'latitude' and 'longitude' keys
            locations = ','.join([f"{item['latitude']},{item['longitude']}" for item in gps_data])
            self.webview.load_url(f'https://www.google.com/maps/embed/v1/directions?key=YOUR_API_KEY&origin=place_id:{locations}&destination=place_id:{locations}')


class GenderRadioButton(BoxLayout):
    icon = StringProperty()
    selected = BooleanProperty(False)

    def __init__(self, icon='', **kwargs):
        super(GenderRadioButton, self).__init__(**kwargs)
        self.icon = icon
        self.orientation = 'horizontal'
        self.spacing = dp(10)

        icon_image = Image(source=self.icon, size_hint=(None, 1), width=dp(24))
        self.add_widget(icon_image)

        label_text = self.icon.split('.')[0].capitalize()  # 'male.png' -> 'Male'
        label = Label(text=label_text)
        self.add_widget(label)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.deselect_all()  # Deselect all other buttons
            self.selected = True  # Select this button
        return super().on_touch_down(touch)

    def on_selected(self, instance, value):
        if value:
            self.group_selected()

    def group_selected(self):
        for child in self.parent.children:
            if isinstance(child, GenderRadioButton) and child != self:
                child.selected = False

class ContactUs(Screen):
    pass

class KimaniStoreReports(Screen):
    pass
class SiteManagerDrillingReport(Screen):
    pass


class DayShiftDrillingReport(Screen):
    def create_dayshiftreport(self, location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver, Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintainance_equipment_used, Maintainance_performed, Safety_and_observation, user_id):

      if not user_id:
        toast("User ID is missing or invalid")
        return

      try:
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your database password
            database="kimani_drilling"
        )
        mycursor = mydb.cursor()

        # SQL query to insert drilling report
        sql = """
        INSERT INTO drilling_reports 
        (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver, Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintainance_equipment_used, Maintainance_performed, Safety_and_observation, user_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Values to be inserted into the database
        val = (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver, Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintainance_equipment_used, Maintainance_performed, Safety_and_observation, user_id)
        
        # Execute the query and commit the changes
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        # Display success message
        toast("Report created successfully")

        # Navigate to the options screen
        self.manager.current = 'kimanireportoptions'

      except mysql.connector.Error as err:
        # Display error message in case of a database connection error
        toast(f"Database connection error: {str(err)}")

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('kimanidayshiftdrillingreport').ids.Date_input.text = str(value)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()
   
class NightShiftDrillingReport(Screen):
    def create_nightshiftreport(self, location,Date,Drilling_rig,Driller,Assistance_driller,Mechanics,Driver,Store_keeper,Weather,Safety_meeting_time,Safety_meeting_topic_covered,Drilling_progress_start_time,Drilling_progress_end_time,Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle,Total_core_covered, Drilling_bit_type,Drilling_fluid_used,Maintainance_equipment_used,Maintainance_performed,Safety_and_observation,user_id):
      try:
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your database password
            database="kimani_drilling"
        )
        mycursor = mydb.cursor()
        sql = """
            INSERT INTO drilling_reports (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver,Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintainance_equipment_used, Maintainance_performed, Safety_and_observation,user_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (location, Date, Drilling_rig, Driller, Assistance_driller, Mechanics, Driver,Store_keeper, Weather, Safety_meeting_time, Safety_meeting_topic_covered, Drilling_progress_start_time, Drilling_progress_end_time, Drilling_total_hours_worked, Depth_started, Depth_ended, Total_meter_drilled, Hole_id, Drilling_angle, Total_core_covered, Drilling_bit_type, Drilling_fluid_used, Maintainance_equipment_used, Maintainance_performed, Safety_and_observation,user_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        
        # Display success message
        toast("Report created successfully")

        # Navigate to the options screen
        self.manager.current = 'kimanireportoptions'
        
      except mysql.connector.Error as err:
        toast("Database connection error:", err)
        
        
    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('kimanidayshiftdrillingreport').ids.Date_input.text = str(value)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

#class ChatBotService:
    #def __init__(self):
        #self.chatbot = ChatBot('MyBot')
       # self.trainer = ChatterBotCorpusTrainer(self.chatbot)
       # self.trainer.train('chatterbot.corpus.english')  # Train with English corpus
        
    #def some_method(self):
        #3start_time = time.perf_counter()  # Use time.perf_counter() instead of time.clock()
        # Rest of your code

        
    #def get_response(self, message):
        #return str(self.chatbot.get_response(message))
    
    

class Password_reset(Screen):
    def reset_password(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authentication WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authentication WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authentication SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'log_in'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
            

class Password_resetAdmin(Screen):
    def resetpasswordAdmin(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationadmin WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationadmin WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authenticationadmin SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'log_in'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)

    
                        
            


class Forgot(Screen):
   
    def reset_password(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authentication WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authentication WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authentication SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'password_reset'

        except mysql.connector.Error as err:
            print("Database connection error:", err)


class ForgotKimaniMechanics(Screen):
       
    def reset_passwordkimanimechanics(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_mechanics"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationmechanics WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationmechanics WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authenticationmechanics SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetkimanimechanics'

        except mysql.connector.Error as err:
            print("Database connection error:", err)


class PasswordResetKimaniMechanics(Screen):
    def reset_passwordkimanimechanics(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani_mechanics"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationmechanics WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationmechanics WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authenticationmechanics SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'loginkimanimechanics'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
            
class ForgotKimaniFinance(Screen):
       
    def reset_passwordkimanifinance(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_finance"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationfinance WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationfinance WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authenticationfinance SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetkimanifinance'

        except mysql.connector.Error as err:
            print("Database connection error:", err)
            
class PasswordResetKimaniFinance(Screen):
    def reset_passwordkimanifinance(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani_finance"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationfinance WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationfinance WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authenticationfinance SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'loginkimanifinance'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
            



            

class ForgotOtherKimaniWorkers(Screen):
       
    def reset_passwordotherkimaniworkers(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_other_employee"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authentication_other_employee WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authentication_other_employee WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authentication_other_emloyee SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetotherkimaniworkers'

        except mysql.connector.Error as err:
            print("Database connection error:", err)
            
class PasswordResetOtherKimaniWorkers(Screen):
    def reset_passwordotherkimaniworkers(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani_other_employee"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authentication_other_employee WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authentication_other_employee WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authentication_other_employee SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'loginotherkimaniworkers'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
            



class ForgotKimaniSiteManagers(Screen):
       
    def reset_passwordkimanisitemanagers(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_site_managers"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationsitemanager WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationsitemanager WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authenticationsitemanager SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetkimanisitemanagers'

        except mysql.connector.Error as err:
            print("Database connection error:", err)
            

class PasswordResetKimaniSiteManagers(Screen):
    def reset_passwordkimanisitemanagers(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani_site_managers"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationsitemanagers WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationsitemanagers WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authenticationsitemanagers SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'loginkimanisitemanagers'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
            






class ForgotKimaniTransport(Screen):
       
    def reset_passwordkimanitransport(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_transport"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationtransport WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationtransport WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authenticationtransport SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetkimanitransport'

        except mysql.connector.Error as err:
            print("Database connection error:", err)

class PasswordResetKimaniTransport(Screen):
    def reset_passwordkimanitransport(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani_transport"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationtransport WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationtransport WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authenticationtransport SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'loginkimanitransport'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
            



            
class ForgotKimaniDrilling(Screen):
       
    def reset_passwordkimanidrilling(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_drilling"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationdrilling WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationdrilling WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authenticationdrilling SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetkimanidrilling'

        except mysql.connector.Error as err:
            print("Database connection error:", err)
            


class PasswordResetKimaniDrilling(Screen):
    def reset_passwordkimanidrilling(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani_drilling"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationdrilling WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationdrilling WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authenticationdrilling SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'loginkimanidrilling'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
            







class ForgotKimaniStores(Screen):
       
    def reset_passwordkimanistore(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_stores"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationstores WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationstores WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authenticationstores SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetkimanistores'

        except mysql.connector.Error as err:
            print("Database connection error:", err)
  
class PasswordResetKimaniStores(Screen):
    def reset_passwordkimanistore(self, username_or_email, new_password, confirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  
                database="kimani_stores"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationstores WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationstores WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return

            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Ensure both password fields are filled and match
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Update the database with the new password
            sql_update_password = "UPDATE authenticationstores SET password = %s WHERE Login_id = %s"
            mycursor.execute(sql_update_password, (new_password, Login_id))
            mydb.commit()

            print("Password updated successfully!")
            self.manager.current = 'loginkimanistores'  # Redirect to login screen after password reset

        except mysql.connector.Error as err:
            print("Database update error:", err)
              




                 


class CircleImage(FloatLayout):
    source = StringProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = Image(source=self.source, size=self.size, pos=self.pos)
        self.add_widget(self.image)

        with self.canvas:
            Color(1, 1, 1, 1)  # White color
            self._ellipse = Ellipse(size=self.size, pos=self.pos)
        
        self.bind(pos=self.update_ellipse, size=self.update_ellipse)

    def update_ellipse(self, *args):
        self._ellipse.pos = self.pos
        self._ellipse.size = self.size

    def on_upload(self):
        file_chooser = FileChooserIconView()
        file_chooser.bind(on_submit=self.load_image)
        popup = Popup(title="Choose an image", content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

    def load_image(self, chooser, path, filename):
        self.source = filename[0]
        print(f"Selected image: {self.source}")
        self.image.source = self.source  # Update the Image widget with the selected image

        # You can add further logic here to process the chosen image
        # For example, resizing or saving the image, etc.
class ForgotAdmin(Screen):
       
    def resetpasswordAdmin(self, username_or_email):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani"
            )
            mycursor = mydb.cursor()

            # Check if the entered value is username or email
            if '@' in username_or_email:
                # It's an email
                sql_check_user = "SELECT Login_id, username, email FROM authenticationadmin WHERE email = %s"
                user_type = 'email'
            else:
                # It's a username
                sql_check_user = "SELECT Login_id, username, email FROM authenticationadmin WHERE username = %s"
                user_type = 'username'

            mycursor.execute(sql_check_user, (username_or_email,))
            user = mycursor.fetchone()

            if not user:
                print(f"No user found with {user_type}: {username_or_email}")
                return
            
            # Extract the primary key (Login_id)
            Login_id = user[0]

            # Generate a random token for password reset (you can modify the length as needed)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Update the database with the generated token and expiry time (e.g., 1 hour from now)
            sql_update_token = "UPDATE authenticationadmin SET reset_token = %s, token_expiry = DATE_ADD(NOW(), INTERVAL 1 HOUR) WHERE Login_id = %s"
            mycursor.execute(sql_update_token, (token, Login_id))
            mydb.commit()

            # Now you would typically send an email or SMS with the token to the user
            # For simplicity, print the token here (replace with email/SMS sending code)
            print(f"Password reset token generated: {token}")

            # Redirect to the password reset screen where the user can enter the token and set a new password
            # You can set self.manager.current = 'password_reset' to navigate to the password reset screen
            # Example: self.manager.current = 'password_reset'
            self.manager.current = 'passwordresetAdmin'

        except mysql.connector.Error as err:
            print("Database connection error:", err)



class Chat(Screen):
    chat_history_list = ObjectProperty(None)

    def message(self, message):
        # Example function to send a message
        if message.strip():  # Ensure message isn't empty
            new_message = OneLineListItem(text=message)
            self.chat_history_list.add_widget(new_message)
            # Here you would typically send the message via backend or update database

    def load_chat_history(self, chat_history):
        # Example function to load chat history
        self.chat_history_list.clear_widgets()
        for message in chat_history:
            self.chat_history_list.add_widget(OneLineListItem(text=message))
    def fetch_gps_data():
        # Replace with actual endpoint URL to fetch GPS data
        endpoint = "https://api.example.com/gps_data"
        headers = {
            'Authorization': 'Bearer YOUR_API_TOKEN'  # If authentication is required
        }

        try:
            response = requests.get(endpoint, headers=headers)
            if response.status_code == 200:
                gps_data = response.json()  # Assuming data is in JSON format
                return gps_data
            else:
                print(f"Error fetching GPS data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching GPS data: {e}")
            return None

    gps_data = fetch_gps_data()        


            


class CircleImage(FloatLayout):
    source = StringProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = Image(source=self.source, size=self.size, pos=self.pos)
        self.add_widget(self.image)

        with self.canvas:
            Color(1, 1, 1, 1)  # White color
            self._ellipse = Ellipse(size=self.size, pos=self.pos)
        
        self.bind(pos=self.update_ellipse, size=self.update_ellipse)

    def update_ellipse(self, *args):
        self._ellipse.pos = self.pos
        self._ellipse.size = self.size

    def on_upload(self):
        file_chooser = FileChooserIconView()
        file_chooser.bind(on_submit=self.load_image)
        popup = Popup(title="Choose an image", content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

    def load_image(self, chooser, path, filename):
        self.source = filename[0]
        print(f"Selected image: {self.source}")
        self.image.source = self.source  # Update the Image widget with the selected image
        
class UserpageKimaniTransport(Screen):
   #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    user_details = {}  # Placeholder for receiving user_details

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_details = {}  # Initialize user_details as an empty dictionary

    def update_profile(self, user_details):
        if user_details:
            self.ids.full_name_label.text = str(user_details.get('full_name', ''))
            self.ids.full_name_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.email_label.text = str(user_details.get('email', ''))
            self.ids.email_label.color = (0, 0, 0, 1)  # Set text color to black
            
            self.ids.gender_label.text = str(user_details.get('gender', ''))
            self.ids.gender_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.phone_label.text = str(user_details.get('phone', ''))
            self.ids.phone_label.color = (0, 0, 0, 1)  # Set text color to black
        else:
            print("User details not found.")


    def reset_profile(self):
        self.ids.full_name_label.text = ''
        self.ids.gender_label.text = ''
        self.ids.email_label.text = ''
        self.ids.phone_label.text = ''
        self.user_details = {}  # Clear stored user_details

    def on_pre_enter(self, *args):
        # Implement this method to handle data passed from Signup screen
        if self.user_details:
            self.update_profile(self.user_details)
            self.user_details = {}  # Reset user_details after handling

    def on_upload(self):
        # Function to handle profile picture upload
        # You can implement the logic for uploading profile picture here
        pass
    
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"

class UserpageKimaniStores(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    user_details = {}  # Placeholder for receiving user_details

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_details = {}  # Initialize user_details as an empty dictionary

    def update_profile(self, user_details):
        if user_details:
            self.ids.full_name_label.text = str(user_details.get('full_name', ''))
            self.ids.full_name_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.email_label.text = str(user_details.get('email', ''))
            self.ids.email_label.color = (0, 0, 0, 1)  # Set text color to black
            
            self.ids.gender_label.text = str(user_details.get('gender', ''))
            self.ids.gender_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.phone_label.text = str(user_details.get('phone', ''))
            self.ids.phone_label.color = (0, 0, 0, 1)  # Set text color to black
        else:
            print("User details not found.")


    def reset_profile(self):
        self.ids.full_name_label.text = ''
        self.ids.gender_label.text = ''
        self.ids.email_label.text = ''
        self.ids.phone_label.text = ''
        self.user_details = {}  # Clear stored user_details

    def on_pre_enter(self, *args):
        # Implement this method to handle data passed from Signup screen
        if self.user_details:
            self.update_profile(self.user_details)
            self.user_details = {}  # Reset user_details after handling

    def on_upload(self):
        # Function to handle profile picture upload
        # You can implement the logic for uploading profile picture here
        pass
    
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
        
class UserpageKimaniDrilling(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    user_details = {}  # Placeholder for receiving user_details

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_details = {}  # Initialize user_details as an empty dictionary

    def update_profile(self, user_details):
        if user_details:
            self.ids.full_name_label.text = str(user_details.get('full_name', ''))
            self.ids.full_name_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.email_label.text = str(user_details.get('email', ''))
            self.ids.email_label.color = (0, 0, 0, 1)  # Set text color to black
            
            self.ids.gender_label.text = str(user_details.get('gender', ''))
            self.ids.gender_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.phone_label.text = str(user_details.get('phone', ''))
            self.ids.phone_label.color = (0, 0, 0, 1)  # Set text color to black
        else:
            print("User details not found.")


    def reset_profile(self):
        self.ids.full_name_label.text = ''
        self.ids.gender_label.text = ''
        self.ids.email_label.text = ''
        self.ids.phone_label.text = ''
        self.user_details = {}  # Clear stored user_details

    def on_pre_enter(self, *args):
        # Implement this method to handle data passed from Signup screen
        if self.user_details:
            self.update_profile(self.user_details)
            self.user_details = {}  # Reset user_details after handling

    def on_upload(self):
        # Function to handle profile picture upload
        # You can implement the logic for uploading profile picture here
        pass
    
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"

class UserpageKimaniSiteManagers(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    user_details = {}  # Placeholder for receiving user_details

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_details = {}  # Initialize user_details as an empty dictionary

    def update_profile(self, user_details):
        if user_details:
            self.ids.full_name_label.text = str(user_details.get('full_name', ''))
            self.ids.full_name_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.email_label.text = str(user_details.get('email', ''))
            self.ids.email_label.color = (0, 0, 0, 1)  # Set text color to black
            
            self.ids.gender_label.text = str(user_details.get('gender', ''))
            self.ids.gender_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.phone_label.text = str(user_details.get('phone', ''))
            self.ids.phone_label.color = (0, 0, 0, 1)  # Set text color to black
        else:
            print("User details not found.")



    def reset_profile(self):
        self.ids.full_name_label.text = ''
        self.ids.gender_label.text = ''
        self.ids.email_label.text = ''
        self.ids.phone_label.text = ''
        self.user_details = {}  # Clear stored user_details

    def on_pre_enter(self, *args):
        # Implement this method to handle data passed from Signup screen
        if self.user_details:
            self.update_profile(self.user_details)
            self.user_details = {}  # Reset user_details after handling

    def on_upload(self):
        # Function to handle profile picture upload
        # You can implement the logic for uploading profile picture here
        pass
    
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
class UserpageKimaniMechanics(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    user_details = {}  # Placeholder for receiving user_details

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_details = {}  # Initialize user_details as an empty dictionary

    def update_profile(self, user_details):
        if user_details:
            self.ids.full_name_label.text = str(user_details.get('full_name', ''))
            self.ids.full_name_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.email_label.text = str(user_details.get('email', ''))
            self.ids.email_label.color = (0, 0, 0, 1)  # Set text color to black
            
            self.ids.gender_label.text = str(user_details.get('gender', ''))
            self.ids.gender_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.phone_label.text = str(user_details.get('phone', ''))
            self.ids.phone_label.color = (0, 0, 0, 1)  # Set text color to black
        else:
            print("User details not found.")



    def reset_profile(self):
        self.ids.full_name_label.text = ''
        self.ids.gender_label.text = ''
        self.ids.email_label.text = ''
        self.ids.phone_label.text = ''
        self.user_details = {}  # Clear stored user_details

    def on_pre_enter(self, *args):
        # Implement this method to handle data passed from Signup screen
        if self.user_details:
            self.update_profile(self.user_details)
            self.user_details = {}  # Reset user_details after handling

    def on_upload(self):
        # Function to handle profile picture upload
        # You can implement the logic for uploading profile picture here
        pass
    
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
        
        
class UserpageOtherKimaniWorkers(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    user_details = {}  # Placeholder for receiving user_details

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_details = {}  # Initialize user_details as an empty dictionary

    def update_profile(self, user_details):
        if user_details:
            self.ids.full_name_label.text = str(user_details.get('full_name', ''))
            self.ids.full_name_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.email_label.text = str(user_details.get('email', ''))
            self.ids.email_label.color = (0, 0, 0, 1)  # Set text color to black
            
            self.ids.gender_label.text = str(user_details.get('gender', ''))
            self.ids.gender_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.phone_label.text = str(user_details.get('phone', ''))
            self.ids.phone_label.color = (0, 0, 0, 1)  # Set text color to black
        else:
            print("User details not found.")



    def reset_profile(self):
        self.ids.full_name_label.text = ''
        self.ids.gender_label.text = ''
        self.ids.email_label.text = ''
        self.ids.phone_label.text = ''
        self.user_details = {}  # Clear stored user_details

    def on_pre_enter(self, *args):
        # Implement this method to handle data passed from Signup screen
        if self.user_details:
            self.update_profile(self.user_details)
            self.user_details = {}  # Reset user_details after handling

    def on_upload(self):
        # Function to handle profile picture upload
        # You can implement the logic for uploading profile picture here
        pass
    
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
class UserpageKimaniFinance(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    user_details = {}  # Placeholder for receiving user_details

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_details = {}  # Initialize user_details as an empty dictionary

    def update_profile(self, user_details):
        if user_details:
            self.ids.full_name_label.text = str(user_details.get('full_name', ''))
            self.ids.full_name_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.email_label.text = str(user_details.get('email', ''))
            self.ids.email_label.color = (0, 0, 0, 1)  # Set text color to black
            
            self.ids.gender_label.text = str(user_details.get('gender', ''))
            self.ids.gender_label.color = (0, 0, 0, 1)  # Set text color to black

            self.ids.phone_label.text = str(user_details.get('phone', ''))
            self.ids.phone_label.color = (0, 0, 0, 1)  # Set text color to black
        else:
            print("User details not found.")


    def reset_profile(self):
        self.ids.full_name_label.text = ''
        self.ids.gender_label.text = ''
        self.ids.email_label.text = ''
        self.ids.phone_label.text = ''
        self.user_details = {}  # Clear stored user_details

    def on_pre_enter(self, *args):
        # Implement this method to handle data passed from Signup screen
        if self.user_details:
            self.update_profile(self.user_details)
            self.user_details = {}  # Reset user_details after handling

    def on_upload(self):
        # Function to handle profile picture upload
        # You can implement the logic for uploading profile picture here
        pass
    
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
        



class SplashScreen(Screen):
    
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        
        # Create a BoxLayout to hold the image
        layout = BoxLayout(orientation='vertical')
        
        # Add an Image widget to the layout
        self.image = Image(source='kimani.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.image)
        
        # Set the initial opacity of the image to 0 (invisible)
        self.image.opacity = 0
        
        # Add the layout to the screen
        self.add_widget(layout)

    def on_enter(self):
        # Start the fade-in animation
        self.fade_in_image()

        # Schedule transition to the home screen after a delay
        Clock.schedule_once(self.switch_to_home, 48)  # 7 seconds splash screen

    def fade_in_image(self):
        # Create a fade-in animation for the image
        animation = Animation(opacity=1, duration=60)  # 2 seconds fade-in
        animation.start(self.image)

    def switch_to_home(self, dt):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'home'

class Home(Screen):
    #chatbot_service = ChatBotService()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_folder = 'image'  # Folder containing your images
        self.images = sorted([os.path.join(self.image_folder, f) for f in os.listdir(self.image_folder)])
        self.current_image = 0
        self.num_images = len(self.images)
        self.start_slideshow()

    def start_slideshow(self):
        Clock.schedule_interval(self.rotate_image, 3)  # Rotate image every 3 seconds

    def rotate_image(self, dt):
        self.ids.image.source = self.images[self.current_image]
        self.current_image = (self.current_image + 1) % self.num_images
        
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"

    
    
   
    


    


class SignupKimaniTransport(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userkimanitransport(self, username,full_name,age ,gender, phone,email, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_transport"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationtransport WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
             

                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationtransport WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
               

                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationtransport WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
                
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
                
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
                
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationtransport (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpagekimanitransport').update_profile(user_details)
            self.manager.current = 'loginkimanitransport'
            toast("User created successfully!")
           


        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
            
   
    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimanitransport').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)

  
class SignupKimaniStores(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userkimanistore(self, username,full_name,age ,gender, phone,email, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_stores"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationstores WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
                
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationstores WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
                
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationstores WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
                
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
              
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
               
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationstores (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpagekimanistores').update_profile(user_details)
            self.manager.current = 'loginkimanistores'
            toast("User created successfully!")
         

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationstores WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'bio': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimanistores').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)
        

     
class SignupKimaniProcurement(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userkimaniprocurement(self, username,full_name,age ,gender, phone,email, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_stores"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationprocurement WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
               
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationprocurement WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
              
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationprocurement WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
              
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
         
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
                
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationprocurement (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpagekimaniprocurement').update_profile(user_details)
            self.manager.current = 'loginkimaniprocurement'
            toast("User created successfully!")
           

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
           
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationprocurement WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'bio': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimaniprocurement').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)
        




 
class SignupKimaniDrilling(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userkimanidrilling(self, username, full_name, age, gender, phone, email, password, comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_drilling"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationdrilling WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
               
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationdrilling WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
              
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationdrilling WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
       
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
                
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
              

                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationdrilling (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpagekimanidrilling').update_profile(user_details)
            self.manager.current = 'loginkimanidrilling'
            toast("User created successfully!")
   

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationdrilling WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'bio': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None
    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimanidrilling').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)
        


        
class SignupKimaniSiteManagers(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userkimanisitemanagers(self, username,full_name,age ,gender, phone,email, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_site_managers"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationsitemanager WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
                
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationsitemanager WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
              
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationsitemanager WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
               
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
                
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
                
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationsitemanager (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpagekimanisitemanagers').update_profile(user_details)
            self.manager.current = 'loginkimanisitemanagers'
            toast("User created successfully!")
         

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
           
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationsitemanager WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'gender': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimanisitemanagers').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)
        
class SignupKimaniMechanics(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userkimanimechanics(self, username,full_name,age ,gender, phone,email, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_mechanics"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationmechanics WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
            
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationmechanics WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
        
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationmechanics WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
                
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
                
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
                
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationmechanics (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpagekimanimechanics').update_profile(user_details)
            self.manager.current = 'loginkimanimechanics'
            toast("User created successfully!")
           

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
         
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authentication WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'bio': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimanimechanics').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)
        
class SignupOtherKimaniWorkers(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userotherkimaniworkers(self, username,full_name,age ,gender, phone,email, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_other_employee"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authentication_other_employee WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
                
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authentication_other_employee WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
                
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authentication_other_employee WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
                
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
                
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
              
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authentication_other_employee (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpageotherkimaniworkers').update_profile(user_details)
            self.manager.current = 'loginotherkimaniworkers'
            toast("User created successfully!")
        

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
        
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authentication WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'bio': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimaniotherworkers').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)
        
class SignupKimaniFinance(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userkimanifinance(self, username,full_name,age ,gender, phone,email, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_finance"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationfinance WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
                
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationfinance WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
             
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationfinance WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
               
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
              
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
                
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            

            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationfinance (username,full_name,age ,gender, phone,email, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s)"
            val = (username,full_name, age , gender, phone,email, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpagekimanifinance').update_profile(user_details)
            self.manager.current = 'loginkimanifinance'
            toast("User created successfully!")
            

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationfinance WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'bio': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupkimanifinance').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()

    def on_date_select(self, instance, value, date_range):
        self.ids.Date_input.text = str(value)
        

     
class SignupAdmin(Screen):
    birth_date = None  # Define birth_date as an instance variable

    def create_userAdmin(self, username,full_name,age ,gender, phone,email,rank, password,comfirm_password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                
                database="kimani_admin"
            )
            mycursor = mydb.cursor()
            sql_check_username = "SELECT * FROM authenticationadmin WHERE username = %s"
            mycursor.execute(sql_check_username, (username,))
            existing_user = mycursor.fetchone()
            if existing_user:
                toast("Username already exists!")
                
                return

            # Check if email already exists
            sql_check_email = "SELECT * FROM authenticationadmin WHERE email = %s"
            mycursor.execute(sql_check_email, (email,))
            existing_email = mycursor.fetchone()
            if existing_email:
                toast("Email already exists!")
              
                return

            # Check if phone number already exists
            sql_check_phone = "SELECT * FROM authenticationadmin WHERE phone = %s"
            mycursor.execute(sql_check_phone, (phone,))
            existing_phone = mycursor.fetchone()
            if existing_phone:
                toast("Phone number already exists!")
                
                return

            if password != comfirm_password:
                toast("Passwords don't match!")
                
                # You can display an error message to the user
                # For example, update a Label's text property with the error message
                return   
            if not (username and password and email and phone):  # Ensure all fields are filled
                toast("Please fill in all fields!")
 
                return

            # Example: Validate email format (you can use regex for more robust validation)
            #if not email.endswith("@example.com"):
               # print("Invalid email format!")
               # return
            
            
 
            # Execute SQL query to insert a new user into the database
            sql = "INSERT INTO authenticationadmin (username,full_name,age ,gender, phone,email,rank, password,comfirm_password) VALUES (%s, %s,%s, %s, %s,%s, %s,%s,%s)"
            val = (username,full_name, age , gender, phone,email,rank, password, comfirm_password)
            mycursor.execute(sql, val)
            mydb.commit()
            
            
            # Initialize user progress in the user_progress table
            user_id = mycursor.lastrowid  # Get the last inserted user_id
            sql_initialize_progress = "INSERT INTO user_progress (user_id) VALUES (%s)"
            mycursor.execute(sql_initialize_progress, (user_id,))
            mydb.commit()
             # Get the user details after successful insertion
            app = MDApp.get_running_app()
            user_details = {
                'user_id': user_id,
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'gender': 'gender',  # Assuming 'bio' field exists in your table
            }
            app.user_details = user_details

            # Navigate to Userpage and pass user_details
            app.root.get_screen('userpageAdmin').update_profile(user_details)
            self.manager.current = 'log_in'
            toast("User created successfully!")
        
            

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
            
    def fetch_user_details(self, cursor, user_id):
        # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authentication WHERE user_id = %s"
        cursor.execute(sql_fetch_user, (user_id,))
        user_details = cursor.fetchone()

        # Format user_details as a dictionary
        if user_details:
            user_details_dict = {
                'user_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'age': user_details[3],
                'email': user_details[4],
                'phone': user_details[5],
                'bio': user_details[6]  # Assuming 'bio' is a column in your table
                # Add more fields as needed
            }
            return user_details_dict
        else:
            return None

    def on_date_select(self, instance, value, date_range):
        self.manager.get_screen('signupAdmin').ids.Date_input.text = str(value)

    def get_selected_gender(self):
        if self.ids.male_checkbox.active:
            return "Male"
        elif self.ids.female_checkbox.active:
            return "Female"
        else:
            return ""

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_select)
        date_dialog.open()




class LogInKimaniStore(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticate_user(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_stores"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authenticationstores WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                toast("Login successful!")
                
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpagekimanistores').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpagekimanistores'

            else:
                toast("Invalid username or password in kimani")
                
        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
        
class LogInKimaniTransport(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticate_user(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_transport"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authenticationtransport WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                print("Login successful!")
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpagekimanitransport').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpagekimanitransport'

            else:
                toast("Invalid username or password in kimani")
             

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
class LogInKimaniDrilling(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticate_user(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_drilling"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authenticationdrilling WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                toast("Login successful!")
                
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpagekimanidrilling').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpagekimanidrilling'

            else:
                toast("Invalid username or password in kimani")
               

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
        
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
class LogInKimaniFinance(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticate_user(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_finance"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authenticationfinance WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                toast("Login successful!")
                
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpagekimanifinance').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpagekimanifinance'

            else:
                toast("Invalid username or password in kimani")
              

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
class LogInKimaniSiteManagers(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticate_userkimanisitemanagers(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_site_managers"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authenticationsitemanager WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                toast("Login successful!")
                
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpagekimanisitemanagers').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpagekimanisitemanagers'

            else:
                toast("Invalid username or password in kimani")
                

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
       
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
                
class LogInKimaniMechanics(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticate_user(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_mechanics"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authenticationmechanics WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                toast("Login successful!")
                
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpagekimanimechanics').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpagekimanimechanics'

            else:
                toast("Invalid username or password in kimani")
             

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
           
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
                
                                
                
class LogInOtherKimaniWorkers(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticate_user(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani_other_employee"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authentication_other_employee WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                toast("Login successful!")
              
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpageotherkimaniworkers').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpageotherkimaniworkers'

            else:
                toast("Invalid username or password in kimani")
            

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
           
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
                        
        


class LogInAdmin(Screen):
    #chatbot_service = ChatBotService()  # Initialize ChatBotService instance
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = MDApp.get_running_app().theme_cls  # Access theme_cls from the app
        self.theme_cls.primary_palette = "Green"  # Default palette

    def authenticateAdmin_user(self, username, password):
        try:
            # Establish a connection to the MySQL database
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="kimani"
            )
            mycursor = mydb.cursor()

            # Execute SQL query to retrieve user information
            sql = "SELECT * FROM authenticationadmin WHERE username = %s AND password = %s"
            val = (username, password)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()

            if user:
                toast("Login successful!")
                
                user_id = user[0]  # Assuming Login_id is in the first column

                # Store user_id in ScreenManager for later access
                app = MDApp.get_running_app()
                app.user_id = user_id
                # Fetch user details from database using user_id
                user_details = app.fetch_user_details(user_id)

                # Store user_details in app for access across screens
                app.user_details = user_details

                # Update Userpage with user_details
                app.root.get_screen('userpageAdmin').update_profile(user_details)


                # Fetch user progress from the user_progress table
                sql_progress = "SELECT * FROM user_progress WHERE user_id = %s"
                mycursor.execute(sql_progress, (user_id,))
                progress = mycursor.fetchone()

                self.manager.current = 'userpageAdmin'

            else:
                toast("Invalid username or password in kimani")
               

        except mysql.connector.Error as err:
            toast("Database connection error:", err)
            
            
    #def ask_question(self, question):
        #response = self.chatbot_service.get_response(question)
        #self.ids.chat_history.text += f"You: {question}\nBot: {response}\n"
        



class KimaniDeliveryNotes(Screen):
    def __init__(self, **kwargs):
        super(KimaniDeliveryNotes, self).__init__(**kwargs)
        self.name = "kimanideliverynotes"
         # Set the window size
        self.build_table()

    def build_table(self):
        layout = self.ids.main_layout

        # Create a BoxLayout for the heading and inputs
        heading_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(100)
        )

        # Add heading label
        heading_label = MDLabel(
            text="DELIVERY NOTE",
            halign="center",
            bold=True,
            underline=True,
            font_style="H5",
            size_hint_y=None,
            height=dp(40)
        )
        heading_layout.add_widget(heading_label)

        # Add TO: and Date: input fields
        info_layout = MDBoxLayout(
            orientation='horizontal',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40)
        )

        self.to_input = MDTextField(hint_text="Enter recipient", size_hint_x=None, width=dp(150))
        date_input = MDTextField(hint_text="MM/DD/YYYY", size_hint_x=None, width=dp(120))
       
        info_layout.add_widget(MDLabel(text="TO:", valign="center", size_hint_x=None, width=dp(50)))
        info_layout.add_widget(self.to_input)
        info_layout.add_widget(MDLabel(text="Date:", valign="center", size_hint_x=None, width=dp(50)))
        info_layout.add_widget(date_input)
       
        heading_layout.add_widget(info_layout)

        # Create a ScrollView to make the table scrollable
        scrollview = ScrollView(size_hint=(1, None), size=(self.width, dp(400)))

        # Create a GridLayout for the table
        table_layout = MDGridLayout(
            cols=3,  # Number of columns (adjust based on your table)
            spacing=dp(10),
            padding=dp(10),
            size_hint_y=None,
        )
        table_layout.bind(minimum_height=table_layout.setter('height'))

        # Add column headers
        headers = ["S/No.", "Quantity", "Description"]
        for header in headers:
            table_layout.add_widget(MDLabel(text=header, halign="center", bold=True, size_hint_y=None, height=dp(40)))

        # Add rows of editable text fields
        self.text_fields = []
        for i in range(10):  # Number of rows (you can adjust as needed)
            table_layout.add_widget(MDLabel(text=str(i + 1), halign="center", size_hint_y=None, height=dp(40)))  # Row number
            row_fields = []
            for j in range(2):  # Number of editable columns (excluding the "S/No." column)
                field = MDTextField(size_hint_y=None, height=dp(40))
                row_fields.append(field)
                table_layout.add_widget(field)
            self.text_fields.append(row_fields)

        # Add the GridLayout to the ScrollView
        scrollview.add_widget(table_layout)
        
        # Clear the layout before adding new widgets
        layout.clear_widgets()
        layout.add_widget(heading_layout)
        layout.add_widget(scrollview)

        # Add a submit button
        submit_button = MDRaisedButton(
            text="Submit",
            size_hint=(None, None),
            size=(dp(100), dp(50)),
            pos_hint={"center_x": .5}
        )
        submit_button.bind(on_release=self.submit_data)
        layout.add_widget(submit_button)

    def submit_data(self, instance):
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='kimani_stores'
        )
        cursor = connection.cursor()

        # Extract data
        recipient = self.to_input.text
        report_date = self.ids.date_input.text
        
        for i, row_fields in enumerate(self.text_fields):
            serial_no = i + 1
            quantity = row_fields[0].text



            description = row_fields[1].text
            
            # Calculate unit price and total price based on your requirements
            unit_price = 0.00
            total_price = float(quantity) * unit_price
            
            # Insert into the database
            cursor.execute("""
                INSERT INTO reports (serial_no, quantity, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (serial_no, "quantity", description))

        connection.commit()
        cursor.close()
        connection.close()

        # Notify the user (this is a placeholder; replace with actual notification code)
        toast("Data submitted successfully")
       

        # Optionally, you can send this data to another app user
        # self.send_data_to_user(data)  # Implement this method as needed

    def send_data_to_user(self, data):
        # Implement this method to send data to another app user
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()
        
        
    def send_data_to_user(self, data):
        # Placeholder function to demonstrate sending data
    # Replace with actual implementation
    
    
    # Example endpoint (replace with your actual endpoint)
        endpoint = "https://example.com/api/send_data"
    
    # Send data via POST request
        response = requests.post(endpoint, json=data)
    
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Failed to send data")
class KimaniGoodReceivedNotes(Screen):
    def __init__(self, **kwargs):
        super(KimaniGoodReceivedNotes, self).__init__(**kwargs)
        self.name = "kimanigoodsreceivednotes"
         # Set the window size
        self.build_table()

    def build_table(self):
        layout = self.ids.main_layout

        # Create a BoxLayout for the heading and inputs
        heading_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(100)
        )

        # Add heading label
        heading_label = MDLabel(
            text="GOODS RECEIVED NOTES",
            halign="center",
            bold=True,
            underline=True,
            font_style="H5",
            size_hint_y=None,
            height=dp(40)
        )
        heading_layout.add_widget(heading_label)

        # Add TO: and Date: input fields
        info_layout = MDBoxLayout(
            orientation='horizontal',
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(40)
        )

        self.to_input = MDTextField(hint_text="Enter recipient", size_hint_x=None, width=dp(150))
        date_input = MDTextField(hint_text="MM/DD/YYYY", size_hint_x=None, width=dp(120))
       
        info_layout.add_widget(MDLabel(text="TO:", valign="center", size_hint_x=None, width=dp(50)))
        info_layout.add_widget(self.to_input)
        info_layout.add_widget(MDLabel(text="Date:", valign="center", size_hint_x=None, width=dp(50)))
        info_layout.add_widget(date_input)
       
        heading_layout.add_widget(info_layout)

        # Create a ScrollView to make the table scrollable
        scrollview = ScrollView(size_hint=(1, None), size=(self.width, dp(400)))

        # Create a GridLayout for the table
        table_layout = MDGridLayout(
            cols=3,  # Number of columns (adjust based on your table)
            spacing=dp(10),
            padding=dp(10),
            size_hint_y=None,
        )
        table_layout.bind(minimum_height=table_layout.setter('height'))

        # Add column headers
        headers = ["S/No.", "Quantity", "Description"]
        for header in headers:
            table_layout.add_widget(MDLabel(text=header, halign="center", bold=True, size_hint_y=None, height=dp(40)))

        # Add rows of editable text fields
        self.text_fields = []
        for i in range(10):  # Number of rows (you can adjust as needed)
            table_layout.add_widget(MDLabel(text=str(i + 1), halign="center", size_hint_y=None, height=dp(40)))  # Row number
            row_fields = []
            for j in range(2):  # Number of editable columns (excluding the "S/No." column)
                field = MDTextField(size_hint_y=None, height=dp(40))
                row_fields.append(field)
                table_layout.add_widget(field)
            self.text_fields.append(row_fields)

        # Add the GridLayout to the ScrollView
        scrollview.add_widget(table_layout)
        
        # Clear the layout before adding new widgets
        layout.clear_widgets()
        layout.add_widget(heading_layout)
        layout.add_widget(scrollview)

        # Add a submit button
        submit_button = MDRaisedButton(
            text="Submit",
            size_hint=(None, None),
            size=(dp(100), dp(50)),
            pos_hint={"center_x": .5}
        )
        submit_button.bind(on_release=self.submit_data)
        layout.add_widget(submit_button)

    def submit_data(self, instance):
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='kimani_stores'
        )
        cursor = connection.cursor()

        # Extract data
        recipient = self.to_input.text
        report_date = self.ids.date_input.text
        
        for i, row_fields in enumerate(self.text_fields):
            serial_no = i + 1
            quantity = row_fields[0].text
            description = row_fields[1].text
            
            # Calculate unit price and total price based on your requirements
            unit_price = 0.00
            total_price = float(quantity) * unit_price
            
            # Insert into the database
            cursor.execute("""
                INSERT INTO reports (serial_no, quantity, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (serial_no, "quantity", description))

        connection.commit()
        cursor.close()
        connection.close()

        # Notify the user (this is a placeholder; replace with actual notification code)
        toast("Data submitted successfully")
        

        # Optionally, you can send this data to another app user
        # self.send_data_to_user(data)  # Implement this method as needed

    def send_data_to_user(self, data):
        # Implement this method to send data to another app user
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()
        
        
    def send_data_to_user(self, data):
        # Placeholder function to demonstrate sending data
    # Replace with actual implementation
    
    
    # Example endpoint (replace with your actual endpoint)
        endpoint = "https://example.com/api/send_data"
    
    # Send data via POST request
        response = requests.post(endpoint, json=data)
    
        if response.status_code == 200:
            toast("Data sent successfully")
            
        else:
            toast("Failed to send data")
            
        
class MyApp(MDApp):
    

    def build(self):
        self.screen_manager = ScreenManager(transition=FadeTransition())
        self.theme_cls.material_style= "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette='Green'
        


        self.wm = ScreenManager(transition=FadeTransition())

        try:
            Builder.load_file("kimani.kv")  # Load the KV file if needed
        except Exception as e:
            print(f"Error loading KV file: {e}")
            raise
        screens = [
            KimaniDayShiftDrillingReport(name="kimanidayshiftdrillingreport"),
            KimaniNightShiftDrillingReport(name="kimaninightshiftdrillingreport"),
            SignupAdmin(name="signupAdmin"),
            SignupKimaniDrilling(name="signupkimanidrilling"),
            SignupKimaniFinance(name="signupkimanifinance"),
            SignupKimaniMechanics(name="signupkimanimechanics"),
            SignupOtherKimaniWorkers(name="signupotherkimaniworkers"),
            SignupKimaniTransport(name="signupkimanitransport"),
            SignupKimaniStores(name="signupkimanistores"),
            SiteManagerDrillingReport(name="sitemanagerdrillingreport"),
            DayShiftDrillingReport(name="dayshiftdrillingreport"),
            NightShiftDrillingReport(name="nightshiftdrillingreport"),
            SignupKimaniSiteManagers(name="signupkimanisitemanagers"),
            LogInKimaniDrilling(name="loginkimanidrilling"),
            LogInKimaniFinance(name="loginkimanifinance"),
            KimaniSiteManagerReport(name="kimanisitemanagerreport"),
            LogInKimaniMechanics(name="loginkimanimechanics"),
            LogInOtherKimaniWorkers(name="loginotherkimaniworkers"),
            LogInKimaniTransport(name="loginkimanitransport"),
            LogInKimaniStore(name="loginkimanistores"),
            LogInKimaniSiteManagers(name="loginkimanisitemanagers"),
            ContactUs(name="contact_us"),
            LogInAdmin(name="loginAdmin"),
            Home(name="home"),
            KimaniReportOptions(name='kimanireportoptions'),
            UserpageKimaniTransport(name="userpagekimanitransport"),
            UserpageKimaniDrilling(name="userpagekimanidrilling"),
            UserpageKimaniFinance(name="userpagekimanifinance"),
            UserpageKimaniMechanics(name="userpagekimanimechanics"),
            UserpageOtherKimaniWorkers(name="userpageotherkimaniworkers"),    
            UserpageKimaniStores(name="userpagekimanistores"),
            UserpageKimaniSiteManagers(name="userpagekimanisitemanagers"),
            KimaniDrillingReport(name="kimanidrillingreport"),
            ForgotKimaniDrilling(name="forgotkimanidrilling"),
            ForgotKimaniFinance(name="forgotkimanifinance"),
            ForgotKimaniSiteManagers(name="forgotkimanisitemanagers"),
            ForgotKimaniTransport(name="forgotkimanitransport"),
            ForgotOtherKimaniWorkers(name="forgototherkimaniworkers"),
            ForgotKimaniStores(name="forgotkimanistores"),
            ForgotKimaniMechanics(name="forgotkimanimechanics"),
            ForgotAdmin(name="forgotAdmin"),
            SplashScreen(name="splash"),
            Password_reset(name="password_reset"),
            PasswordResetKimaniDrilling(name="passwordresetkimanidrilling"),
            PasswordResetKimaniFinance(name="passwordresetkimanifinance"),
            PasswordResetKimaniMechanics(name="passwordresekimanimechanics"),
            PasswordResetKimaniSiteManagers(name="passwordresetkimanisitemanagers"),
            KimaniSitemanagerReportOption(name="kimanisitemanagerreportoption"),
            PasswordResetKimaniStores(name="passwordresetkimanistores"),
            PasswordResetKimaniTransport(name="passwordresetkimanitransport"),
            PasswordResetOtherKimaniWorkers(name="passwordresetotherkimaniworkers"),
            Password_resetAdmin(name="passwordresetAdmin"), 
            KimaniStoreReports(name="kimanistorereports") ,   
            Settings(name="settings"),
            KimaniDeliveryNotes(name="kimanideliverynotes"),
            Settings(name="settings"),
            Lof(name="loff"),
            
            
            
            
            
        ]

        for screen in screens:
            self.wm.add_widget(screen)
            
            
        # Initialize self.store (assuming it's intended to store user_id)
        self.wm.current = 'splash'

        self.store = {}  # Or you can use kivy.storage.Storage if needed
        def on_start(self):
            # Set the initial screen to 'splash'
            self.wm.current = 'splash'


        return self.wm  # Return the ScreenManager instance as the root widget
    
    
    def load_chat_data(self):
        # Example function to load chat data into chat screen
        chat_history = ["Hello!", "How are you?", "Example message"]
        self.chat.load_chat_history(chat_history)

    def send_message_to_chat(self, message):
        # Example function to send message from any screen to chat screen
        self.chat.send_message(message)
    
    
   
    def show_date_picker(self):
        self.root.get_screen('signupkimanifinance').show_date_picker()
        
    def show_date_picker(self):
        self.root.get_screen('signupkimanidrilling').show_date_picker()
        
        
    def show_date_picker(self):
        self.root.get_screen('signupkimanistores').show_date_picker()
    def show_date_picker(self):
        self.root.get_screen('signupkimanimechanics').show_date_picker()
    def show_date_picker(self):
        self.root.get_screen('signupkimanisitemanager').show_date_picker()
    def show_date_picker(self):
        self.root.get_screen('signupkimaniotherworkers').show_date_picker()
    def show_date_picker(self):
        self.root.get_screen('signupkimanitransport').show_date_picker()
    def show_date_picker(self):
        self.root.get_screen('kimanidayshiftdrillingreport').show_date_picker()
    def show_date_picker(self):
        self.root.get_screen('kimaninightshiftdrillingreport').show_date_picker()
        
    def on_start(self):
        pass
    
    
    #def show_date_picker(self):
            # Access the show_date_picker method from an instance of the Customer class
        #customer_screen = self.root.get_screen('signup')
        #customer_screen.show_date_picker()

    def current_slide(self, index):
        pass

    def show_settings_screen(self):
        self.root.current = 'settings'

    def callback_2(self):
        # Implement callback_2 functionality
        pass
    @staticmethod
    def hash_password(password):
        return password
    
    def on_login(self, Login_id):
        self.store.put('Login_id', value=Login_id)
    # Fetch user details from database using user_id
        user_details = self.fetch_user_details(Login_id)
        self.root.get_screen('userpagekimanitransport').update_profile(user_details)

    def fetch_user_details(self, Login_id):
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kimani_transport"
    )
        cursor = mydb.cursor()
    
    # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationtransport WHERE Login_id = %s"
        cursor.execute(sql_fetch_user, (Login_id,))
        user_details = cursor.fetchone()

    # Close the cursor and connection
        cursor.close()
        mydb.close()

    # Format user_details as a dictionary
        if user_details:
             user_details_dict = {
                'Log_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'gender':user_details[4],
                'age': user_details[3],
                'email': user_details[6],
                'phone': user_details[5],
                'bio': user_details[7]  # Assuming 'bio' is a column in your table
            # Add more fields as needed
        }
             return user_details_dict
        else:
             return {}
      
        
    def on_login(self, Login_id):
        self.store.put('Login_id', value=Login_id)
    # Fetch user details from database using user_id
        user_details = self.fetch_user_details(Login_id)
        self.root.get_screen('userpagekimanidrilling').update_profile(user_details)

    def fetch_user_details(self, Login_id):
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kimani_drilling"
    )
        cursor = mydb.cursor()
    
    # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationdrilling WHERE Login_id = %s"
        cursor.execute(sql_fetch_user, (Login_id,))
        user_details = cursor.fetchone()

    # Close the cursor and connection
        cursor.close()
        mydb.close()

    # Format user_details as a dictionary
        if user_details:
             user_details_dict = {
                'Log_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'gender':user_details[4],
                'age': user_details[3],
                'email': user_details[6],
                'phone': user_details[5],
                'bio': user_details[7]  # Assuming 'bio' is a column in your table
            # Add more fields as needed
        }
             return user_details_dict
        else:
             return {}
      
         
         
         
    def on_login(self, Login_id):
        self.store.put('Login_id', value=Login_id)
    # Fetch user details from database using user_id
        user_details = self.fetch_user_details(Login_id)
        self.root.get_screen('userpagekimanistores').update_profile(user_details)

    def fetch_user_details(self, Login_id):
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kimani_stores"
    )
        cursor = mydb.cursor()
    
    # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationstores WHERE Login_id = %s"
        cursor.execute(sql_fetch_user, (Login_id,))
        user_details = cursor.fetchone()

    # Close the cursor and connection
        cursor.close()
        mydb.close()

    # Format user_details as a dictionary
        if user_details:
             user_details_dict = {
                'Log_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'gender':user_details[4],
                'age': user_details[3],
                'email': user_details[6],
                'phone': user_details[5],
                'bio': user_details[7]  # Assuming 'bio' is a column in your table
            # Add more fields as needed
        }
             return user_details_dict
        else:
             return {}
    
    def on_login(self, Login_id):
        self.store.put('Login_id', value=Login_id)
    # Fetch user details from database using user_id
        user_details = self.fetch_user_details(Login_id)
        self.root.get_screen('userpagekimanisitemanagers').update_profile(user_details)

    def fetch_user_details(self, Login_id):
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kimani_site_managers"
    )
        cursor = mydb.cursor()
    
    # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationsitemanagers WHERE Login_id = %s"
        cursor.execute(sql_fetch_user, (Login_id,))
        user_details = cursor.fetchone()

    # Close the cursor and connection
        cursor.close()
        mydb.close()

    # Format user_details as a dictionary
        if user_details:
             user_details_dict = {
                'Log_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'gender':user_details[4],
                'age': user_details[3],
                'email': user_details[6],
                'phone': user_details[5],
                'bio': user_details[7]  # Assuming 'bio' is a column in your table
            # Add more fields as needed
        }
             return user_details_dict
        else:
             return {}
         
    
    def on_login(self, Login_id):
        self.store.put('Login_id', value=Login_id)
    # Fetch user details from database using user_id
        user_details = self.fetch_user_details(Login_id)
        self.root.get_screen('userpagekimanimechanics').update_profile(user_details)

    def fetch_user_details(self, Login_id):
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kimani_mechanics"
    )
        cursor = mydb.cursor()
    
    # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authenticationmechanics WHERE Login_id = %s"
        cursor.execute(sql_fetch_user, (Login_id,))
        user_details = cursor.fetchone()

    # Close the cursor and connection
        cursor.close()
        mydb.close()

    # Format user_details as a dictionary
        if user_details:
             user_details_dict = {
                'Log_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'gender':user_details[4],
                'age': user_details[3],
                'email': user_details[6],
                'phone': user_details[5],
                'bio': user_details[7]  # Assuming 'bio' is a column in your table
            # Add more fields as needed
        }
             return user_details_dict
        else:
             return {}
        
    
    def on_login(self, Login_id):
        self.store.put('Login_id', value=Login_id)
    # Fetch user details from database using user_id
        user_details = self.fetch_user_details(Login_id)
        self.root.get_screen('userpageotherkimaniworkers').update_profile(user_details)

    def fetch_user_details(self, Login_id):
        # Establish a connection to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kimani_other_employee"
    )
        cursor = mydb.cursor()
    
    # Execute SQL query to fetch user details based on user_id
        sql_fetch_user = "SELECT * FROM authentication_other_employee WHERE Login_id = %s"
        cursor.execute(sql_fetch_user, (Login_id,))
        user_details = cursor.fetchone()

    # Close the cursor and connection
        cursor.close()
        mydb.close()

    # Format user_details as a dictionary
        if user_details:
             user_details_dict = {
                'Log_id': user_details[0],
                'username': user_details[1],
                'full_name': user_details[2],
                'gender':user_details[4],
                'age': user_details[3],
                'email': user_details[6],
                'phone': user_details[5],
                'bio': user_details[7]  # Assuming 'bio' is a column in your table
            # Add more fields as needed
        }
             return user_details_dict
        else:
             return {}
      
   
    def chat(self):
        print("Chat method called")
        # Implementation for the chat method
        pass    

    def on_logout(self):
        if 'user_id' in self.store:
            del self.store['user_id']
        # Reset user_details on userpage
        self.root.get_screen('userpagekimanistore').reset_profile()
        self.show_screen('home')
    def on_logout(self):
        if 'user_id' in self.store:
            del self.store['user_id']
        # Reset user_details on userpage
        self.root.get_screen('userpagekimanidrilling').reset_profile()
        self.show_screen('home')
    def on_logout(self):
        if 'user_id' in self.store:
            del self.store['user_id']
        # Reset user_details on userpage
        self.root.get_screen('userpagekimanisitemanager').reset_profile()
        self.show_screen('home')
    def on_logout(self):
        if 'user_id' in self.store:
            del self.store['user_id']
        # Reset user_details on userpage
        self.root.get_screen('userpagekimanimechanics').reset_profile()
        self.show_screen('home')
    def on_logout(self):
        if 'user_id' in self.store:
            del self.store['user_id']
        # Reset user_details on userpage
        self.root.get_screen('userpageotherkimaniworkers').reset_profile()
        self.show_screen('home')
    def on_logout(self):
        if 'user_id' in self.store:
            del self.store['user_id']
        # Reset user_details on userpage
        self.root.get_screen('userpagekimanifinance').reset_profile()
        self.show_screen('home')
    def on_logout(self):
        if 'user_id' in self.store:
            del self.store['user_id']
        # Reset user_details on userpage
        self.root.get_screen('userpagekimanitransport').reset_profile()
        self.show_screen('home')
    
                                        
    def update_map_markers(self, gps_data):
        map_view = self.root.ids.map_view  # Assuming map_view is the ID of your MapView

        map_view.remove_all_markers()

        if gps_data:
            for item in gps_data:
                lat = item.get('latitude')
                lon = item.get('longitude')
                if lat and lon:
                    marker = MapMarker(lat=lat, lon=lon)
                    map_view.add_marker(marker)
                    
    def send_message(self):
        Chat= self.root.get_screen('chat')
        message=Chat.message_input.text
        if message:
            Chat.chat_log.add_widget(MDLabel(text=message,halign='left')) 
        
        Chat.message_input.text=''   
              
    def show_screen(self, screen_name):
        self.wm.current = screen_name
          


    


class Settings(Screen):
    pass

if __name__ == "__main__":
    Window.size = (350, 640)
    
    MyApp().run()
