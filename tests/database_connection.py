import pytest
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd
from db.connection import DatabaseConnection

# Load environment variables from a separate .env.test file
load_dotenv(dotenv_path=".env.test")

# Fixture for creating a DatabaseConnection instance
@pytest.fixture
def database_connection():
    return DatabaseConnection()

# Fixture for creating a test database engine
@pytest.fixture
def test_database_engine():
    # Fetch test database credentials from environment variables
    username = os.getenv("TEST_DB_USERNAME")
    password = os.getenv("TEST_DB_PASSWORD")
    host = os.getenv("TEST_DB_HOST")
    port = os.getenv("TEST_DB_PORT")
    database = os.getenv("TEST_DB_DATABASE")

    connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    return create_engine(connection_url)

# Test cases for the DatabaseConnection class
def test_database_connection_init(database_connection):
    assert database_connection is not None, "DatabaseConnection instance not created successfully"

def test_database_connection_connect(database_connection, test_database_engine):
    database_connection.connect()
    assert database_connection.connection is not None, "Connection not established successfully"
    database_connection.close_connection()  # Close the connection after testing

def test_database_connection_execute_query(database_connection, test_database_engine):
    # Assuming a "SELECT * FROM your_table" query for testing
    query = "SELECT * xdr_data"  # Replace 'your_table' with an actual table name
    result_df = database_connection.execute_query(query)
    assert isinstance(result_df, pd.DataFrame), "Query execution failed"

# Clean up after testing by closing the connection
def test_database_connection_close_connection(database_connection, test_database_engine):
    database_connection.connect()
    database_connection.close_connection()
    assert database_connection.connection.closed, "Connection not closed successfully"
