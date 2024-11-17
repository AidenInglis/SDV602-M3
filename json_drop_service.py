import requests
import json

class JsnDrop:
    def __init__(self, token, base_url):
        self.token = "4c78b4b2-5a72-459d-86ec-dd1bb298aa17"
        self.base_url = "https://newsimland.com/~todd/JSON/"

    def jsnDropApi(self, command):
        """
        Sends the command to the JsnDrop API.
        """
        #construct query string for the API
        query = {
            "tok": self.token,
            "cmd": command
        }

        #convert to JSON and encode to make into a URL
        query_string = f"{self.base_url}?tok={json.dumps(query)}"

        print(f"Generated URL: {query_string}")

        #send a GET request
        try:
            response = requests.get(query_string)
            if response.status_code == 200:
                return response.json()  #parse JSON response
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def create(self, table_name, example):
        """
        Creates a new table with the specified example schema.
        """
        command = {
            "CREATE": table_name,
            "EXAMPLE": example
        }
        return self.jsnDropApi(command)

    def store(self, table_name, value_list):
        """
        Stores data into the specified table.
        """
        command = {
            "STORE": table_name,
            "VALUE": value_list
        }
        return self.jsnDropApi(command)

    def all(self, table_name):
        """
        Retrieves all data from the specified table.
        """
        command = {
            "ALL": table_name
        }
        return self.jsnDropApi(command)

    def select(self, table_name, where):
        """
        Selects data from the specified table based on a WHERE clause.
        """
        command = {
            "SELECT": table_name,
            "WHERE": where
        }
        return self.jsnDropApi(command)

    def delete(self, table_name, where):
        """
        Deletes data from the specified table based on a WHERE clause.
        """
        command = {
            "DELETE": table_name,
            "WHERE": where
        }
        return self.jsnDropApi(command)

    def drop(self, table_name):
        """
        Drops the specified table.
        """
        command = {
            "DROP": table_name
        }
        return self.jsnDropApi(command)