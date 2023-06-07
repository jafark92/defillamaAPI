"""

"""

import time, requests

BASE_URL = "https://api.llama.fi"
COIN_BASE_URL = "https://coins.llama.fi"
STABLECOINS_BASE_URL = "https://stablecoins.llama.fi"
YIELDS_BASE_URL = "https://yields.llama.fi"
ABI_DECODER_BASE_URL = "https://abi-decoder.llama.fi"
BRIDGES_BASE_URL = "https://bridges.llama.fi"
VOLUMES_BASE_URL = "https://api.llama.fi"
FESSANDREVENUE_BASE_URL = "https://api.llama.fi"


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

class Stablecoins(Base):
    """ """
    
    def get_all_stablecoins(self, includePrices=None):
        """Description: List all stablecoins along with their circulating amounts"""
        path = '/stablecoins'
        params = {}
        if includePrices: params.update({"includePrices": includePrices})
        return self._send_request(method="GET", endpoint=path, base_url=STABLECOINS_BASE_URL, params=params)

    def get_all_stablecoins_charts(self, stablecoin=None):
        """Description: Get historical mcap sum of all stablecoins"""
        path = '/stablecoincharts/all'
        params = {}
        if stablecoin: params.update({"stablecoin": stablecoin})
        return self._send_request(method="GET", endpoint=path, base_url=STABLECOINS_BASE_URL, params=params)
    
    def get_stablecoincharts(self, chain, stablecoin):
        """Description: Get historical mcap sum of all stablecoins in a chain"""
        path = f"/stablecoincharts/{chain}"
        params = {}
        if stablecoin: params.update({"stablecoin": stablecoin})
        return self._send_request(method="GET", endpoint=path, base_url=STABLECOINS_BASE_URL, params=params)

    def get_stablecoin_asset(self, asset):
        """Description: Get historical mcap and historical chain distribution of a stablecoin"""
        path = f'/stablecoin/{asset}'
        return self._send_request(method="GET", endpoint=path, base_url=STABLECOINS_BASE_URL)

    def get_stablecoinchains(self):
        """Description: Get current mcap sum of all stablecoins on each chain"""
        path = '/stablecoinchains'
        return self._send_request(method="GET", endpoint=path, base_url=STABLECOINS_BASE_URL)

    def get_stablecoinprices(self):
        """Description: Get historical prices of all stablecoins"""
        path = '/stablecoinprices'
        return self._send_request(method="GET", endpoint=path, base_url=STABLECOINS_BASE_URL)

class Yields(Base):
    """"""
    def get_all_pools(self):
        """Description: Retrieve the latest data for all pools, including enriched information such as predictions"""
        path= "/pools"
        return self._send_request(method="GET", endpoint=path, base_url=YIELDS_BASE_URL)

    def get_pool_chart(self, pool):
        """Description: Get historical APY and TVL of a pool"""
        path= f"/chart/{pool}"
        return self._send_request(method="GET", endpoint=path, base_url=YIELDS_BASE_URL)

class ABIDecoder(Base):
    """"""
    def get_abi(self, functions=None, events=None):
        """Description: Get the ABI for a function or event signature."""
        path = '/fetch/signature'
        params = {}
        if functions is None and events is None:
            return {"message": "Kindly provide either functions or events"}
        if functions:
            params.update({"functions": functions})
        if events:
            params.update({"events": events})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=ABI_DECODER_BASE_URL)
    
    def get_abi_contract(self, chain, address, functions=None, events=None):
        """Description: Get the verbose ABI for a function or event signature for a particular contract"""
        path = f'/fetch/contract/{chain}/{address}'
        params = {}
        if functions is None and events is None:
            return {"message": "Kindly provide either functions or events"}
        if functions:
            params.update({"functions": functions})
        if events:
            params.update({"events": events})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=ABI_DECODER_BASE_URL)

class Bridges(Base):
    """"""
    def get_all_bridges(self, includeChains=True):
        """Description: List all bridges along with summaries of recent bridge volumes."""
        path = '/bridges'
        params = {"includeChains": includeChains}
        return self._send_request(method="GET", endpoint=path, params=params, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume_summary(self, id):
        """Description: Get a summary of bridge volume and volume breakdown by chain."""
        path = f'/bridge/{id}'
        return self._send_request(method="GET", endpoint=path, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume(self, chain, id=None):
        """Description: Get historical volumes for a bridge, chain, or bridge on a particular chain."""
        path = f'/bridgevolume/{chain}'
        params = {}
        if id: params.update({"id":id})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume_token(self, timestamp, chain, id=None):
        """Description: Get a 24hr token and address volume breakdown for a bridge."""
        path = f"/bridgedaystats/{timestamp}/{chain}"
        params = {}
        if id: params.update({"id":id})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=BRIDGES_BASE_URL)
    
    def get_all_transactions(self, id, starttimestamp=None, endtimestamp=None, sourcechain=None, address=None, limit=None):
        """Description: Get all transactions for a bridge within a date range."""
        path = f'/transactions/{id}'
        params = {}
        if id: params.update({"starttimestamp":starttimestamp})
        if id: params.update({"endtimestamp":endtimestamp})
        if id: params.update({"sourcechain":sourcechain})
        if id: params.update({"address":address})
        if id: params.update({"limit":limit})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=BRIDGES_BASE_URL)

class Volumes(Base):
    """"""
    def get_all_dexs(self, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all dexs along with summaries of their volumes and dataType history data."""
        path = "/overview/dexs"
        params= {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_chain(self, chain, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all dexs along with summaries of their volumes and dataType history data filtering by chain."""
        path = f"/overview/dexs/{chain}"
        params= {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dex_hist_data(self, protocol, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: Get a summary of dex volume with historical data."""
        path = f"/summary/dexs/{protocol}"
        params= {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_options(self, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all options dexs along with summaries of their volumes and dataType history data."""
        path = "/overview/options"
        params= {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_chain(self, chain, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all options dexs along with summaries of their volumes and dataType history data filtering by chain."""
        path = f"/overview/options/{chain}"
        params= {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_protocol(self, protocol, dataType=None):
        """Description: Get a summary of options dex volume with historical data."""
        path = f"/summary/options/{protocol}"
        params= {}
        if dataType: params.update({"dataType": dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

class FessAndRevenue(Base):
    """"""
    def get_all_protocols(self, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all protocols along with summaries of their fees and revenue and dataType history data."""
        path = "/overview/fees"
        params = {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=FESSANDREVENUE_BASE_URL)

    def get_protocols_chain(self, chain, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all protocols along with summaries of their fees and revenue and dataType history data by chain."""
        path = f"/overview/fees/{chain}"
        params = {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=FESSANDREVENUE_BASE_URL)

    def get_summary_protocol(self, protocol, dataType=None):
        """Description: Get a summary of protocol fees and revenue with historical data."""
        path = f"/summary/fees/{protocol}"
        params = {}
        if dataType: params.update({"dataType":dataType})
        return self._send_request(method="GET", endpoint=path, params=params, base_url=FESSANDREVENUE_BASE_URL)