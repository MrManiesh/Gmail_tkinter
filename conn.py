import sqlite3

conn = sqlite3.connect('zeeuser.db')
c = conn.cursor()

# c.execute(""" CREATE TABLE zeeuser (z_fname text,z_lname text,z_dob text,z_mob integer,z_email text,z_id text,z_pass text)""" )

def get_all_user_id():
    all_username_in_list=[]
    with conn:
        c.execute(""" SELECT z_id FROM zeeuser """)
        for i in c.fetchall():
            all_username_in_list.append(i[0])
        return tuple(all_username_in_list)

def add_user(z_fname,z_lname,z_dob,z_mob,z_email,z_id,z_pass):
    with conn:
        c.execute("""INSERT INTO zeeuser VALUES (:z_fname,:z_lname,:z_dob,:z_mob,:z_email,:z_id,:z_pass)""",
        {'z_fname':z_fname,'z_lname':z_lname,'z_dob':z_dob,'z_mob':z_mob,'z_email':z_email,'z_id':z_id,'z_pass':z_pass})


def get_data(z_id):
    with conn:
        c.execute("""SELECT * FROM zeeuser WHERE z_id = :z_id""",{'z_id':z_id})
        return c.fetchall()[0]
# print(get_data("msdhoni"))

