import requests

API_ROOT = r"https://www.googleapis.com/customsearch/v1?"
KEY = "AIzaSyANpCNdOXG6s1ZFP1gZsbJ3f71LHfk-hio"
ENGINE_ID = "71a072fcae628476a"
LINK = "https://uqpug.github.io/"

class NotFoundError(Exception):
    """Raised when TITLE is not found in searches"""

queries = ["uq pug", "uq python user group"]

for query in queries:
    r = requests.get(API_ROOT+f"key={KEY}&cx={ENGINE_ID}&q={query}")

    r.raise_for_status()

    content = r.json()

    for result in content["items"]:
        if LINK in result["link"]:
            print(f"Query '{query}' has PASSED")
            break    
    else:
        raise NotFoundError(f"Page '{LINK}' was not found with query '{query}'")



