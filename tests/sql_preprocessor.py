import pandas as pd
import numpy as np
import sqlite3
import pytest
from db.sql_preprocessor import DBFilter

# Sample data for testing
sample_data = {
    'NumericColumn1': [1, 2, 3, 4, 5],
    'NumericColumn2': [0, -1, 2, -3, 4],
    'NonNumericColumn': ['A', 'B', 'C', 'D', 'E']
}

# Create a DataFrame for testing
test_dataframe = pd.DataFrame(sample_data)

# Fixture for creating a DBFilter instance
@pytest.fixture
def db_filter_instance():
    return DBFilter(test_dataframe.copy())

# Test cases for the DBFilter class
def test_filter_numeric_columns(db_filter_instance):
    threshold = 0
    filtered_df = db_filter_instance.filter_numeric_columns(threshold)
    expected_columns = ['NumericColumn1', 'NumericColumn2']
    assert all(column in filtered_df.columns for column in expected_columns), "Numeric columns not filtered correctly"

def test_get_unique_values(db_filter_instance):
    column = 'NonNumericColumn'
    unique_values = db_filter_instance.get_unique_values(column)
    expected_values = ['A', 'B', 'C', 'D', 'E']
    assert all(value in unique_values for value in expected_values), "Unique values not retrieved correctly"

def test_most_repeated_value(db_filter_instance):
    column = 'NonNumericColumn'
    most_repeated_value = db_filter_instance.most_repeated_value(column)
    expected_value = 'A'  # Assuming 'A' is the most repeated value in the sample data
    assert most_repeated_value == expected_value, "Most repeated value not retrieved correctly"

def test_calculate_average(db_filter_instance):
    column = 'NumericColumn1'
    average_value = db_filter_instance.calculate_average(column)
    expected_average = np.mean([1, 2, 3, 4, 5])
    assert average_value == expected_average, "Average value not calculated correctly"

# Test load_data_from_db by setting up a SQLite in-memory database
def test_load_data_from_db():
    # Create an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create a test table
    cursor.execute('''CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, value INTEGER)''')

    # Insert test data
    cursor.execute('''INSERT INTO test_table (name, value) VALUES ('A', 10), ('B', 20), ('C', 30)''')

    # Commit the changes
    conn.commit()

    # Test load_data_from_db method
    db_filter_instance = DBFilter(test_dataframe.copy())
    sql_query = 'SELECT * FROM test_table'
    loaded_df = db_filter_instance.load_data_from_db(':memory:', sql_query)

    # Check if the loaded data matches the expected data
    expected_data = {'id': [1, 2, 3], 'name': ['A', 'B', 'C'], 'value': [10, 20, 30]}
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(loaded_df, expected_df)

    # Close the database connection
    conn.close()
