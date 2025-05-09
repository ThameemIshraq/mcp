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
    )  # Should include createPet
    print(
        f"{len(resources)} Resource(s): {', '.join([r.name for r in resources.values()])}"
    )  # Should include listPets
    print(
        f"{len(templates)} Resource Template(s): {', '.join([t.name for t in templates.values()])}"
    )  # Should include getPet

    return mcp

async def load_swagger_spec(url: str) -> str:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(url)
        response.raise_for_status()  
        return response.text  

spec_str = asyncio.run(load_swagger_spec("http://localhost:5167/swagger/v1/swagger.json"))
jobject = json.loads(spec_str)
headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImF0LTE2MjQ4Njg3MjkiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiI4ZmM4MTlhYS1kZTkyLTQwMTAtYTEzYi1hZTE5NzEyMTI2ZGUiLCJzdWJ0eXBlIjoiYXBwIiwidHR5IjoiYXQiLCJqdGkiOiIzZDI4ZTBjMC01OWVjLTQ3ZjQtYjI2Ni0yNmQ1NzgyMjM0YzgiLCJ0ZW5hbnQiOlsidGVuYW50TmFtZTpVbmlmaWVkIEJhc2tldCBUZXN0IENsaWVudCBBUEkiLCJncm91cElkOjM1MzEyZDFhLTUzNzEtNDAxZC1iNTUwLTdjN2NlOTQwMjczNSIsImNtZGJJZDoiXSwiYXVkIjpbInVuaWZpZWQtYmFza2V0LWl0ZW0tYXBpIiwidW5pZmllZC1iYXNrZXQtY29udGFjdC1hcGkiLCJ1bmlmaWVkLWJhc2tldC1zbmFwc2hvdC1hcGkiLCJ1bmlmaWVkLWJhc2tldC1hcGkiLCJ1bmlmaWVkLWJhc2tldC1zZWFyY2gtYXBpIl0sInNjb3BlIjpbInVuaWZpZWQtYmFza2V0LWl0ZW0tYXBpLnJlYWQiLCJ1bmlmaWVkLWJhc2tldC1pdGVtLWFwaS5yZWFkd3JpdGUiLCJ1bmlmaWVkLWJhc2tldC1jb250YWN0LWFwaS5yZWFkd3JpdGUiLCJ1bmlmaWVkLWJhc2tldC1jb250YWN0LWFwaS5yZWFkIiwidW5pZmllZC1iYXNrZXQtc25hcHNob3QtYXBpLnJlYWQiLCJ1bmlmaWVkLWJhc2tldC1hcGkuZGVsZXRlIiwidW5pZmllZC1iYXNrZXQtYXBpLnJlYWR3cml0ZSIsInVuaWZpZWQtYmFza2V0LWFwaS5yZWFkIiwidW5pZmllZC1iYXNrZXQtc2VhcmNoLWFwaS5yZWFkIiwidW5pZmllZC1iYXNrZXQtc2VhcmNoLWFwaS5yZWFkd3JpdGUiXSwiaWF0IjoxNzQ2NjE1OTQ2LCJuYmYiOjE3NDY2MTU5NDYsImV4cCI6MTc0NjYxNzc0NiwiaXNzIjoiaHR0cDovL3d3dy5kZWxsLmNvbS9pZGVudGl0eSJ9.vo7Buo0kGXmCh7g2l0T2GDZF59oOblgz_qMdGKbneCALBaOXMDGE0zKgHNVJAJPwihfrezIhrL1fzbTH2atf93I8bwpciOPga_u92zjaKi5Gi0Rz2KUBBvmUB3gGNweG54xS7bopdwU3J-JKVNd4hTzk0aKcMQB2yj10Mhz_130QzybbKQg_sdEpQxaus4wBnfyTjtFVhjiufQ_obp-ubmPZasncwdAJ0wuECpensQH4PHevHckOu3d-lcY3C85KQfBqixMZ3i7gDRVldLjwiJ3dfPN5bZ4YjF76OWkxUNf9-GqEDqoCkLV5LyG1dmCIx50HgNR4NrK0ZvsP0K-M6w"
}
client = httpx.AsyncClient(base_url="http://localhost:5167",verify=False,headers=headers)
server = FastMCP.from_openapi(openapi_spec=jobject,client=client,name="User Profile")
asyncio.run(check_mcp(server))

if __name__ == "__main__":
    server.run(transport='sse')
    
