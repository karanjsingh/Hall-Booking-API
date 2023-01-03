from repository import query_database
from model import halls
from datetime import datetime as dt
def fetch_all_bookings():
    """
    Fetches all booking from the database table 'BOOKING'
    """
    client = query_database.DB_Client()
    bookings = client.execute_sql_query("SELECT * FROM BOOKING")
    print(bookings)
    return bookings

def fetch_all_halls(content):
    print(content)
    st = dt.strptime(content['startTime'], "%Y-%m-%d %H:%M:%S")
    et = dt.strptime(content['endTime'], "%Y-%m-%d %H:%M:%S")
    cap = content['capacity']

    client = query_database.DB_Client()
    bookings = client.execute_sql_query("SELECT * FROM BOOKING")
    # print(bookings)
    # h=Halls()
    hal = [e.name for e in halls.Halls]
    dic = {}
    for e in halls.Halls:
        dic[e.name]=e.value
    temp=set()
    for id,halname,capacity,sttime,endtime in bookings:
        print(halname)
        if halname in temp:
            continue
        sttime = dt.strptime(sttime, "%Y-%m-%d %H:%M:%S")
        endtime = dt.strptime(endtime, "%Y-%m-%d %H:%M:%S")
        # print(halls.Halls.halname.value,"---")
        if (et<=sttime or  st>=endtime) and cap<=dic[halname]:
            continue
        else:
            hal.remove(halname)
            temp.add(halname)
    print(hal)
    return hal

