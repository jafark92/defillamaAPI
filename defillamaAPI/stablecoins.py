from .defillamaAPI import Base

STABLECOINS_BASE_URL = "https://stablecoins.llama.fi"
class Stablecoins(Base):
    """ """
    
    def get_all_stablecoins(self, **args):
        """List all stablecoins along with their circulating amounts
        
        Parameters
        ----------
        includePrices : boolean (query)
            set whether to include current stablecoin prices
            Example: true

        Return
        ----------
        JSON response
        """
        path = '/stablecoins'
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, base_url=STABLECOINS_BASE_URL, params=params)

    def get_all_stablecoins_charts(self, **args):
        """Get historical mcap sum of all stablecoins
        
        Parameters
        ----------
        stablecoin : integer (query)
            stablecoin ID, you can get these from /stablecoins
            Example: 1

        Return
        ----------
        JSON response
        """
        path = '/stablecoincharts/all'
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, base_url=STABLECOINS_BASE_URL, params=params)
    
    def get_stablecoincharts(self, chain, stablecoin):
        """Get historical mcap sum of all stablecoins in a chain
        
        Parameters
        ----------
        chain : string (path)
            chain slug, you can get these from /chains or the chains property on /protocols
            Example: Ethereum

        stablecoin : integer (query)
            stablecoin ID, you can get these from /stablecoins
            Example: 1

        Return
        ----------
        JSON response
        """
        path = f"/stablecoincharts/{chain}"
        params = self._get_params_dict(stablecoin)
        return self._send_request(endpoint=path, base_url=STABLECOINS_BASE_URL, params=params)

    def get_stablecoin_asset(self, asset):
        """Get historical mcap and historical chain distribution of a stablecoin
        
        Parameters
        ----------
        asset : integer (path)
            stablecoin ID, you can get these from /stablecoins
            Example: 1

        Return
        ----------
        JSON response
        """
        path = f'/stablecoin/{asset}'
        return self._send_request(endpoint=path, base_url=STABLECOINS_BASE_URL)

    def get_stablecoinchains(self):
        """Get current mcap sum of all stablecoins on each chain
        
        Return
        ----------
        JSON response
        """
        path = '/stablecoinchains'
        return self._send_request(endpoint=path, base_url=STABLECOINS_BASE_URL)

    def get_stablecoinprices(self):
        """Get historical prices of all stablecoins

        Return
        ----------
        JSON response
        """
        path = '/stablecoinprices'
        return self._send_request(endpoint=path, base_url=STABLECOINS_BASE_URL)
