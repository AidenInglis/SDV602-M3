import requests
import json

class JsnDrop:
    def __init__(self, tok = None, url = None) -> None:
        self.tok = tok
        self.url = url
        
        self.jsnStatus = " "
        self.jsnResult = {}

        self.decode = json.JSONDecoder().decode
        self.encode = json.JSONEncoder().encode


        self.jsnDropRecord = self.decode('{"tok":"","cmd":{}}')
        self.jsnDropCreate = self.decode('{"CREATE":"aTableName","EXAMPLE":{}}')
        self.jsnDropStore  = self.decode('{"STORE":"aTableName","VALUE":[]}')
        self.jsnDropAll    = self.decode('{"ALL":"aTableName"}')
        self.jsnDropSelect = self.decode('{"SELECT":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDelete = self.decode('{"DELETE":"aTableName","WHERE":"aField = b"}')
        self.jsnDropDrop   = self.decode('{"DROP":"aTableName"}')


    def jsnDropApi(self, command):
        api_call  = self.jsnDropRecord
        api_call["cmd"] = command
        api_call["tok"] = self.tok
        payload = {'tok': self.encode(api_call)}

        r = requests.get(self.url, payload)

        # Update the status and result
        jsnResponse = r.json()
        self.jsnStatus = jsnResponse["JsnMsg"]
        self.jsnResult = jsnResponse["Msg"]

        # Feedback to check it works
        print(f"Status = {self.jsnStatus} , Result = {self.jsnResult}")
        return self.jsnResult 



 

    def create(self, table_name, example):
        """
        Creates a new table with the specified example schema.
        """
        command = self.jsnDropCreate ={
            "CREATE": table_name,
            "EXAMPLE": example
        }
        return self.jsnDropApi(command)

    def store(self, table_name, value_list):
        """
        Stores data into the specified table.
        """
        command = self.jsnDropStore = {
            "STORE": table_name,
            "VALUE": value_list
        }
        return self.jsnDropApi(command)

    def all(self, table_name):
        """
        Retrieves all data from the specified table.
        """
        command = self.jsnDropAll = {
            "ALL": table_name
        }
        return self.jsnDropApi(command)

    def select(self, table_name, where):
        """
        Selects data from the specified table based on a WHERE clause.
        """
        command = self.jsnDropSelect = {
            "SELECT": table_name,
            "WHERE": where
        }
        return self.jsnDropApi(command)

    def delete(self, table_name, where):
        """
        Deletes data from the specified table based on a WHERE clause.
        """
        command = self.jsnDropDelete = {
            "DELETE": table_name,
            "WHERE": where
        }
        return self.jsnDropApi(command)

    def drop(self, table_name):
        """
        Drops the specified table.
        """
        command = self.jsnDropDrop = {
            "DROP": table_name
        }
        return self.jsnDropApi(command)
    


    class jsnTable(object):
        def __init__(self, jsnDrop, table_name) -> None:
            self.jsnDrop = jsnDrop
            self.table_name = table_name

        def create(self, example):
            return self.jsnDrop.create(self.table_name, example)

        def store(self, value_list):
            return self.jsnDrop.store(self.table_name, value_list)

        def all(self):
            return self.jsnDrop.all(self.table_name)

        def select(self, where):
            return self.jsnDrop.select(self.table_name, where)

        def delete(self, where):
            return self.jsnDrop.delete(self.table_name, where)

        def drop(self):
            return self.jsnDrop.drop(self.table_name)

        def __str__(self) -> str:
            return f"Table {self.table_name}"
