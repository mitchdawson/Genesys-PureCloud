from requests import Session
import json
from genesys_json import new_integration_json, new_action_json, publish_action_json, test_new_action_json

class Build(Session):

    def __init__(self, base_url, client_id, client_secret):
        # Initialise the Inherited class
        super().__init__()

        # Create our base url
        self.base_url = base_url

        # Create the client_id
        self.client_id = client_id

        # Create the client_secret
        self.client_secret = client_secret

        # Create the Access Token Place Holder
        self.access_token = None

        # Create the Integration Id Place Holder
        self.integration_id = None

        # Create the Data Action Id Place Holder
        self.data_action_id = None

        # Call self.authorise to obtain an access token for the session.
        self.authorize()
    
    # The authorize method is called automatically during initialisation. 
    # The method uses the clientid & client secret values to make a Basic auth post request 
    # against the "/oauth/token" endpoint to obtain an access token 
    # which can be used for authentication for the rest of the session.
    def authorize(self):

        # Define the Auth url
        auth_url = f"https://login.{self.base_url}/oauth/token"

        # Set the Auth Credentials
        auth = (self.client_id, self.client_secret)

        # Set the "application/x-www-form-urlencoded" Header on the Session
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        # Create the data for the Grant Type {"grant_type": "client_credentials"}
        data = {"grant_type": "client_credentials"}

        # Create the Request Object
        req = self.post(
            url=auth_url,
            auth=auth,
            headers=headers,
            data=data
        )

        # Check the status code
        if req.status_code != 200:

            # Print out the text error from the response before raising an exception.
            print("Error: ", req.text)

            # Raise an Exception and exit as we cannot continue
            raise ValueError("The Authorisation request was not successful")

        # We need to Convert the body of the request to json
        response = json.loads(req.text)

        # The access Token should be present under the following key
        access_token = response["access_token"]

        # Set the self.access_token variable to the recieved token
        self.access_token = access_token
        print("Obtained an access token for the session...")

    # Define the create_integration method
    def create_integration(self):
        print("Attempting to build a new Web Services Interaction")

        # Define the Api Url
        api_url = f"https://api.{self.base_url}/api/v2/integrations"

        # Set the "Content-Type: application/json" & "Authorization: Bearer xxx" 
        # Headers on the Session
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.access_token
        }

        # Build the json data object for the request body
        data = json.loads(new_integration_json)

        # Create the Request Object
        req = self.post(
            url=api_url,
            # headers=headers,
            data=json.dumps(data)
        )

        # Check the status code, anything other than 200 indicates a problem.
        if req.status_code != 200:

            # Print out the text error from the response before raising an exception.
            print("Error: ", req.text)
    
            # Raise an Exception and exit as we cannot continue
            raise ValueError("Unable to create a new Integration...")
        
        print("Integration created successfully...")

        # A success response would be similar to the following

        # {'id': '394eab38-cc04-459c-90ad-99974754f79e', 'name': 'Web Services Data Actions (2)', 
        # 'integrationType': {'id': 'custom-rest-actions', 
        # 'selfUri': '/api/v2/integrations/types/custom-rest-actions'}, 
        # 'notes': '', 'intendedState': 'DISABLED', 
        # 'config': {'current': {'id': 'current', 'selfUri': '/api/v2/integrations/394eab38-cc04-459c-90ad-99974754f79e/config/current'}}, 
        # 'reportedState': {'code': 'INACTIVE', 'effective': 'Inactive', 'lastUpdated': '2020-04-22T11:53:56.177Z'}, 
        # 'attributes': {}, 'selfUri': '/api/v2/integrations/394eab38-cc04-459c-90ad-99974754f79e'}
        
        # Read the json response and convert to a python dict object.
        response = json.loads(req.text)

        # Extract the Integrationid value of the newly created integration
        self.integration_id = response["id"]
        print(self.integration_id)
    
    # Update the integration and set the necessary values.
    def update_integration(self):
        print("Updating Integration")

        # Define the Api Url
        api_url = f"https://api.{self.base_url}/api/v2/integrations/{self.integration_id}/config/current"

        # Build the json data object for the request body
        data = {
            "name": "Consentec API Integration",
            "version": 1,
            "properties": {},
            "advanced": {},
            "notes": "",
            "credentials": {}
        }

        # Create the Request Object
        req = self.put(
            url=api_url,
            data=json.dumps(data)
        )

        # Check the status code, anything other than 200 indicates a problem.
        if req.status_code != 200:

            # Print out the text error from the response before raising an exception.
            print("Error: ", req.text)

            # Raise an Exception and exit as we cannot continue
            raise ValueError("Unable to update integration")

        # Patch the Integration and set the intended state to "ENABLED"

        # Define the Api Url
        api_url = f"https://api.{self.base_url}/api/v2/integrations/{self.integration_id}"
        
        # Build the json data object for the request body
        data = {
            "intendedState": "ENABLED"
        }

        # Create the "PATCH" Request Object
        req = self.patch(
            url=api_url,
            data=json.dumps(data)
        )

        # Check the status code, anything other than 200 indicates a problem.
        if req.status_code != 200:

            # Print out the text error from the response before raising an exception.
            print("Error: ", req.text)

            # Raise an Exception and exit as we cannot continue
            raise ValueError("Unable to Patch the integration")
        
        print("Integration updated successfully...")

    # Define the create_action method
    def create_action(self):
        print("Attempting to build a new Data Action")

        # Define the Api Url, the action needs to be created as draft first.
        api_url = f"https://api.{self.base_url}/api/v2/integrations/actions/drafts"

        # Build the json data object for the request body
        data = json.loads(new_action_json)

        # Update the Data Object with the integration_id value
        data["integrationId"] = self.integration_id

        # Create the Request Object
        req = self.post(
            url=api_url,
            data=json.dumps(data)
        )
        print(req.text)

        # Check the status code, anything other than 201 indicates a problem.
        if req.status_code != 201:

            # Print out the text error from the response before raising an exception.
            print("Error: ", req.text)

            # Raise an Exception and exit as we cannot continue
            raise ValueError("Unable to create a new Data Action...")
        
        print("Data Action built successfully...")

        # We need to Convert the body of the request to json
        response = json.loads(req.text)

        # Extract the Id of the newly created action
        self.data_action_id = response["id"]

    # Define the create_action method
    def test_create_action(self):
        print("Attempting to build a new Test Data Action")

        # Define the Api Url, the action needs to be created as draft first.
        api_url = f"https://api.{self.base_url}/api/v2/integrations/actions"

        # Build the json data object for the request body
        data = json.loads(test_new_action_json)

        # Update the Data Object with the integration_id value
        data["integrationId"] = self.integration_id

        # Create the Request Object
        req = self.post(
            url=api_url,
            data=json.dumps(data)
        )
        # print(req.text)

        # Check the status code, anything other than 201 indicates a problem.
        if req.status_code != 201:

            # Print out the text error from the response before raising an exception.
            print("Error: ", req.text)

            # Raise an Exception and exit as we cannot continue
            raise ValueError("Unable to create a new Data Action...")
        
        print("Data Action built successfully...")

        # We need to Convert the body of the request to json
        response = json.loads(req.text)

        # Extract the Id of the newly created action
        self.data_action_id = response["id"]

    # Publish the Draft Data Action so that it can be used.
    def publish_data_action(self):
        print("Attempting to Publish Data Action")

        # Define the Api Url, the action needs to be created as draft first.
        api_url = f"https://api.{self.base_url}/api/v2/integrations/actions/{self.data_action_id}/draft/publish"

        # Build the json data object for the request body
        # data = json.loads(publish_action_json)

        # Create the Request Object
        req = self.post(
            url=api_url,
            # data=json.dumps(data)
            data=publish_action_json
        )
        print(req.status_code)
        print(req.text)
        # Check the status code, anything other than 201 indicates a problem.
        if req.status_code != 201:

            # Print out the text error from the response before raising an exception.
            print("Error: ", req.text)

            # Raise an Exception and exit as we cannot continue
            raise ValueError("Unable to publish new Data Action...")
        
        print("Data Action Published Successfully...")



def main():

    # Define our base url
    base_url = "mypurecloud.ie"

    # Create the client_id
    client_id = "client-id"

    # Create the client_secret
    client_secret = "client-secret"

    # Instantiate the Build Class
    b = Build(base_url, client_id, client_secret)

    # Call the create_integration method to create a new integration
    # and stores its id as a variable on the class.
    b.create_integration()

    # Call the update integraton method
    b.update_integration()

    # Call the create_action  method to create a new data action
    #b.create_action()
    b.test_create_action()

    # Publish the previously created action
    b.publish_data_action()




if __name__ == "__main__":
    main()

