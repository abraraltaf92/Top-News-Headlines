from selenium import webdriver # pip install selenium
from selenium.webdriver.common.keys import Keys
import datetime,time
import smtplib
from email.message import EmailMessage
from decouple import config      # pip install python-decouple


''' 						!!!FOR PRIVACY!!!
Create an .env file in the root of directory and store your email and password there as:
EMAIL='{whatever is your email from you will send the news }'
PASSWORD='{whatever is your password for the email address}'    
'''


# getting values from environment variable stored in .env file

API_EMAIL = config('EMAIL')
API_PASSWORD = config('PASSWORD')
#Uncomment the below line

#RECIEVER_MAIL = '{whomsoever you are gonna send the headlines}' 


td = datetime.date.today()



driver= webdriver.Chrome('/Users/abraraltaflone/code/python/web_scrap/chromedriver') #download driver from : https://chromedriver.chromium.org/downloads

print ("Connecting to Legit News source, Please have some patience .....\n")
time.sleep(2)
news_site = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

print (" ------------------------------------------------------------------------------------------- ")
print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  TODAY's TOP NEWS HEADLINES  <<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")
print ("Date:",td.strftime("%d-%b-%Y"))   # Date-Month-Year
print (" \n ")

# Web driver to openup website

driver.get(news_site)
driver.implicitly_wait(10) # 10 secs implicit wait
elems = driver.find_elements_by_tag_name('h3')

# 
file_loc = '/Users/abraraltaflone/code/python/web_scrap/headlines/newsfile.txt' #creating anew file where data will be stored
file_to_write = open(file_loc, 'w+')
ind = 1
for elem in elems:
    file_to_write.write(str(ind)+ ') '+elem.text+'\n')
    print (str(ind) + ") " + elem.text)
    ind += 1
file_to_write.close()
print('\n')

# Compose message

msg = EmailMessage()
msg['From'] = API_EMAIL
msg['To']   = RECIEVER_MAIL
msg['Subject'] = " Hello ! Today's TOP NEWS HEADLINES >>"

with open(file_loc,'rb') as f: # reading in binary code
    N_file = f.read()

# Body of email  

msg.set_content("Find the attached document for detailed NEWS .. ")
msg.add_attachment(N_file, maintype = 'document',subtype = 'txt', filename = f.name )

# Configure server

# For different Servers, there are different server names, quite obvious!
# For Gmail Accounts , SMTP SERVER NAME:'smtp.gmail.com' and SMPT port :587 for tls

server = smtplib.SMTP('smtp.gmail.com', 587) #tls , ssl #
server.ehlo()     #handshake
server.starttls() # using tls
server.login(API_EMAIL,API_PASSWORD)
server.send_message(msg)

# printing final info

print (f"A copy of this NEWS HEADLINES has been sent to your E-mail {RECIEVER_MAIL} Successfuly !!")
print ("Have a Nice Day !!")
server.quit()






















