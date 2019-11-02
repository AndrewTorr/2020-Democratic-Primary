"""Creates a database and populates it with basic initial datapoints."""

import database
import datetime
import collect.polls
import collect.process_polls
import simulate.state_similarities as ss
import constants as c

def populate():
    # Instantiate an empty database.
    db = database.Database()

    # Add the state and territory data, columns are as follows:
    # PEP 8 limits lines to 79 characters but data is formatted as a table here for clarity.
    # Name, PVI, electors, pchispanic, pcwhite, pcblack, pcasian, pcnative, status, elasticity, pop1000s, date of primary/caucus, pledged delegates in democratic primary, region in the USA.
    db.add_state(database.State(c.S_ALABAMA,                    14,     9,      4.1,    65.5,   26.7,   1.3,    0.5,    c.T_STATE       ,   0.89,   4888,   datetime.date(2019, 3, 3),  52,     c.R_SOUTH))
    db.add_state(database.State(c.S_ALASKA,                     9,      3,      7.0,    60.6,   2.9,    6.6,    14.2,   c.T_STATE       ,   1.16,   737,    datetime.date(2019, 4, 4),  14,     c.R_PACIFIC))
    # Territories are included as although they do not vote in presidential elections, they do in the Democratic Primary.
    db.add_state(database.State(c.S_AMERICAN_SAMOA,             0,      0,      0,      0,      0,      0,      0,      c.T_TERRITORY   ,   1.00,   56,     datetime.date(2019, 3, 3),  6,      c.R_PACIFIC))
    db.add_state(database.State(c.S_ARIZONA,                    3,      11,     31.4,   54.7,   4.1,    3.2,    3.9,    c.T_STATE       ,   1.05,   7172,   datetime.date(2019, 3, 17), 67,     c.R_WEST))
    db.add_state(database.State(c.S_ARKANSAS,                   15,     6,      7.4,    72.3,   15.2,   1.6,    0.6,    c.T_STATE       ,   1.00,   3014,   datetime.date(2019, 3, 3),  31,     c.R_SOUTH))
    db.add_state(database.State(c.S_CALIFORNIA,                 -12,    55,     39.1,   37.0,   5.5,    14.4,   0.4,    c.T_STATE       ,   0.94,   39557,  datetime.date(2019, 3, 3),  417,    c.R_WEST))
    db.add_state(database.State(c.S_COLORADO,                   -2,     9,      21.5,   68.2,   3.9,    3.1,    0.6,    c.T_STATE       ,   1.07,   5696,   datetime.date(2019, 3, 3),  67,     c.R_WEST))
    db.add_state(database.State(c.S_CONNETICUT,                 -6,     7,      16.1,   66.7,   9.9,    4.5,    0.2,    c.T_STATE       ,   0.99,   3573,   datetime.date(2019, 4, 28), 49,     c.R_NORTH))
    db.add_state(database.State(c.S_DELAWARE,                   -7,     3,      9.3,    62.2,   21.5,   4.0,    0.2,    c.T_STATE       ,   0.93,   967,    datetime.date(2019, 4, 28), 17,     c.R_SOUTH))
    # Democrats Abroad have a primary and delegates of their own.
    db.add_state(database.State(c.S_DEMOCRATS_ABROAD,           0,      0,      0,      0,      0,      0,      0,      c.T_ORG         ,   None,   None,   datetime.date(2019, 3, 3),  13,     c.R_WORLD))
    # DC gets its own status as it does get to send electors to the electoral college, but is not technically a state.
    db.add_state(database.State(c.S_DC,                         -43,    3,      11.0,   36.5,   45.3,   4.0,    0.2,    c.T_DC          ,   0.80,   702,    datetime.date(2019, 6, 16), 17,     c.R_SOUTH))
    db.add_state(database.State(c.S_FLORIDA,                    2,      29,     25.6,   53.8,   15.4,   2.8,    0.2,    c.T_STATE       ,   1.03,   21299,  datetime.date(2019, 3, 17), 219,    c.R_SOUTH))
    db.add_state(database.State(c.S_GEORGIA,                    5,      16,     9.6,    52.6,   31.1,   3.9,    0.2,    c.T_STATE       ,   0.90,   10519,  datetime.date(2019, 3, 24), 105,    c.R_SOUTH))
    db.add_state(database.State(c.S_GUAM,                       0,      0,      0,      0,      0,      0,      0,      c.T_TERRITORY   ,   1.00,   166,    datetime.date(2019, 5, 2),  6,      c.R_PACIFIC))
    db.add_state(database.State(c.S_HAWAII,                     -18,    4,      10.5,   21.8,   1.6,    37.3,   0.1,    c.T_STATE       ,   1.07,   1420,   datetime.date(2019, 4, 4),  22,     c.R_PACIFIC))
    db.add_state(database.State(c.S_IDAHO,                      19,     4,      12.4,   82.0,   0.6,    1.3,    1.1,    c.T_STATE       ,   1.12,   1754,   datetime.date(2019, 3, 10), 20,     c.R_WEST))
    db.add_state(database.State(c.S_ILLINOIS,                   -7,     20,     17.2,   61.2,   14.0,   5.4,    0.1,    c.T_STATE       ,   1.01,   12741,  datetime.date(2019, 3, 17), 155,    c.R_MIDWEST))
    db.add_state(database.State(c.S_INDIANA,                    9,      11,     6.9,    79.2,   9.2,    2.2,    0.1,    c.T_STATE       ,   0.99,   6692,   datetime.date(2019, 5, 5),  70,     c.R_MIDWEST))
    db.add_state(database.State(c.S_IOWA,                       3,      6,      5.9,    85.9,   3.3,    2.6,    0.2,    c.T_STATE       ,   1.08,   3156,   datetime.date(2019, 2, 3),  41,     c.R_MIDWEST))
    db.add_state(database.State(c.S_KANSAS,                     13,     6,      11.9,   75.9,   5.5,    2.9,    0.6,    c.T_STATE       ,   1.00,   2912,   datetime.date(2019, 5, 2),  33,     c.R_MIDWEST))
    db.add_state(database.State(c.S_KENTUCKY,                   15,     8,      3.5,    84.6,   8.0,    1.4,    0.2,    c.T_STATE       ,   0.94,   4468,   datetime.date(2019, 5, 19), 46,     c.R_SOUTH))
    db.add_state(database.State(c.S_LOUISIANA,                  11,     8,      5.2,    58.5,   32.1,   1.8,    0.5,    c.T_STATE       ,   0.96,   4660,   datetime.date(2019, 4, 4),  50,     c.R_SOUTH))
    # Maine and Nebraska split their electoral votes so the states and each of their congressional districts get their own statuses.
    db.add_state(database.State(c.S_MAINE,                      -3,     2,      1.6,    93.4,   1.2,    1.1,    0.6,    c.T_STATE       ,   1.13,   1338,   datetime.date(2019, 3, 3),  24,     c.R_NORTH))
    db.add_state(database.State(c.S_MAINE1,                     -8,     1,      1.9,    94.4,   1.7,    1.6,    0.4,    c.T_DISTRICT    ,   1.13,   673,    None,                       None,   c.R_NORTH))
    db.add_state(database.State(c.S_MAINE2,                     2,      1,      1.4,    97.2,   0.8,    0.6,    0.1,    c.T_DISTRICT    ,   1.13,   665,    None,                       None,   c.R_NORTH))
    db.add_state(database.State(c.S_MARYLAND,                   -12,    10,     10.1,   50.7,   29.4,   6.4,    0.2,    c.T_STATE       ,   0.96,   6043,   datetime.date(2019, 4, 28), 79,     c.R_SOUTH))
    db.add_state(database.State(c.S_MASSACHUSETTS,              -12,    11,     11.8,   71.5,   7.0,    6.6,    0.1,    c.T_STATE       ,   1.15,   6902,   datetime.date(2019, 3, 3),  91,     c.R_NORTH))
    db.add_state(database.State(c.S_MICHIGAN,                   -1,     16,     5.1,    75.0,   13.6,   3.1,    0.5,    c.T_STATE       ,   1.07,   9996,   datetime.date(2019, 3, 10), 125,    c.R_MIDWEST))
    db.add_state(database.State(c.S_MINNESOTA,                  -2,     10,     5.3,    79.9,   6.4,    4.9,    1.0,    c.T_STATE       ,   1.03,   5611,   datetime.date(2019, 3, 3),  75,     c.R_MIDWEST))
    db.add_state(database.State(c.S_MISSISSIPPI,                9,      6,      2.9,    56.6,   37.9,   0.9,    0.4,    c.T_STATE       ,   0.92,   2987,   datetime.date(2019, 3, 10), 36,     c.R_SOUTH))
    db.add_state(database.State(c.S_MISSOURI,                   9,      10,     4.2,    79.4,   11.4,   2.0,    0.3,    c.T_STATE       ,   0.95,   6126,   datetime.date(2019, 3, 10), 68,     c.R_MIDWEST))
    db.add_state(database.State(c.S_MONTANA,                    11,     3,      3.7,    86.3,   0.4,    0.7,    5.9,    c.T_STATE       ,   1.07,   1062,   datetime.date(2019, 6, 2),  16,     c.R_WEST))
    db.add_state(database.State(c.S_NEBRASKA,                   14,     2,      10.9,   79.0,   4.5,    2.4,    0.7,    c.T_STATE       ,   1.01,   1929,   datetime.date(2019, 5, 12), 25,     c.R_MIDWEST))
    db.add_state(database.State(c.S_NEBRASKA1,                  11,     1,      9.0,    85.5,   2.7,    2.7,    0.1,    c.T_DISTRICT    ,   1.01,   647,    None,                       None,   c.R_MIDWEST))
    db.add_state(database.State(c.S_NEBRASKA2,                  4,      1,      10.9,   76.6,   9.0,    3.5,    0.1,    c.T_DISTRICT    ,   1.01,   649,    None,                       None,   c.R_MIDWEST))
    db.add_state(database.State(c.S_NEBRASKA3,                  27,     1,      11.3,   87.0,   1.1,    0.6,    0.1,    c.T_DISTRICT    ,   1.01,   633,    None,                       None,   c.R_MIDWEST))
    db.add_state(database.State(c.S_NEVADA,                     -2,     6,      28.8,   48.8,   8.9,    8.3,    0.9,    c.T_STATE       ,   1.08,   3034,   datetime.date(2019, 2, 22), 36,     c.R_WEST))
    db.add_state(database.State(c.S_NEW_HAMPSHIRE,              0,      4,      3.8,    90.3,   1.3,    2.7,    0.1,    c.T_STATE       ,   1.15,   1356,   datetime.date(2019, 2, 11), 24,     c.R_NORTH))
    db.add_state(database.State(c.S_NEW_JERSEY,                 -8,     14,     20.4,   54.8,   12.8,   9.8,    0.1,    c.T_STATE       ,   1.01,   8909,   datetime.date(2019, 6, 2),  107,    c.R_NORTH))
    db.add_state(database.State(c.S_NEW_MEXICO,                 -4,     5,      48.8,   37.4,   1.8,    1.3,    8.8,    c.T_STATE       ,   1.02,   2095,   datetime.date(2019, 6, 2),  29,     c.R_WEST))
    db.add_state(database.State(c.S_NEW_YORK,                   -12,    29,     19.2,   55.1,   14.3,   8.7,    0.2,    c.T_STATE       ,   0.97,   19542,  datetime.date(2019, 4, 28), 224,    c.R_NORTH))
    db.add_state(database.State(c.S_NORTH_CAROLINA,             3,      15,     9.4,    63.0,   21.2,   2.9,    1.1,    c.T_STATE       ,   1.00,   10384,  datetime.date(2019, 3, 3),  110,    c.R_SOUTH))
    db.add_state(database.State(c.S_NORTH_DAKOTA,               17,     3,      3.5,    84.4,   3.0,    1.7,    5.4,    c.T_STATE       ,   0.98,   760,    datetime.date(2019, 3, 10), 14,     c.R_MIDWEST))
    db.add_state(database.State(c.S_NORTHERN_MARIANA_ISLANDS,   0,      0,      0,      0,      0,      0,      0,      c.T_TERRITORY   ,   1.00,   55,     datetime.date(2019, 3, 14), 6,      c.R_PACIFIC))
    db.add_state(database.State(c.S_OHIO,                       5,      18,     3.7,    78.9,   12.2,   2.2,    0.2,    c.T_STATE       ,   1.02,   11689,  datetime.date(2019, 3, 17), 136,    c.R_MIDWEST))
    db.add_state(database.State(c.S_OKLAHOMA,                   20,     7,      10.6,   65.6,   7.2,    2.1,    7.3,    c.T_STATE       ,   0.94,   3943,   datetime.date(2019, 3, 3),  37,     c.R_SOUTH))
    db.add_state(database.State(c.S_OREGON,                     -6,     7,      13.1,   75.6,   1.8,    4.3,    0.9,    c.T_STATE       ,   1.00,   4191,   datetime.date(2019, 5, 19), 52,     c.R_WEST))
    db.add_state(database.State(c.S_PENNSYLVANIA,               0,      20,     7.3,    76.4,   10.7,   3.5,    0.1,    c.T_STATE       ,   1.00,   12807,  datetime.date(2019, 4, 28), 153,    c.R_NORTH))
    db.add_state(database.State(c.S_PUERTO_RICO,                0,      0,      0,      0,      0,      0,      0,      c.T_TERRITORY   ,   1.00,   3195,   datetime.date(2019, 3, 29), 51,     c.R_SOUTH))
    db.add_state(database.State(c.S_RHODE_ISLAND,               -10,    4,      15.4,   72.1,   5.4,    3.6,    0.3,    c.T_STATE       ,   1.15,   1057,   datetime.date(2019, 4, 28), 21,     c.R_NORTH))
    db.add_state(database.State(c.S_SOUTH_CAROLINA,             8,      9,      5.7,    63.6,   26.8,   1.5,    0.2,    c.T_STATE       ,   0.97,   5084,   datetime.date(2019, 2, 28), 54,     c.R_SOUTH))
    db.add_state(database.State(c.S_SOUTH_DAKOTA,               14,     3,      3.6,    82.3,   1.9,    1.2,    8.6,    c.T_STATE       ,   1.01,   882,    datetime.date(2019, 6, 2),  14,     c.R_MIDWEST))
    db.add_state(database.State(c.S_TENNESSEE,                  14,     11,     5.4,    73.9,   16.6,   1.8,    0.2,    c.T_STATE       ,   0.98,   6770,   datetime.date(2019, 3, 3),  64,     c.R_SOUTH))
    db.add_state(database.State(c.S_TEXAS,                      7,      38,     39.4,   41.9,   11.8,   4.8,    0.3,    c.T_STATE       ,   1.03,   28702,  datetime.date(2019, 3, 3),  228,    c.R_SOUTH))
    db.add_state(database.State(c.S_US_VIRGIN_ISLANDS,          0,      0,      0,      0,      0,      0,      0,      c.T_TERRITORY   ,   1.00,   105,    datetime.date(2019, 6, 6),  6,      c.R_SOUTH))
    db.add_state(database.State(c.S_UTAH,                       20,     6,      14.0,   78.3,   1.2,    2.4,    1.0,    c.T_STATE       ,   1.06,   3161,   datetime.date(2019, 3, 3),  29,     c.R_WEST))
    db.add_state(database.State(c.S_VERMONT,                    -15,    3,      1.9,    92.8,   1.2,    1.8,    0.3,    c.T_STATE       ,   1.12,   626,    datetime.date(2019, 3, 3),  16,     c.R_NORTH))
    db.add_state(database.State(c.S_VIRGINIA,                   -2,     13,     9.3,    61.7,   18.8,   6.4,    0.2,    c.T_STATE       ,   0.94,   8518,   datetime.date(2019, 3, 3),  99,     c.R_SOUTH))
    db.add_state(database.State(c.S_WASHINGTON,                 -7,     12,     12.7,   68.6,   3.5,    8.5,    1.0,    c.T_STATE       ,   1.00,   7536,   datetime.date(2019, 3, 10), 89,     c.R_WEST))
    db.add_state(database.State(c.S_WEST_VIRGINIA,              19,     5,      1.3,    92.0,   3.9,    0.8,    0.1,    c.T_STATE       ,   1.04,   1806,   datetime.date(2019, 5, 12), 24,     c.R_SOUTH))
    db.add_state(database.State(c.S_WISCONSIN,                  0,      10,     6.9,    81.2,   6.3,    2.7,    0.8,    c.T_STATE       ,   1.07,   5814,   datetime.date(2019, 4, 7),  77,     c.R_MIDWEST))
    db.add_state(database.State(c.S_WYOMING,                    25,     3,      10.0,   84.0,   0.9,    0.8,    2.1,    c.T_STATE       ,   1.08,   578,    datetime.date(2019, 4, 4),  13,     c.R_WEST))

    # Add all the primary dates to the primary calendar.
    db.primary_calendar = []
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 2, 3), [c.S_IOWA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 2, 11), [c.S_NEW_HAMPSHIRE]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 2, 22), [c.S_NEVADA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 2, 28), [c.S_SOUTH_CAROLINA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 3, 3), [c.S_ALABAMA, c.S_ARKANSAS, c.S_CALIFORNIA, c.S_COLORADO, c.S_MAINE, c.S_MASSACHUSETTS, c.S_MINNESOTA, c.S_NORTH_CAROLINA,
                                                                         c.S_OKLAHOMA, c.S_TENNESSEE, c.S_TEXAS, c.S_UTAH, c.S_VERMONT, c.S_VIRGINIA, c.S_AMERICAN_SAMOA, c.S_DEMOCRATS_ABROAD]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 3, 10), [c.S_IDAHO, c.S_MICHIGAN, c.S_MISSISSIPPI, c.S_MISSOURI, c.S_WASHINGTON, c.S_NORTH_DAKOTA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 3, 14), [c.S_NORTHERN_MARIANA_ISLANDS]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 3, 17), [c.S_ARIZONA, c.S_FLORIDA, c.S_ILLINOIS, c.S_OHIO]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 3, 24), [c.S_GEORGIA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 3, 29), [c.S_PUERTO_RICO]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 4, 4), [c.S_ALASKA, c.S_HAWAII, c.S_LOUISIANA, c.S_WYOMING]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 4, 7), [c.S_WISCONSIN]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 4, 28), [c.S_CONNETICUT, c.S_DELAWARE, c.S_MARYLAND, c.S_NEW_YORK, c.S_PENNSYLVANIA, c.S_RHODE_ISLAND]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 5, 2), [c.S_KANSAS, c.S_GUAM]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 5, 5), [c.S_INDIANA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 5, 12), [c.S_NEBRASKA, c.S_WEST_VIRGINIA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 5, 19), [c.S_KENTUCKY, c.S_OREGON]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 6, 2), [c.S_MONTANA, c.S_NEW_JERSEY, c.S_NEW_MEXICO, c.S_SOUTH_DAKOTA]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 6, 6), [c.S_US_VIRGIN_ISLANDS]))
    db.add_primary_date(database.PrimaryDate(datetime.date(2019, 5, 16), [c.S_DC]))

    # Add a list of candidates in the Democratic Primary.
    db.set_primary_candidates([c.C_BIDEN, c.C_WARREN, c.C_SANDERS,
                               c.C_BUTTIGIEG, c.C_HARRIS, c.C_YANG,
                               c.C_BENNET, c.C_GABBARD, c.C_BOOKER,
                               c.C_KLOBUCHAR, c.C_CASTRO, c.C_STEYER,
                               c.C_DELANEY, c.C_MESSAM, c.C_BULLOCK,
                               c.C_SESTAK, c.C_WILLIAMSON])

    # Add the polls to the database, then average them and attach them to states or the national environment as appropriate.
    db = collect.polls.add_to_database(db)
    db = collect.process_polls.attach_primary_polls_to_states(db)

    # Add the state similarity matrices to the database.
    db = ss.save_state_similarities(db)

    return db