import sys
from langchain_groq import ChatGroq
from dotenv import load_dotenv

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-120b"
)
    
    
prompt = "what is python?"
response = llm.invoke(prompt)
print(response.content)
   
