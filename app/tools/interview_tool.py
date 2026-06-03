from langchain.tools import tool

@tool 
def interviewer_tool(role:str) -> str:
    """ 
     Generates the interview question for the user based on the role"""
     response = interviewer_tool.invoke({
         "job_role"=role
     })
     return response.content