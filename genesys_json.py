# Define the string that will form the json to create a new action. a new integration
# This is kept as a string so that formatting operations can be carried out.
new_integration_json = """
{
    "name": "Consentec new interaction",
    "integrationType": {
       "id": "custom-rest-actions",
       "name": "Consentec new interaction"
    }
 }
 """

# Define the string that will form the json to create a new action.
# This is kept as a string so that formatting operations can be carried out.
# The integrationId key has a place holder for the id of the newly created integration.
new_action_json = """
{
    "category": "Web Services Data Actions",
    "name": "Consentec Compliance Api EU Action",
    "integrationId": "",
    "config": {
       "request": {
          "requestUrlTemplate": "https://portal.consentec.net/api/v1/consent?e164=%2B${input.e164}",
          "requestTemplate": "",
          "requestTemplateUri": "",
          "requestType": "GET",
          "headers": {
            "apikey": "Y4TE2cr7DsasEBQ2+6cQRqat"
          }
       },
       "response": {
          "translationMap": {},
          "translationMapDefaults": {},
          "successTemplate": "",
          "successTemplateUri": ""
       }
    },
    "contract": {
       "input": {
          "inputSchema": {
             "id": "",
             "$schema": "",
             "title": "Consentec Compliance Api",
             "description": "",
             "type": "object",
             "required": ["e164"],
             "properties": {
                 "e164": {
                "type": "string"
                }
            },
             "additionalProperties": true
          }
       },
       "output": {
          "successSchema": {
            "title": "Response",
            "type": "object",
            "required": [
              "status",
              "match"
            ],
            "properties": {
              "status": {
                "type": "integer"
              },
              "match": {
                "type": "integer"
              },
              "result": {
                "type": "object",
                "required": [
                  "compliance",
                  "continentCode",
                  "continent",
                  "isoAlpha2",
                  "isoAlpha3",
                  "isoNum",
                  "country",
                  "regionName",
                  "regionCode",
                  "complianceType",
                  "complianceDetail"
                ],
                "properties": {
                  "compliance": {
                    "type": "integer"
                  },
                  "continentCode": {
                    "type": "string"
                  },
                  "continent": {
                    "type": "string"
                  },
                  "isoAlpha2": {
                    "type": "string"
                  },
                  "isoAlpha3": {
                    "type": "string"
                  },
                  "isoNum": {
                    "type": "string"
                  },
                  "country": {
                    "type": "string"
                  },
                  "regionName": {
                    "type": "string"
                  },
                  "regionCode": {
                    "type": "string"
                  },
                  "complianceType": {
                    "type": "string"
                  },
                  "complianceDetail": {
                    "type": "string"
                  }
                },
                "additionalProperties": true
                }
            },
            "additionalProperties": true
        }
       }
    },
    "secure": true
 }
 """
# Test new action minus some values
test_new_action_json = """
{
    "category": "Web Services Data Actions",
    "name": "Consentec Compliance Api EU Action",
    "integrationId": "",
    "config": {
       "request": {
          "requestUrlTemplate": "https://portal.consentec.net/api/v1/consent?e164=%2B${input.e164}",
          "requestTemplate": "",
          "requestTemplateUri": "",
          "requestType": "GET",
          "headers": {
            "apikey": "Y4TE2cr7DsasEBQ2+6cQRqat"
          }
       },
       "response": {
          "translationMap": {},
          "translationMapDefaults": {},
          "successTemplate": "",
          "successTemplateUri": ""
       }
    },
    "contract": {
       "input": {
          "inputSchema": {
             "title": "Consentec Compliance Api",
             "description": "",
             "type": "object",
             "required": ["e164"],
             "properties": {
                 "e164": {
                "type": "string"
                }
            },
             "additionalProperties": true
          }
       },
       "output": {
          "successSchema": {
            "title": "Response",
            "type": "object",
            "required": [
              "status",
              "match"
            ],
            "properties": {
              "status": {
                "type": "integer"
              },
              "match": {
                "type": "integer"
              },
              "result": {
                "type": "object",
                "required": [
                  "compliance",
                  "continentCode",
                  "continent",
                  "isoAlpha2",
                  "isoAlpha3",
                  "isoNum",
                  "country",
                  "regionName",
                  "regionCode",
                  "complianceType",
                  "complianceDetail"
                ],
                "properties": {
                  "compliance": {
                    "type": "integer"
                  },
                  "continentCode": {
                    "type": "string"
                  },
                  "continent": {
                    "type": "string"
                  },
                  "isoAlpha2": {
                    "type": "string"
                  },
                  "isoAlpha3": {
                    "type": "string"
                  },
                  "isoNum": {
                    "type": "string"
                  },
                  "country": {
                    "type": "string"
                  },
                  "regionName": {
                    "type": "string"
                  },
                  "regionCode": {
                    "type": "string"
                  },
                  "complianceType": {
                    "type": "string"
                  },
                  "complianceDetail": {
                    "type": "string"
                  }
                },
                "additionalProperties": true
                }
            },
            "additionalProperties": true
        }
       }
    },
    "secure": true
 }
 """

publish_action_json = """
{"version": 1}
"""

test_action_json = """
{
    "category": "Web Services Data Actions",
    "name": "Consentec Compliance Api EU Action",
    "integrationId": "2f98c500-262d-4fad-8298-879b19cad4f2",
    "config": {
       "request": {
          "requestUrlTemplate": "https://portal.consentec.net/api/v1/consent?e164=%2B${input.e164}",
          "requestTemplate": "",
          "requestTemplateUri": "",
          "requestType": "GET",
          "headers": {
            "apikey": "Y4TE2cr7DsasEBQ2+6cQRqat"
          }
       },
       "response": {
          "translationMap": {},
          "translationMapDefaults": {},
          "successTemplate": "",
          "successTemplateUri": ""
       }
    },
    "contract": {
       "input": {
          "inputSchema": {
             "id": "",
             "$schema": "",
             "title": "Consentec Compliance Api",
             "description": "",
             "type": "object",
             "required": [],
             "properties": {},
            },
            "additionalProperties": true
          }
       },
       "output": {
          "successSchema": {
            "title": "Response",
            "type": "object",
            "required": [
              "status",
              "match"
            ],
            "properties": {
              "status": {
                "type": "integer"
              },
              "match": {
                "type": "integer"
              },
              "result": {
                "type": "object",
                "required": [
                  "compliance",
                  "continentCode",
                  "continent",
                  "isoAlpha2",
                  "isoAlpha3",
                  "isoNum",
                  "country",
                  "regionName",
                  "regionCode",
                  "complianceType",
                  "complianceDetail"
                ],
                "properties": {
                  "compliance": {
                    "type": "integer"
                  },
                  "continentCode": {
                    "type": "string"
                  },
                  "continent": {
                    "type": "string"
                  },
                  "isoAlpha2": {
                    "type": "string"
                  },
                  "isoAlpha3": {
                    "type": "string"
                  },
                  "isoNum": {
                    "type": "string"
                  },
                  "country": {
                    "type": "string"
                  },
                  "regionName": {
                    "type": "string"
                  },
                  "regionCode": {
                    "type": "string"
                  },
                  "complianceType": {
                    "type": "string"
                  },
                  "complianceDetail": {
                    "type": "string"
                  }
                },
                "additionalProperties": true
                }
            },
            "additionalProperties": true
        }
       }
    },
    "secure": true
 }
 """
