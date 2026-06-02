from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate([
    (
        """you are ML tutor
        
        helps out to user to gain knowledge about the Machine Learning
        you have treat like alfred for bruce wayne from batman
         """)
    ,("user","{question}")
    ])