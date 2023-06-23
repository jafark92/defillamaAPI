from .defillamaAPI import Base
import time

COIN_BASE_URL = "https://coins.llama.fi"
class Coins(Base):
    """
    Endpoints for Coins
    """
    
    def token_prices(self, coins, searchWidth="4h"):
        """
        Get current prices of tokens by contract address

        The goal of this API is to price as many tokens as possible, including exotic ones that never get traded, 
        which makes them impossible to price by looking at markets.

        The base of our data are prices pulled from coingecko, which is then extended through multiple means:
            * We price all bridged tokens by using the price of the token in it's original chain, so we fetch all bridged versions of 
              USDC on arbitrum, fantom, avax... and price all them using the price for the token on Ethereum, which we know. Right now 
              we support 10 different bridging protocols.

            * We have multiple adapters to price specialized sets of tokens by running custom code:
                * We price yearn's yToken LPs by checking how much underlying token can be withdrawn for each LP
                * Aave, compound and euler LP tokens are also priced based on their relationship against underlying tokens
                * Uniswap, curve, balancer and stargate LPs are priced using the underlying tokens in each pair
                * GMX's GLP token is priced based on the value of tokens given on withdrawal (which includes calculations 
                  based on trader's PnL)
                * Synthetix tokens are priced using forex prices of the coin they are pegged to

            * For tokens that we haven't been able to price in any other way, we find the pool with most liquidity for each on uniswap, 
              curve and serum and then use the prices provided on those exchanges.

            Unlike all the other tokens, we can't confirm that these prices are correct, so we only ingest the ones that have sufficient 
            liquidity and, even in that case, we attach a confidence value to them that is related to the depth of liquidity and which 
            represents our confidence in the quality of each price. API consumers can choose to filter out prices with low confidence values.

        Our API server is fully open source and we are constantly adding more pricing adapters, extending the amount of tokens we support.

        Tokens are queried using {chain}:{address}, where chain is an identifier such as ethereum, bsc, polygon, avax... You can also get 
        tokens by coingecko id by setting coingecko as the chain, eg: coingecko:ethereum, coingecko:bitcoin. Examples:

        * ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1
        * bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878
        * coingecko:ethereum
        * arbitrum:0x4277f8f2c384827b5273592ff7cebd9f2c1ac258

        Parameters
        ----------
        coins : string (path)
            set of comma-separated tokens defined as {chain}:{address} 
            Example: ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1,coingecko:ethereum,bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878,ethereum:0xdB25f211AB05b1c97D595516F45794528a807ad8

        searchWidth : string (query)
            time range on either side to find price data, defaults to 6 hours
            Example: 4h
            
        Return
        ----------
        JSON response
        """
        path = f"/prices/current/{coins}"
        return self._send_request(endpoint=path, base_url=COIN_BASE_URL,  params={"searchWidth": searchWidth})

    def token_historical_prices(self, timestamp, coins, searchWidth="4h"):
        """
        Get historical prices of tokens by contract address
        See /prices/current for explanation on how prices are sourced.

        Parameters
        ----------
        coins : string (path)
            set of comma-separated tokens defined as {chain}:{address}
            Example: ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1,coingecko:ethereum,bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878,ethereum:0xdB25f211AB05b1c97D595516F45794528a807ad8
        
        timestamp : number (path)
            UNIX timestamp of time when you want historical prices
            Example: 1648680149

        searchWidth : string (query)
            time range on either side to find price data, defaults to 6 hours
            Example: 4h

        Return
        ----------
        JSON response
        """
        path = f'/prices/historical/{timestamp}/{coins}'
        return self._send_request(endpoint=path, base_url=COIN_BASE_URL,  params={"searchWidth": searchWidth})

    def batch_historical(self, coins, searchWidth="600"):
        """
        Get historical prices for multiple tokens at multiple different timestamps
        Strings accepted by period and searchWidth: Can use regular chart candle notion like ‘4h’ etc where: W = week, D = day, H = hour, 
        M = minute (not case sensitive)

        Parameters
        ----------
        coins : string (path)
            object where keys are coins in the form {chain}:{address}, and values are arrays of requested timestamps
            Example: {"avax:0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e": [1666876743, 1666862343], "coingecko:ethereum": [1666869543, 1666862343]}
        
        searchWidth : string (query)
            time range on either side to find price data, defaults to 6 hours
            Example: 600

        Return
        ----------
        JSON response
        """
        path = "/batchHistorical"
        return self._send_request(endpoint=path, base_url=COIN_BASE_URL,  params={"coins": coins, "searchWidth": searchWidth})
    
    def token_pricess_by_time(self, coins, start=1664364537, end=None, span=10, period="2d", searchWidth="600"):
        """
        Get token prices at regular time intervals
        Strings accepted by period and searchWidth: Can use regular chart candle notion like ‘4h’ etc where: W = week, D = day, H = hour, 
        M = minute (not case sensitive)

        Parameters
        ----------
        coins : string (path)
            set of comma-separated tokens defined as {chain}:{address}
            Example: ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1,coingecko:ethereum,bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878,ethereum:0xdB25f211AB05b1c97D595516F45794528a807ad8
    
        start : number (query)
            unix timestamp of earliest data point requested
            Example: 1664364537
    
        end : number (query)
            unix timestamp of latest data point requested

        span : number (query)
            number of data points returned, defaults to 0
            Example: 10

        period : string (query)
            duration between data points, defaults to 24 hours
            Example: 2d

        searchWidth : string (query)
            time range on either side to find price data, defaults to 10% of period
            Example: 600

        Return
        ----------
        JSON response
        """
        path = f'/chart/{coins}'
        params = {'start': start, 'span': span, 'period': period, 'searchWidth': searchWidth}
        if end is not None:
            params['end'] = end
        return self._send_request(endpoint=path, base_url=COIN_BASE_URL,  params=params)

    def percentage_change(self, coins, timestamp=None, lookForward=False, period="3w"):
        """
        Get percentage change in price over time
        Strings accepted by period: Can use regular chart candle notion like ‘4h’ etc where: W = week, D = day, H = hour, M = minute (not case sensitive)

        Parameters
        ----------
        coins : string (path)
            set of comma-separated tokens defined as {chain}:{address}
            Example: ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1,coingecko:ethereum,bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878,ethereum:0xdB25f211AB05b1c97D595516F45794528a807ad8

        timestamp : number (query)
            timestamp of data point requested, defaults to time now
            Example: 1664364537

        lookForward : boolean (query)
            whether you want the duration after your given timestamp or not, defaults to false (looking back)
            Example: False

        period: string (query)
            duration between data points, defaults to 24 hours
            Example:3w

        Return
        ----------
        JSON response
        """
        if timestamp is None: timestamp=time.now()
        path = f'/percentage/{coins}'
        params = self._get_params_dict(timestamp, lookForward)
        params.update({'period': period})
        return self._send_request(endpoint=path, base_url=COIN_BASE_URL,  params=params)

    def first_price(self, coins):
        """
        Get earliest timestamp price record for coins
        
        Parameters
        ----------
        coins : string (path)
            set of comma-separated tokens defined as {chain}:{address}
            Example: ethereum:0xdF574c24545E5FfEcb9a659c229253D4111d87e1,coingecko:ethereum,bsc:0x762539b45a1dcce3d36d080f74d1aed37844b878,ethereum:0xdB25f211AB05b1c97D595516F45794528a807ad8
        
        Return
        ----------
        JSON response
        """
        path = f'/prices/first/{coins}'
        return self._send_request(endpoint=path, base_url=COIN_BASE_URL)
    
    def closest_block(self, chain, timestamp):
        """
        Get the closest block to a timestamp
        Runs binary search over a blockchain's blocks to get the closest one to a timestamp. Every time this is run we add new data to our database, 
        so each query permanently speeds up future queries.

        Parameters
        ----------
        chain : string (path)
            Chain which you want to get the block from

        timestamp : integer (path)
            UNIX timestamp of the block you are searching for
        
        Return
        ----------
        JSON response
        """
        path = f'/block/{chain}/{timestamp}'
        return self._send_request(endpoint=path, base_url=COIN_BASE_URL)
