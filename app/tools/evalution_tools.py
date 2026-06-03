from langchain.tools import tool

@tool
def evaluate_candidate(answer: str) -> str:
    """
    Evaluate candidate answers.
    """

    response = evaluation_chain.invoke(
        {
            "answer": answer
        }
    )

    return response.content