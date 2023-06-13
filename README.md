# defillamaAPI
API Collection of DefiLlama (https://defillama.com/docs/api)

Splitted the endpoints categories on defillama's 'docs as a seperate class, so that user can import only required category endpoints.

### Installation:

use pip to install:

``` 
pip install defillamaAPI
```

### Example usage:

```
from defillamaAPI import TVL, Stablecoins

# initialize TVL api client
defillama_tvl = TVL()

# initialize Stablecoins api client
defillama_stablecoins = Stablecoins()

# Get all protocols data
protocols = defillama_tvl.get_protocols()

# Get all stablecoins along with their circulating amounts
stablecoins = defillama_stablecoins.get_all_stablecoins()
```
-------
**Task ToDo**
- Write Test cases to validate the response
- Add Doc string details for all endpoints
- User can select if he wants pandas dataframe or just response json
- Test with other versions of python ( Although used only requests and time module with no fancy methods)

This is open-source project, I am extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.