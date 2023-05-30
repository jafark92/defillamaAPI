# defillamaAPI
Under Development
API Collection of DefiLlama - Unofficial

### Installation:

use pip to install:

``` 
pip install defillamaAPI
```

### Example usage:

```
from defillamaAPI import TVL

# initialize TVL api client
defillama_tvl = TVL()

# Get all protocols data
response = defillama_tvl.get_protocols()

```

-------

Task ToDo
-> Add remaining endpoints
-> User can select if he wants pandas dataframe or just response json
-> Test with other versions of python ( Although used only requests and time module with no fancy methods)