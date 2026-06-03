from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from app.llm.llm import model
from app.prompts.prompt import prompt
from app.tools.agents_tools import tools

agent = create_tool_calling_agent(llm = model, prompt =prompt, tools = tools )
agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True)

response = agent_executor.invoke(
    {
        "input":
        f"""
        Analyze this resume and recommend suitable roles.

        {resume_content}
        """
    }
)

print(response["output"])