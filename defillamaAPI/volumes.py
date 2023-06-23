from .defillamaAPI import Base

VOLUMES_BASE_URL = "https://api.llama.fi"
class Volumes(Base):
    """"""
    def get_all_dexs(self, **args):
        """
        List all dexs along with summaries of their volumes and dataType history data

        Parameters
        ----------
        excludeTotalDataChart : boolean (query)
            true to exclude aggregated chart from response
            Example: true

        excludeTotalDataChartBreakdown : boolean (query)
            true to exclude broken down chart from response
            Example: true

        dataType : string (query)
            Desired data type, dailyVolume by default.
            Available values : dailyVolume, totalVolume
            Example: dailyVolume

        Return
        ----------
        JSON response
        """
        path = "/overview/dexs"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_chain(self, chain, **args):
        """
        List all dexs along with summaries of their volumes and dataType history data filtering by chain

        Parameters
        ----------
        chain : string (path)
            chain name, list of all supported chains can be found under allChains attribute in /overview/dexs response
            Example: ethereum

        excludeTotalDataChart : boolean (query)
            true to exclude aggregated chart from response
            Example: true

        excludeTotalDataChartBreakdown : boolean (query)
            true to exclude broken down chart from response
            Example: true

        dataType : string (query)
            Desired data type, dailyVolume by default.
            Available values : dailyVolume, totalVolume
            Example: dailyVolume

        Return
        ----------
        JSON response
        """
        path = f"/overview/dexs/{chain}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dex_hist_data(self, protocol, **args):
        """
        Get a summary of dex volume with historical data

        Parameters
        ----------
        protocol : string (path)
            protocol slug
            Example: aave

        excludeTotalDataChart : boolean (query)
            true to exclude aggregated chart from response
            Example: true

        excludeTotalDataChartBreakdown : boolean (query)
            true to exclude broken down chart from response
            Example: true

        dataType : string (query)
            Desired data type, dailyVolume by default.
            Available values : dailyVolume, totalVolume
            Example: dailyVolume

        Return
        ----------
        JSON response
        """
        path = f"/summary/dexs/{protocol}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_options(self, **args):
        """
        List all options dexs along with summaries of their volumes and dataType history data

        Parameters
        ----------
        excludeTotalDataChart: boolean (query)
            true to exclude aggregated chart from response
            Example: true

        excludeTotalDataChartBreakdown: boolean (query)
            true to exclude broken down chart from response
            Example: true

        dataType: string (query)
            Desired data type, dailyNotionalVolume by default.
            Available values : dailyPremiumVolume, dailyNotionalVolume, totalPremiumVolume, totalNotionalVolume
            Example: dailyPremiumVolume

        Return
        ----------
        JSON response
        """
        path = "/overview/options"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_chain(self, chain, **args):
        """
        List all options dexs along with summaries of their volumes and dataType history data filtering by chain

        Parameters
        ----------
        chain : string (path)
            chain name, list of all supported chains can be found under allChains attribute in /overview/options response
            Example: ethereum

        excludeTotalDataChart : boolean (query)
            true to exclude aggregated chart from response
            Example: true

        excludeTotalDataChartBreakdown : boolean (query)
            true to exclude broken down chart from response
            Example: true
        
        dataType : string (query)
            Desired data type, dailyNotionalVolume by default.
            Available values : dailyPremiumVolume, dailyNotionalVolume, totalPremiumVolume, totalNotionalVolume
            Example: dailyPremiumVolume

        Return
        ----------
        JSON response
        """
        path = f"/overview/options/{chain}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_protocol(self, protocol, **args):
        """
        Get a summary of options dex volume with historical data

        Parameters
        ----------
        protocol : string (path)
            protocol slug
            Example: lyra

        dataType : string (query)
            Desired data type, dailyNotionalVolume by default.
            Available values : dailyPremiumVolume, dailyNotionalVolume, totalPremiumVolume, totalNotionalVolume
            Example: dailyPremiumVolume

        Return
        ----------
        JSON response
        """
        path = f"/summary/options/{protocol}"
        params= self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)