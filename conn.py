import sqlite3

conn = sqlite3.connect('zeeuser.db')
c = conn.cursor()

# c.execute(""" CREATE TABLE zeeuser (z_fname text,z_lname text,z_dob text,z_mob integer,z_email text,z_id text,z_pass text)""" )

def get_data(z_id):
    with conn:
        c.execute("""SELECT * FROM zeeuser WHERE z_id = :z_id""",{'z_id':z_id})
        return c.fetchall()[0]
# print(get_data("msdhoni"))

