from agentsjson.core.executor import execute
from agentsjson.core.models.schema import Flow, Link, Action
from agentsjson.core.models.auth import AuthType, ApiKeyAuthConfig

API_KEY = ""

def test_trending_gifs():
    # Create a simple chain that just gets trending GIFs
    chain = Flow(
        id="test_trending",
        name="Trending GIFs",
        displayName="Get Trending GIFs",
        description="Fetches trending GIFs from Giphy",
        fields={
            "parameters": [],
            "requestBody": []
        },
        order=[
            Action(
                id="get_trending",
                apiName="giphy",
                operationId="giphy_get_gifs_trending"
            )
        ],
        links=[
            # Link to pass the response back to the chain
            Link(
                origin={"id": "get_trending", "fieldType": "responses", "fieldName": "data"},
                target={"id": "test_trending", "fieldType": "responses", "fieldName": "gifs"}
            )
        ]
    )
    
    # Set up auth config
    auth = ApiKeyAuthConfig(
        type=AuthType.API_KEY,
        key_value=API_KEY
    )
    
    # Execute the chain
    result = execute(chain, auth, parameters={}, requestBody={})
    print(f"Found {len(result['gifs'])} trending GIFs")
    
def test_search_gifs():
    # Create a chain that searches for GIFs
    chain = Flow(
        id="test_search",
        name="Search GIFs",
        displayName="Search for GIFs",
        description="Searches for GIFs on Giphy",
        fields={
            "parameters": [{"fieldName": "q"}, {"fieldName": "limit"}],
            "requestBody": []
        },
        order=[
            Action(
                id="search_gifs",
                apiName="giphy",
                operationId="giphy_get_gifs_search"
            )
        ],
        links=[
            Link(
                origin={"id": "test_search", "fieldType": "parameters", "fieldName": "q"},
                target={"id": "search_gifs", "fieldType": "parameters", "fieldName": "q"}
            ),
            Link(
                origin={"id": "test_search", "fieldType": "parameters", "fieldName": "limit"},
                target={"id": "search_gifs", "fieldType": "parameters", "fieldName": "limit"}
            ),
            Link(
                origin={"id": "search_gifs", "fieldType": "responses", "fieldName": "data"},
                target={"id": "test_search", "fieldType": "responses", "fieldName": "results"}
            )
        ]
    )
    
    auth = ApiKeyAuthConfig(
        type=AuthType.API_KEY,
        key_value=API_KEY
    )
    
    # Execute with search parameters
    result = execute(
        chain,
        auth,
        parameters={"q": "cats", "limit": 5},
        requestBody={}
    )
    print(f"Found {len(result['results'])} GIFs matching 'cats'")

def test_random_gif():
    # Create a chain that gets a random GIF
    chain = Flow(
        id="test_random",
        name="Random GIF",
        displayName="Get Random GIF",
        description="Gets a random GIF from Giphy",
        fields={
            "parameters": [],
            "requestBody": []
        },
        order=[
            Action(
                id="random_gif",
                apiName="giphy",
                operationId="giphy_get_gifs_random"
            )
        ],
        links=[
            Link(
                origin={"id": "random_gif", "fieldType": "responses", "fieldName": "data"},
                target={"id": "test_random", "fieldType": "responses", "fieldName": "gif"}
            )
        ]
    )
    
    auth = ApiKeyAuthConfig(
        type=AuthType.API_KEY,
        key_value=API_KEY
    )
    
    # Execute to get a random GIF
    result = execute(chain, auth, parameters={}, requestBody={})
    print(f"Got random GIF with ID: {result['gif'].get('id')}")

if __name__ == "__main__":
    print("Testing Giphy Integration")
    print("-----------------------")
    
    print("\nTesting trending GIFs:")
    test_trending_gifs()
    
    print("\nTesting GIF search:")
    test_search_gifs()
    
    print("\nTesting random GIF:")
    test_random_gif() 