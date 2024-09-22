import pytest
import sqlite3

from lib.sql_queries import (
    select_all_female_bears_return_name_and_age,
    select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest,
    select_oldest_bear_and_returns_name_and_age,
    select_all_bears_names_and_orders_in_alphabetical_order
)



@pytest.fixture(scope="module")
def db_connection():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    
    with open("lib/create.sql") as f:
        cursor.executescript(f.read())
    
    with open("lib/insert.sql") as f:
        cursor.executescript(f.read())
    
    yield cursor
    
    connection.close()

def test_select_all_female_bears_return_name_and_age(db_connection):
    db_connection.execute(select_all_female_bears_return_name_and_age)
    results = db_connection.fetchall()
    assert results == [('Tabitha', 4), ('Melissa', 2), ('Wendy', 1)]

# Add more tests based on the other queries similarly
