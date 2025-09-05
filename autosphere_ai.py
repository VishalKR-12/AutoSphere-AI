#!/usr/bin/env python3
"""
AutoSphere AI: Automate, Assist, Achieve
Standalone Python script version of the AI agent
"""

import os
import getpass
import requests
from langchain_ibm import ChatWatsonx
from ibm_watsonx_ai import APIClient
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from ibm_watsonx_ai.foundation_models.utils import Tool, Toolkit
from ibm_watsonx_ai.deployments import RuntimeContext
from langchain_core.tools import StructuredTool
import json

class AutoSphereAI:
    def __init__(self, api_key=None, project_id=None):
        """Initialize AutoSphere AI with credentials"""
        self.api_key = api_key
        self.project_id = project_id
        self.client = None
        self.agent = None
        self.initialized = False
        
        if api_key and project_id:
            self.initialize()
    
    def get_credentials(self):
        """Get IBM Cloud credentials from environment or user input"""
        if self.api_key and self.project_id:
            return {
                "url": "https://us-south.ml.cloud.ibm.com",
                "apikey": self.api_key
            }
        
        print("🔐 AutoSphere AI - IBM Cloud Authentication")
        print("=" * 50)
        
        return {
            "url": "https://us-south.ml.cloud.ibm.com",
            "apikey": getpass.getpass("Please enter your IBM Cloud API key: ")
        }

    def get_project_id(self):
        """Get project ID from environment or user input"""
        if self.project_id:
            return self.project_id
        return getpass.getpass("Please enter your project ID: ")

    def validate_api_key(self, apikey):
        """Check if the given API key is valid by trying to fetch a Bearer token."""
        url = "https://iam.cloud.ibm.com/identity/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={apikey}"

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            token = response.json().get("access_token")
            if token:
                return True, token
        return False, None

    def create_utility_agent_tool(self, tool_name, params, api_client, **kwargs):
        """Create utility agent tool"""
        utility_agent_tool = Toolkit(api_client=api_client).get_tool(tool_name)
        tool_description = utility_agent_tool.get("description")

        if kwargs.get("tool_description"):
            tool_description = kwargs.get("tool_description")
        elif utility_agent_tool.get("agent_description"):
            tool_description = utility_agent_tool.get("agent_description")
        
        tool_schema = utility_agent_tool.get("input_schema")
        if tool_schema is None:
            tool_schema = {
                "type": "object",
                "additionalProperties": False,
                "$schema": "http://json-schema.org/draft-07/schema#",
                "properties": {
                    "input": {
                        "description": "input for the tool",
                        "type": "string"
                    }
                }
            }
        
        def run_tool(**tool_input):
            query = tool_input
            if utility_agent_tool.get("input_schema") is None:
                query = tool_input.get("input")

            results = utility_agent_tool.run(input=query, config=params)
            return results.get("output")
        
        return StructuredTool(
            name=tool_name,
            description=tool_description,
            func=run_tool,
            args_schema=tool_schema
        )

    def create_tools(self, client):
        """Create all available tools"""
        tools = []
        
        # Google Search
        tools.append(self.create_utility_agent_tool("GoogleSearch", None, client))
        
        # Web Crawler
        tools.append(self.create_utility_agent_tool("WebCrawler", {}, client))
        
        # Wikipedia
        tools.append(self.create_utility_agent_tool("Wikipedia", {"maxResults": 5}, client))
        
        # DuckDuckGo
        tools.append(self.create_utility_agent_tool("DuckDuckGo", {}, client))
        
        # Weather
        tools.append(self.create_utility_agent_tool("Weather", {}, client))

        return tools

    def create_chat_model(self, credentials, project_id, client):
        """Create the chat model"""
        model_id = "ibm/granite-3-3-8b-instruct"
        parameters = {
            "frequency_penalty": 0,
            "max_tokens": 2000,
            "presence_penalty": 0,
            "temperature": 0,
            "top_p": 1
        }
        
        chat_model = ChatWatsonx(
            model_id=model_id,
            url=credentials["url"],
            project_id=project_id,
            params=parameters,
            watsonx_client=client,
        )
        return chat_model

    def create_agent(self, credentials, project_id, client):
        """Create the AutoSphere AI agent"""
        print("🤖 Creating AutoSphere AI Agent...")
        
        # Create chat model
        chat_model = self.create_chat_model(credentials, project_id, client)
        
        # Create tools
        tools = self.create_tools(client)
        
        # Create memory
        memory = MemorySaver()
        
        # Custom instructions for India-centric focus
        instructions = """You are a helpful assistant that uses tools to answer questions in detail.
When greeted, say "Hi, I am AutoSphere AI. How can I help you?"
Always leverage IBM Granite models for reasoning, summarization, and translation.
Preprocess and clean input using IBM preprocessing toolkits before generating responses.
Use Retrieval-Augmented Generation (RAG) to provide grounded, factual answers.
Orchestrate workflows with the IBM Agent Development Kit (ADK) for full automation.
Ensure solutions are end-to-end (automate, assist, and optimize tasks fully).
Focus on India-centric and socially impactful applications (agriculture, healthcare, education, etc.).
Always explain the value proposition (how it helps save time, improve efficiency, or reduce costs).
Demonstrate answers in a clear, structured, and actionable way.
If unsure of an answer: say "I don't have that exact information, but I can suggest alternatives or direct you to reliable sources."
If a query is incomplete: say "Can you provide more details so I can give you the most accurate response?"
Never provide misleading or fabricated data.
Always highlight social good and economic growth impact.
Whenever possible, recommend automation workflows rather than manual steps.
Suggest interdisciplinary collaboration if relevant (e.g., healthcare + AI, agriculture + IoT)."""

        # Use "prompt" instead of "state_modifier" as per the working notebook
        agent = create_react_agent(chat_model, tools=tools, checkpointer=memory, prompt=instructions)
        return agent

    def convert_messages(self, messages):
        """Convert messages to LangChain format"""
        converted_messages = []
        for message in messages:
            if message["role"] == "user":
                converted_messages.append(HumanMessage(content=message["content"]))
            elif message["role"] == "assistant":
                converted_messages.append(AIMessage(content=message["content"]))
        return converted_messages

    def initialize(self):
        """Initialize the AI agent"""
        try:
            # Get credentials
            credentials = self.get_credentials()
            
            # Validate API key
            is_valid, token = self.validate_api_key(credentials["apikey"])
            if not is_valid:
                print("❌ Invalid API Key. Please check and try again.")
                return False
            
            print("✅ API Key is valid. Token generated successfully.")
            
            # Get project ID
            project_id = self.get_project_id()
            if not project_id.strip():
                print("❌ Project ID is required. Please try again.")
                return False
            
            print("✅ Project ID set successfully")
            
            # Create API client
            self.client = APIClient(credentials=credentials, project_id=project_id)
            
            # Create agent
            self.agent = self.create_agent(credentials, project_id, self.client)
            
            print("✅ AutoSphere AI Agent created successfully!")
            self.initialized = True
            return True
            
        except Exception as e:
            print(f"❌ Failed to initialize AutoSphere AI: {str(e)}")
            return False

    def process_message(self, message, conversation_history=None):
        """Process a message and return AI response"""
        if not self.initialized:
            return "Sorry, the AI service is not initialized. Please check your configuration."
        
        try:
            # Convert conversation history to LangChain format
            if conversation_history:
                messages = self.convert_messages(conversation_history)
            else:
                messages = [HumanMessage(content=message)]
            
            # Generate response
            generated_response = self.agent.invoke(
                {"messages": messages},
                {"configurable": {"thread_id": "42"}}
            )
            
            # Extract agent's reply
            result = generated_response["messages"][-1].content
            return result
            
        except Exception as e:
            print(f"❌ Error processing message: {str(e)}")
            return "Sorry, I encountered an error while processing your message. Please try again."

    def run_interactive(self):
        """Run interactive command-line interface"""
        if not self.initialized:
            if not self.initialize():
                return
        
        print("🎯 Ready to assist with automation, assistance, and achievement!")
        print("=" * 50)
        
        # Continuous chatbot loop with memory
        print("Hi, I am AutoSphere AI. How can I help you?")
        print("(Type 'exit' or 'end' to quit)\n")
        
        conversation_history = []  # store conversation context
        
        while True:
            try:
                question = input("Question: ")
                
                # Exit condition
                if question.strip().lower() in ["exit", "end", "quit", "bye"]:
                    print("Goodbye! Have a great day 🙂")
                    break
                
                if not question.strip():
                    continue
                
                # Add user message
                conversation_history.append({"role": "user", "content": question})
                
                # Generate response
                response = self.process_message(question, conversation_history)
                print(f"\nAutoSphere AI: {response}\n")
                
                # Add assistant message to history
                conversation_history.append({"role": "assistant", "content": response})
                
            except KeyboardInterrupt:
                print("\n👋 Thank you for using AutoSphere AI!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")
                print("Please try again or type 'exit' to quit.")

def main():
    """Main function to run AutoSphere AI"""
    print("🚀 AutoSphere AI: Automate, Assist, Achieve")
    print("=" * 50)
    print("India-Centric AI Automation Platform")
    print("Built with IBM Watson AI & LangGraph")
    print("=" * 50)
    
    # Create AI instance
    ai = AutoSphereAI()
    
    # Run interactive mode
    ai.run_interactive()

if __name__ == "__main__":
    main()


