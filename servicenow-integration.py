# import requests
# from langchain.schema import AIMessage, HumanMessage

# # Define the MCP Endpoint (Placeholder)
# MCP_ENDPOINT = "https://mcp-api.example.com/invoke"

# def invoke_mcp_with_github(owner: str, repo: str):
#     """Invoke MCP to fetch GitHub repo details and create an issue."""
#     messages = [
#         HumanMessage(content=f"Fetch repository details for {owner}/{repo} and generate a summary."),
#     ]

#     # Call MCP Endpoint
#     mcp_response = requests.post(MCP_ENDPOINT, json={"messages": messages})
#     return mcp_response.json()

# # Example Usage (Replace placeholders)
# OWNER = "gautamnayak247"
# REPO = "langchain"
# response = invoke_mcp_with_github(OWNER, REPO)
# print(response)


# integration with service now
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# ServiceNow instance details
HOST = os.getenv("ServiceNow_Host")
USERNAME = os.getenv("ServiceNow_Username")
PASSWORD = os.getenv("ServiceNow_Password")


def create_incident(short_description: str, category: str, impact: str, urgency: str, caller_id: str):

    url = f"https://{HOST}/api/now/table/incident"

    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {
        "short_description": short_description,
        "category": category,
        "impact": impact,
        "urgency": urgency,
        "caller_id": caller_id,
    }

    # Make API request
    response = requests.post(
        url, auth=(USERNAME, PASSWORD), headers=headers, data=json.dumps(payload)
    )

    # Handle response
    if response.status_code == 201:
        return response.json()
    else:
        return {"error": response.text}
