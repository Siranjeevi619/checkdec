from langchain.tools import tool


@tool
def job_selector(resume : str) -> str:
    """ the age which is help to find out which is the best job suits for the candidate

    Args:
        resume (str): this is content of the resume 

    Returns:
        str: return the paragraph which tells why the application choose the job which suits for the candidate resume
    """
    response = role_chain.invoke({
        "resume_content" =resume
    })
    return response.content



