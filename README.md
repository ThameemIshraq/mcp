//  Ignore the below if you have already an existing api(with openapi standards definition defined)
clone the gitlab repo, open the sample api folder..its a webapi built on .net 9(Install this version if its not already installed)
if you running in vscode, open the terminal go to the folder userprofile and do a dotnet run
it should ideally run the application and provide you with a url which is the basic url for accessing this app
for example: http://localhost:5167 then the swagger for this would http://localhost:5167/swagger/v1/swagger.json..
grab both of these urls for use in mcp server

----------------------------------------------------------------------------------------------------------------------------

open a new vscode go to the folder mcpclientserver..
based on the package manager(UV or PIP) create a virtual environment 
install the required dependencies using PIP or UV from the requirements
for example: pip install -r <path to requirements file>
once the required packages are installed..
to run the server put in the swagger endpoints grabbed either from running the sampleapi or the existing api which you want to turn as mcp server
to use it in a mcpclient use python server.py/FastMcp run server.py which will spin up a new mcp server and provide you the uri
to run the server and run it debug mode use FastMcp dev server.py which will open a mcp inspector 
once the mcp server is up and running, take the uri and put the uri in the client constructor in client.py
now run the client using python client.py which will spin up a mcpclient and connect with sampleapi/any api using mcp server
check the connectivity by invoking any of the tools/resources/resourcetemplates on the mcp server

