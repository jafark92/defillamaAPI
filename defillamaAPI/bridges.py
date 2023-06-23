from .defillamaAPI import Base

BRIDGES_BASE_URL = "https://bridges.llama.fi"
class Bridges(Base):
    """"""
    def get_all_bridges(self, includeChains=True):
        """
        List all bridges along with summaries of recent bridge volumes
        
        Parameters
        ----------
        includeChains : boolean (query)
            set whether to include current previous day volume breakdown by chain
            Example: true

        Return
        ----------
        JSON response
        """
        path = '/bridges'
        params = self._get_params_dict(includeChains)
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume_summary(self, id):
        """
        Get a summary of bridge volume and volume breakdown by chain
        
        Parameters
        ----------
        id : integer (path)
            bridge ID, you can get these from /bridges
            Example; 1

        Return
        ----------
        JSON response
        """
        path = f'/bridge/{id}'
        return self._send_request(endpoint=path, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume(self, chain, **args):
        """
        Get historical volumes for a bridge, chain, or bridge on a particular chain
        
        Parameters
        ----------
        chain : string (path)
            chain slug, you can get these from /chains. Call also use 'all' for volume on all chains.
            Example: Ethereum

        id : integer (query)
            bridge ID, you can get these from /bridges
            Example: 5

        Return
        ----------
        JSON response
        """
        path = f'/bridgevolume/{chain}'
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume_token(self, timestamp, chain, **args):
        """Get a 24hr token and address volume breakdown for a bridge
        Parameters
        ----------
        timestamp : integer (path)
            Unix timestamp. Data returned will be for the 24hr period starting at 00:00 UTC that the timestamp lands in.
            Example: 1667304000

        chain :  string (path)
            chain slug, you can get these from /chains.
            Example: Ethereum

        id : integer (query)
            bridge ID, you can get these from /bridges
            Example: 5

        Return
        ----------
        JSON response
        """
        path = f"/bridgedaystats/{timestamp}/{chain}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)
    
    def get_all_transactions(self, id, **args):
        """Get all transactions for a bridge within a date range
        Parameters
        ----------
        id : integer (path)
            bridge ID, you can get these from /bridges
            Example: 1

        starttimestamp: integer (query)
            start timestamp (Unix Timestamp) for date range
            Example: 1667260800

        endtimestamp: integer (query)
            end timestamp (Unix timestamp) for date range
            Example: 1667347200

        sourcechain: string (query)
            Returns only transactions that are bridging from the specified source chain.
            Example: Polygon

        address: string (query)
            Returns only transactions with specified address as "from" or "to". Addresses are quried in the form {chain}:{address}, where chain is an identifier such as ethereum, bsc, polygon, avax... .
            Example: ethereum:0x69b4B4390Bd1f0aE84E090Fe8af7AbAd2d95Cc8E

        limit: integer (query)
            limit to number of transactions returned, maximum is 6000
            Example: 200

        Return
        ----------
        JSON response
        """
        path = f'/transactions/{id}'
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)
