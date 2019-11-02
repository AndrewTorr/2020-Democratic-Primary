"""Adds Poll objects to the database. These polls start from October 2019."""

import sys
import database
import datetime
import constants as c


def add_to_database(db):
    """
    Adds polls starting from late October 2019 to the database.

    :param db:
        The database to add the polls to.
    :return db:
        The database with the polls added.
    
    """
    polls = [
        database.Poll(c.Q_PRIMARY, c.S_USA, 7.12, {c.C_BIDEN:25, c.C_WARREN:24,
            c.C_SANDERS:15, c.C_BUTTIGIEG:8, c.C_HARRIS:5, c.C_YANG:3,
            c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:1, c.C_BOOKER:2,
            c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:2, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:0},
            datetime.date(2019, 10, 19)),

        database.Poll(c.Q_PRIMARY, c.S_IOWA, 6.88, {c.C_BIDEN:20,
            c.C_WARREN:23, c.C_SANDERS:16, c.C_BUTTIGIEG:13, c.C_HARRIS:4,
            c.C_YANG:2, c.C_OROURKE:1, c.C_BENNET:1, c.C_GABBARD:2,
            c.C_BOOKER:3, c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:2,
            c.C_DELANEY:1, c.C_MESSAM:0, c.C_BULLOCK:1, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 19)),

        database.Poll(c.Q_PRIMARY, c.S_NEW_HAMPSHIRE, 7.34, {c.C_BIDEN:23,
            c.C_WARREN:27, c.C_SANDERS:17, c.C_BUTTIGIEG:10, c.C_HARRIS:5,
            c.C_YANG:3, c.C_OROURKE:1, c.C_BENNET:0, c.C_GABBARD:2,
            c.C_BOOKER:1, c.C_KLOBUCHAR:2, c.C_CASTRO:0, c.C_STEYER:2,
            c.C_DELANEY:1, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 19)),

        database.Poll(c.Q_PRIMARY, c.S_NEVADA, 7.01, {c.C_BIDEN:22,
            c.C_WARREN:20, c.C_SANDERS:19, c.C_BUTTIGIEG:5, c.C_HARRIS:5,
            c.C_YANG:3, c.C_OROURKE:1, c.C_BENNET:0, c.C_GABBARD:1,
            c.C_BOOKER:2, c.C_KLOBUCHAR:1, c.C_CASTRO:1, c.C_STEYER:4,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:1}, datetime.date(2019, 10, 19)),

        database.Poll(c.Q_PRIMARY, c.S_SOUTH_CAROLINA, 6.65, {c.C_BIDEN:39,
            c.C_WARREN:14, c.C_SANDERS:11, c.C_BUTTIGIEG:3, c.C_HARRIS:6,
            c.C_YANG:2, c.C_OROURKE:1, c.C_BENNET:1, c.C_GABBARD:1,
            c.C_BOOKER:4, c.C_KLOBUCHAR:1, c.C_CASTRO:1, c.C_STEYER:4,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:1}, datetime.date(2019, 10, 19)),

        database.Poll(c.Q_PRIMARY, c.S_CALIFORNIA, 7.20, {c.C_BIDEN:23,
            c.C_WARREN:22, c.C_SANDERS:21, c.C_BUTTIGIEG:5, c.C_HARRIS:10,
            c.C_YANG:5, c.C_OROURKE:3, c.C_BENNET:10, c.C_GABBARD:2,
            c.C_BOOKER:2, c.C_KLOBUCHAR:1, c.C_CASTRO:2, c.C_STEYER:1,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 19)),
                                                        
        database.Poll(c.Q_PRIMARY, c.S_TEXAS, 5.99, {c.C_BIDEN:27,
            c.C_WARREN:16, c.C_SANDERS:13, c.C_BUTTIGIEG:4, c.C_HARRIS:7,
            c.C_YANG:2, c.C_OROURKE:17, c.C_BENNET:0, c.C_GABBARD:1,
            c.C_BOOKER:1, c.C_KLOBUCHAR:2, c.C_CASTRO:3, c.C_STEYER:0,
            c.C_DELANEY:1, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:1}, datetime.date(2019, 10, 19)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 2.69, {c.C_BIDEN:19, c.C_WARREN:12,
            c.C_SANDERS:17, c.C_BUTTIGIEG:3, c.C_HARRIS:4, c.C_YANG:3,
            c.C_OROURKE:3, c.C_BENNET:0, c.C_GABBARD:1, c.C_BOOKER:2,
            c.C_KLOBUCHAR:1, c.C_CASTRO:1, c.C_STEYER:0, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:1},
            datetime.date(2019, 10, 20)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 2.14, {c.C_BIDEN:32, c.C_WARREN:22,
            c.C_SANDERS:17, c.C_BUTTIGIEG:5, c.C_HARRIS:7, c.C_YANG:2,
            c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:1, c.C_BOOKER:2,
            c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:0},
            datetime.date(2019, 10, 20)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 3.51, {c.C_BIDEN:30, c.C_WARREN:21,
            c.C_SANDERS:18, c.C_BUTTIGIEG:6, c.C_HARRIS:6, c.C_YANG:3,
            c.C_OROURKE:3, c.C_BENNET:1, c.C_GABBARD:1, c.C_BOOKER:3,
            c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:1, c.C_DELANEY:1,
            c.C_MESSAM:0, c.C_BULLOCK:1, c.C_SESTAK:0, c.C_WILLIAMSON:1},
            datetime.date(2019, 10, 20)),

        database.Poll(c.Q_PRIMARY, c.S_CALIFORNIA, 1.11, {c.C_BIDEN:33,
            c.C_WARREN:18, c.C_SANDERS:17, c.C_BUTTIGIEG:4, c.C_HARRIS:8,
            c.C_YANG:4, c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:1,
            c.C_BOOKER:2, c.C_KLOBUCHAR:1, c.C_CASTRO:1, c.C_STEYER:1,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 21)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 0.86, {c.C_BIDEN:27, c.C_WARREN:21,
            c.C_SANDERS:25, c.C_BUTTIGIEG:6, c.C_HARRIS:5, c.C_YANG:4,
            c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:3, c.C_BOOKER:3,
            c.C_KLOBUCHAR:1, c.C_CASTRO:0, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:0},
            datetime.date(2019, 10, 21)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 0.88, {c.C_BIDEN:27, c.C_WARREN:19,
            c.C_SANDERS:14, c.C_BUTTIGIEG:6, c.C_HARRIS:5, c.C_YANG:2,
            c.C_OROURKE:3, c.C_BENNET:1, c.C_GABBARD:0, c.C_BOOKER:1,
            c.C_KLOBUCHAR:1, c.C_CASTRO:1, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:1, c.C_BULLOCK:0, c.C_SESTAK:1, c.C_WILLIAMSON:0},
            datetime.date(2019, 10, 21)),

        database.Poll(c.Q_PRIMARY, c.S_MICHIGAN, 0.43, {c.C_BIDEN:27,
            c.C_WARREN:23, c.C_SANDERS:12, c.C_BUTTIGIEG:4, c.C_HARRIS:4,
            c.C_YANG:1, c.C_OROURKE:1, c.C_BENNET:2, c.C_GABBARD:1,
            c.C_BOOKER:1, c.C_KLOBUCHAR:1, c.C_CASTRO:0, c.C_STEYER:0,
            c.C_DELANEY:1, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 22)),

        database.Poll(c.Q_PRIMARY, c.S_WISCONSIN, 0.76, {c.C_BIDEN:31,
            c.C_WARREN:24, c.C_SANDERS:17, c.C_BUTTIGIEG:7, c.C_HARRIS:5,
            c.C_YANG:3, c.C_OROURKE:0, c.C_BENNET:0, c.C_GABBARD:2,
            c.C_BOOKER:1, c.C_KLOBUCHAR:0, c.C_CASTRO:0, c.C_STEYER:0,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 22)),

        database.Poll(c.Q_PRIMARY, c.S_MASSACHUSETTS, 0.91, {c.C_BIDEN:18,
            c.C_WARREN:33, c.C_SANDERS:13, c.C_BUTTIGIEG:7, c.C_HARRIS:3,
            c.C_YANG:1, c.C_OROURKE:0, c.C_BENNET:0, c.C_GABBARD:2,
            c.C_BOOKER:0, c.C_KLOBUCHAR:1, c.C_CASTRO:0, c.C_STEYER:1,
            c.C_DELANEY:1, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 22)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 0.64, {c.C_BIDEN:34, c.C_WARREN:19,
            c.C_SANDERS:16, c.C_BUTTIGIEG:6, c.C_HARRIS:6, c.C_YANG:2,
            c.C_OROURKE:3, c.C_BENNET:1, c.C_GABBARD:1, c.C_BOOKER:1,
            c.C_KLOBUCHAR:3, c.C_CASTRO:0, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:0},
            datetime.date(2019, 10, 22)),

        database.Poll(c.Q_PRIMARY, c.S_SOUTH_CAROLINA, 0.80, {c.C_BIDEN:33,
            c.C_WARREN:16, c.C_SANDERS:12, c.C_BUTTIGIEG:3, c.C_HARRIS:6,
            c.C_YANG:2, c.C_OROURKE:1, c.C_BENNET:0, c.C_GABBARD:1,
            c.C_BOOKER:2, c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:4,
            c.C_DELANEY:1, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 22)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 1.26, {c.C_BIDEN:24, c.C_WARREN:21,
            c.C_SANDERS:15, c.C_BUTTIGIEG:8, c.C_HARRIS:5, c.C_YANG:3,
            c.C_OROURKE:2, c.C_BENNET:1, c.C_GABBARD:3, c.C_BOOKER:2,
            c.C_KLOBUCHAR:1, c.C_CASTRO:1, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:1},
            datetime.date(2019, 10, 22)),

        database.Poll(c.Q_PRIMARY, c.S_CALIFORNIA, 3.26, {c.C_BIDEN:19,
            c.C_WARREN:28, c.C_SANDERS:24, c.C_BUTTIGIEG:9, c.C_HARRIS:8,
            c.C_YANG:3, c.C_OROURKE:1, c.C_BENNET:0, c.C_GABBARD:2,
            c.C_BOOKER:1, c.C_KLOBUCHAR:2, c.C_CASTRO:0, c.C_STEYER:1,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 23)),

        database.Poll(c.Q_PRIMARY, c.S_SOUTH_CAROLINA, 1.46, {c.C_BIDEN:30,
            c.C_WARREN:19, c.C_SANDERS:13, c.C_BUTTIGIEG:9, c.C_HARRIS:11,
            c.C_YANG:4, c.C_OROURKE:1, c.C_BENNET:1, c.C_GABBARD:3,
            c.C_BOOKER:3, c.C_KLOBUCHAR:3, c.C_CASTRO:1, c.C_STEYER:5,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 23)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 1.06, {c.C_BIDEN:21, c.C_WARREN:28,
            c.C_SANDERS:15, c.C_BUTTIGIEG:10, c.C_HARRIS:5, c.C_YANG:1,
            c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:3, c.C_BOOKER:1,
            c.C_KLOBUCHAR:3, c.C_CASTRO:1, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:0},
            datetime.date(2019, 10, 23)),

        database.Poll(c.Q_PRIMARY, c.S_IOWA, 1.20, {c.C_BIDEN:12,
            c.C_WARREN:28, c.C_SANDERS:18, c.C_BUTTIGIEG:20, c.C_HARRIS:3,
            c.C_YANG:2, c.C_OROURKE:1, c.C_BENNET:1, c.C_GABBARD:2,
            c.C_BOOKER:1, c.C_KLOBUCHAR:4, c.C_CASTRO:0, c.C_STEYER:3,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 23)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 0.92, {c.C_BIDEN:28, c.C_WARREN:16,
            c.C_SANDERS:18, c.C_BUTTIGIEG:3, c.C_HARRIS:6, c.C_YANG:6,
            c.C_OROURKE:3, c.C_BENNET:0, c.C_GABBARD:2, c.C_BOOKER:3,
            c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:0, c.C_DELANEY:1,
            c.C_MESSAM:0, c.C_BULLOCK:1, c.C_SESTAK:0, c.C_WILLIAMSON:1},
            datetime.date(2019, 10, 24)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 3.49, {c.C_BIDEN:32, c.C_WARREN:20,
            c.C_SANDERS:20, c.C_BUTTIGIEG:7, c.C_HARRIS:6, c.C_YANG:3,
            c.C_OROURKE:2, c.C_BENNET:1, c.C_GABBARD:2, c.C_BOOKER:2,
            c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:1, c.C_DELANEY:1,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:1},
            datetime.date(2019, 10, 27)),
        
        database.Poll(c.Q_PRIMARY, c.S_NEW_HAMPSHIRE, 1.05, {c.C_BIDEN:15,
            c.C_WARREN:18, c.C_SANDERS:21, c.C_BUTTIGIEG:10, c.C_HARRIS:3,
            c.C_YANG:5, c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:5,
            c.C_BOOKER:2, c.C_KLOBUCHAR:5, c.C_CASTRO:0, c.C_STEYER:3,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:1,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 28)),

        database.Poll(c.Q_PRIMARY, c.S_ARIZONA, 0.68, {c.C_BIDEN:28,
            c.C_WARREN:21, c.C_SANDERS:21, c.C_BUTTIGIEG:12, c.C_HARRIS:4,
            c.C_YANG:5, c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:2,
            c.C_BOOKER:0, c.C_KLOBUCHAR:2, c.C_CASTRO:0, c.C_STEYER:0,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:1,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 28)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 0.80, {c.C_BIDEN:26, c.C_WARREN:17,
            c.C_SANDERS:13, c.C_BUTTIGIEG:10, c.C_HARRIS:3, c.C_YANG:3,
            c.C_OROURKE:0, c.C_BENNET:0, c.C_GABBARD:4, c.C_BOOKER:2,
            c.C_KLOBUCHAR:2, c.C_CASTRO:0, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:1},
            datetime.date(2019, 10, 30)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 1.26, {c.C_BIDEN:27, c.C_WARREN:23,
            c.C_SANDERS:14, c.C_BUTTIGIEG:8, c.C_HARRIS:4, c.C_YANG:3,
            c.C_OROURKE:4, c.C_BENNET:1, c.C_GABBARD:2, c.C_BOOKER:1,
            c.C_KLOBUCHAR:2, c.C_CASTRO:1, c.C_STEYER:1, c.C_DELANEY:1,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:0},
            datetime.date(2019, 10, 30)),

        database.Poll(c.Q_PRIMARY, c.S_PENNSYLVANIA, 0.34, {c.C_BIDEN:30,
            c.C_WARREN:18, c.C_SANDERS:12, c.C_BUTTIGIEG:8, c.C_HARRIS:1,
            c.C_YANG:1, c.C_OROURKE:2, c.C_BENNET:2, c.C_GABBARD:2,
            c.C_BOOKER:1, c.C_KLOBUCHAR:2, c.C_CASTRO:0, c.C_STEYER:0,
            c.C_DELANEY:0, c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0,
            c.C_WILLIAMSON:0}, datetime.date(2019, 10, 31)),

        database.Poll(c.Q_PRIMARY, c.S_IOWA, 0.88, {c.C_BIDEN:17,
            c.C_WARREN:22, c.C_SANDERS:19, c.C_BUTTIGIEG:18, c.C_HARRIS:3,
            c.C_YANG:3, c.C_BENNET:0, c.C_GABBARD:2, c.C_BOOKER:2,
            c.C_KLOBUCHAR:4, c.C_CASTRO:0, c.C_STEYER:2, c.C_DELANEY:1,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:0},
            datetime.date(2019, 11, 1)),

        database.Poll(c.Q_PRIMARY, c.S_USA, 0.96, {c.C_BIDEN:33, c.C_WARREN:15,
            c.C_SANDERS:18, c.C_BUTTIGIEG:4, c.C_HARRIS:5, c.C_YANG:2,
            c.C_OROURKE:2, c.C_BENNET:0, c.C_GABBARD:2, c.C_BOOKER:3,
            c.C_KLOBUCHAR:3, c.C_CASTRO:0, c.C_STEYER:1, c.C_DELANEY:0,
            c.C_MESSAM:0, c.C_BULLOCK:0, c.C_SESTAK:0, c.C_WILLIAMSON:1},
            datetime.date(2019, 11, 1)),

        ]

    db.add_polls(polls)

    return db