from .defillamaAPI import Base

class TVL(Base):

    """
    Endpoints to retrieve TVL data
    """

    def get_protocols(self):
        """
        """
        path = '/protocols'
        return self._send_request(endpoint=path)

    def get_protocol_historical_tvl(self, protocol):
        """
        Get historical TVL of a protocol and breakdowns by token and chain
        Endpoint: GET /protocol/{name}

        :param: protocol : protocol slug eg: aave
            Can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f'/protocol/{protocol}'
        return self._send_request(endpoint=path)

    def get_historical_tvl(self):
        """
        Get historical TVL (excludes liquid staking and double counted tvl) of DeFi on all chains

        :return: JSON response
        """
        path = '/v2/historicalChainTvl'
        return self._send_request(endpoint=path)

    def get_historical_tvl_by_chain(self, chain):
        """
        Get historical TVL (excludes liquid staking and double counted tvl) of a chain

        :param: chain : chain slug, you can get these from /chains or the chains property on /protocols eg: Ethereum.
            This can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f"/v2/historicalChainTvl/{chain}"
        return self._send_request(endpoint=path)
    
    def get_tvl_of_protocol(self, protocol):
        """
        Simplified endpoint that only returns a number, the current TVL of a protocol
        
        :param: protocol : protocol slug eg: uniswap
        :return: JSON response
        """
        path = f'/tvl/{protocol}'
        return self._send_request(endpoint=path)
    
    def get_tvl_chains(self, protocol):
        """
        Get current TVL of all chains
        :return: JSON response
        """
        path = '/v2/chains'
        return self._send_request(endpoint=path)