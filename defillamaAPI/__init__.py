# from .defillamaAPI import Base
from .tvl import TVL
from .coins import Coins
from .stablecoins import Stablecoins
from .yields import Yields
from .abidecoder import ABIDecoder
from .bridges import Bridges
from .volumes import Volumes
from .feesandrevenue import FeesAndRevenue

# So that we can directly use classes as object during import instead of creating obvious objects
FeesAndRevenue = FeesAndRevenue()
TVL = TVL()
Coins = Coins()
Stablecoins = Stablecoins()
Yields = Yields()
ABIDecoder = ABIDecoder()
Bridges = Bridges()
Volumes = Volumes()