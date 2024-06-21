from langchain.agents import load_tools
from langchain_community.utilities.requests import JsonRequestsWrapper

requests_tools = load_tools(["requests_all"])

requests = JsonRequestsWrapper()
rval = requests.get("https://api.agify.io/?name=jackson")
print(rval)