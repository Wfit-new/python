import sqlite3
conn = sqlite3.connect('facebook.db')
cursor = conn.cursor()

user_email = input('Provide your email: ')
provided_pass = input('Now, provide your password: ')

cursor.execute("select * from users where email = :email", {'email': user_email})
user = cursor.fetchone()

if user is not None and user[2] == provided_pass:
   print('Welcome inside')
else:
   print('Invalid user email or password')

conn.commit()
conn.close()

