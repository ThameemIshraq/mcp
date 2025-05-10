from fastmcp import FastMCP
import asyncio
import httpx
import json

async def check_mcp(mcp: FastMCP):
    # List what components were created
    tools = await mcp.get_tools()
    resources = await mcp.get_resources()
    templates = await mcp.get_resource_templates()

    print(
        f"{len(tools)} Tool(s): {', '.join([t.name for t in tools.values()])}"
    )  
    print(
        f"{len(resources)} Resource(s): {', '.join([r.name for r in resources.values()])}"
    )  
    print(
        f"{len(templates)} Resource Template(s): {', '.join([t.name for t in templates.values()])}"
    )  

    return mcp

async def load_swagger_spec(url: str) -> str:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(url)
        response.raise_for_status()  
        return response.text  

spec_str = asyncio.run(load_swagger_spec("http://userprofileservice.com/swagger/v1/swagger.json")) #This would be the api servers exposing open api definitions
jobject = json.loads(spec_str)
headers = {
    "Authorization": "Bearer XXXXX"
}
client = httpx.AsyncClient(base_url="http://localhost:5167",verify=False,headers=headers)  #base uri where the api is available
server = FastMCP.from_openapi(openapi_spec=jobject,client=client,name="User Profile")
asyncio.run(check_mcp(server))

if __name__ == "__main__":
    server.run(transport='sse')
    
