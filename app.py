import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def run_memory_chat():
    # Load environment variables
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    confid_file = "browser_mcp.json"

    # Create MCPClient client and agent with memory enabled
    client = MCPClient.from_config_file("browser_mcp.json")
    

    # Create LLM - you can choose between different models
    llm = ChatGroq(model="qwen-qwq-32b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30, memory_enabled=True)

    print("\n====== INteractive MCP Chat ======")
    print("Type 'exit' or 'quit' to end the chat")
    print("Type 'clear' to clear the memory")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        elif user_input.lower() == "clear":
            agent.memory.clear()
            print("Memory cleared")
            continue
        
        print("\nAssistant: ", end=", flush=True")
        

    try:
        # Run a query to search for accommodations
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            elif user_input.lower() == "clear":
                agent.memory.clear()
                print("Memory cleared")
                continue
            
            print("\nAssistant: ", end=", flush=True")
                
            try:    
                response = await agent.run(user_input, max_steps=30)
                print(f"\nResult: {response}")

            except Exception as e:
                print(f"\nError: {e}")

        
    finally:
        # Ensure we clean up resources properly
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())