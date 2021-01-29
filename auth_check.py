import connection
import mysql.connector 

#connection
mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database=""
)


def authentication(license_number):
    """This is function is to check where the detected license number plate exists in allowed list of numbers. """

    mycursor = mydb.cursor()
    mycursor.execute(r"SELECT * FROM auth_table WHERE allowed_license_plates='{}'".format(license_number))
    myresult = mycursor.fetchall()
    if myresult:
        allowance = "ALLOWED"
    else:
        allowance = "NOT ALLOWED"
    mycursor.close()
    return allowance


def enter_logs(location, img_path, license_number, date_time, device_id, allowance):
    """This fucntion adds log details into log table in database"""
    mycursor = mydb.cursor()
    sql = "INSERT INTO logs_table(location, path_of_image, license_number, datetime, device_id, allowed) VALUES (%s,%s,%s,%s,%s,%s)"
    val= (location, img_path, license_number, date_time, device_id, allowance)
    mycursor.execute(sql, val)
    mydb.commit()
    insert_result = mycursor.rowcount
    return insert_result


lp=""
#temporary
location = ""
img_path = ""
license_number = ""
date_time = ""
device_id = ""
allow = ""

allow = authentication(lp)
print (allow)
#entering logs
log_result = enter_logs(location, img_path, license_number, date_time, device_id, allow)
