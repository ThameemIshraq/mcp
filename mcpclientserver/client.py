import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8000/sse") 

async def main():
    async with client:
        print(f"Client connected: {client.is_connected()}")
    
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        
        resources = await client.list_resources()
        print(f"Available resources: {resources}")
        
        resourcetemplates = await client.list_resource_templates()
        print(f"Available resource templates: {resourcetemplates}")

        if any(template.name =="get_api_UserProfile" for template in resourcetemplates):
            result = await client.read_resource("resource://openapi/get_api_UserProfile/1")
            print(f"{result}")
    print(f"Client connected: {client.is_connected()}")

if __name__ == "__main__":
    asyncio.run(main())