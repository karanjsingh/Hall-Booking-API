import sqlite3
from datetime import datetime
from controller.controller import app


def initialize_database():
    """
    Initializes and pre-populates the database
    Database name - booking
    Table name - BOOKING
    """
    connection = sqlite3.connect('database/booking.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS BOOKING")
    cursor.execute(("CREATE TABLE BOOKING ("
                    "  ID VARCHAR(20) PRIMARY KEY NOT NULL,"
                    "  HALL_NAME VARCHAR(20) NOT NULL,"
                    "  CAPACITY INT NOT NULL,"
                    "  START_TIME TIMESTAMP NOT NULL,"
                    "  END_TIME TIMESTAMP NOT NULL)"))
    cursor.execute("INSERT INTO BOOKING (ID, HALL_NAME, CAPACITY, START_TIME, END_TIME) VALUES (?, ?, ?, ?, ?);",
                   ("2546543",
                    "A",
                    50,
                    datetime.strptime("2021-06-27 15:00:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2021-06-27 16:00:00", "%Y-%m-%d %H:%M:%S")))
    cursor.execute("INSERT INTO BOOKING (ID, HALL_NAME, CAPACITY, START_TIME, END_TIME) VALUES (?, ?, ?, ?, ?);",
                   ("2546541",
                    "A",
                    50,
                    datetime.strptime("2021-06-27 16:00:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2021-06-27 17:00:00", "%Y-%m-%d %H:%M:%S")))
    cursor.execute("INSERT INTO BOOKING (ID, HALL_NAME, CAPACITY, START_TIME, END_TIME) VALUES (?, ?, ?, ?, ?);",
                   ("2546542",
                    "B",
                    100,
                    datetime.strptime("2021-06-27 16:00:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2021-06-27 17:00:00", "%Y-%m-%d %H:%M:%S")))
    cursor.execute("INSERT INTO BOOKING (ID, HALL_NAME, CAPACITY, START_TIME, END_TIME) VALUES (?, ?, ?, ?, ?);",
                   ("2546544",
                    "C",
                    200,
                    datetime.strptime("2021-06-27 16:30:00", "%Y-%m-%d %H:%M:%S"),
                    datetime.strptime("2021-06-27 17:30:00", "%Y-%m-%d %H:%M:%S")))

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    initialize_database()
    app.run(host='0.0.0.0', port=8085, threaded=True)
