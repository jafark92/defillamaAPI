"""

"""

import time, requests

BASE_URL = "https://api.llama.fi"
COIN_BASE_URL = "https://coins.llama.fi"

class Base:
    """
    """

    def __init__(self):
        """
        Initialize the object
        """
        self.session = requests.Session()

    def _send_request(self, method, endpoint, base_url=BASE_URL, params=None, data=None):
        """
        """
        url = base_url + endpoint
        response = self.session.request(method, url, params=params,
                                 data=data, timeout=60)
        return response.json()

class TVL(Base):

    """
    Endpoints to retrieve TVL data
    """

    def get_protocols(self):
        """
        """
        path = '/protocols'

        return self._send_request(method="GET", endpoint=path)

    def get_protocol_historical_tvl(self, protocol):
        """
        Get historical TVL of a protocol and breakdowns by token and chain
        Endpoint: GET /protocol/{name}

        :param: protocol : protocol slug eg: aave
            Can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f'/protocol/{protocol}'

        return self._send_request(method="GET", endpoint=path)

    def get_historical_tvl(self):
        """
        Get historical TVL (excludes liquid staking and double counted tvl) of DeFi on all chains

        :return: JSON response
        """
        path = '/v2/historicalChainTvl'

        return self._send_request(method="GET", endpoint=path)

    def get_historical_tvl_by_chain(self, chain):
        """
        Get historical TVL (excludes liquid staking and double counted tvl) of a chain

        :param: chain : chain slug, you can get these from /chains or the chains property on /protocols eg: Ethereum.
            This can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f"/v2/historicalChainTvl/{chain}"

        return self._send_request(method="GET", endpoint=path)
    
    def get_tvl_of_protocol(self, protocol):
        """
        Simplified endpoint that only returns a number, the current TVL of a protocol
        
        :param: protocol : protocol slug eg: uniswap
        :return: JSON response
        """
        path = f'/tvl/{protocol}'

        return self._send_request(method="GET", endpoint=path)
    
    def get_tvl_chains(self, protocol):
        """
        Get current TVL of all chains
        :return: JSON response
        """
        path = '/v2/chains'

        return self._send_request(method="GET", endpoint=path)

class Coins(Base):
    """
    Endpoints for General blockchain data used by defillama and open-sourced
    """

    def token_prices(self, coins, searchWidth="4h"):
        """
        Get current prices of tokens by contract address

        Detail Description:

        The goal of this API is to price as many tokens as possible, including exotic ones that never get traded, which makes them impossible to price by looking at markets.

        The base of our data are prices pulled from coingecko, which is then extended through multiple means:

        We price all bridged tokens by using the price of the token in it's original chain, so we fetch all bridged versions of USDC on arbitrum, fantom, avax... and price all them using the price for the token on Ethereum, which we know. Right now we support 10 different bridging protocols.

        We have multiple adapters to price specialized sets of tokens by running custom code:

        We price yearn's yToken LPs by checking how much underlying token can be withdrawn for each LP

        Aave, compound and euler LP tokens are also priced based on their relationship against underlying tokens

        Uniswap, curve, balancer and stargate LPs are priced using the underlying tokens in each pair

        GMX's GLP token is priced based on the value of tokens given on withdrawal (which includes calculations based on trader's PnL)

        Synthetix tokens are priced using forex prices of the coin they are pegged to

        For tokens that we haven't been able to price in any other way, we find the pool with most liquidity for each on uniswap, curve and serum and then use the prices provided on those exchanges.

        Unlike all the other tokens, we can't confirm that these prices are correct, so we only ingest the ones that have sufficient liquidity and, even in that case, we attach a confidence value to them that is related to the depth of liquidity and which represents our confidence in the quality of each price. API consumers can choose to filter out prices with low confidence values.

        Our API server is fully open source and we are constantly adding more pricing adapters, extending the amount of tokens we support.

        Tokens are queried using {chain}:{address}, where chain is an identifier such as ethereum, bsc, polygon, avax... You can also get tokens by coingecko id by setting coingecko as the chain, eg: coingecko:ethereum, coingecko:bitcoin. Examples:

        ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1
        bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878
        coingecko:ethereum
        arbitrum:0x4277f8f2c384827b5273592ff7cebd9f2c1ac258

        :param: coins : set of comma-separated tokens defined as {chain}:{address} eg: ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1,coingecko:ethereum,bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878,ethereum:0xdB25f211AB05b1c97D595516F45794528a807ad8
            searchWidth : 4h
            
        :return: JSON response
        """
        path = f"/prices/current/{coins}"

        return self._send_request(method="GET", endpoint=path, base_url=COIN_BASE_URL,  params={"searchWidth": searchWidth})

    def token_historical_prices(self, timestamp, coins, searchWidth="4h"):
        """
        Get historical TVL (excludes liquid staking and double counted tvl) of DeFi on all chains

        :return: JSON response
        """
        path = f'/prices/historical/{timestamp}/{coins}'

        return self._send_request(method="GET", endpoint=path, base_url=COIN_BASE_URL,  params={"searchWidth": searchWidth})

    def batch_historical(self, coins, searchWidth="600"):
        """
        Strings accepted by period and searchWidth: Can use regular chart candle notion like ‘4h’ etc where: W = week, D = day, H = hour, M = minute (not case sensitive)
        """
        path = "/batchHistorical"

        return self._send_request(method="GET", endpoint=path, base_url=COIN_BASE_URL,  params={"coins": coins, "searchWidth": searchWidth})
    
    def token_pricess_by_time(self, coins, start=1664364537, end=None, span=10, period="2d", searchWidth="600"):
        """
        Strings accepted by period and searchWidth: Can use regular chart candle notion like ‘4h’ etc where: W = week, D = day, H = hour, M = minute (not case sensitive)
        """
        path = f'/chart/{coins}'
        params = {'start': start, 'span': span, 'period': period, 'searchWidth': searchWidth}
    
        if end is not None:
            params['end'] = end

        return self._send_request(method="GET", endpoint=path, base_url=COIN_BASE_URL,  params=params)

    def percentage_change(self, coins, timestamp=None, lookForward=False, period="3w"):
        """
        Strings accepted by period: Can use regular chart candle notion like ‘4h’ etc where: W = week, D = day, H = hour, M = minute (not case sensitive)
        """
        if timestamp is None: timestamp=time.now()
        path = f'/percentage/{coins}'
        params = {'timestamp': timestamp, 'lookForward': lookForward, 'period': period}

        return self._send_request(method="GET", endpoint=path, base_url=COIN_BASE_URL,  params=params)

    def first_price(self, coins):
        """
        Strings accepted by period: Can use regular chart candle notion like ‘4h’ etc where: W = week, D = day, H = hour, M = minute (not case sensitive)
        """
        path = f'/prices/first/{coins}'

        return self._send_request(method="GET", endpoint=path, base_url=COIN_BASE_URL)
    
    def closest_block(self, chain, timestamp):
        """
        Runs binary search over a blockchain's blocks to get the closest one to a timestamp. Every time this is run we add new data to our database, so each query permanently speeds up future queries.
        """
        path = f'/block/{chain}/{timestamp}'

        return self._send_request(method="GET", endpoint=path, base_url=COIN_BASE_URL)

