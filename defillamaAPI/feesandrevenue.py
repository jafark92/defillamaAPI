from .defillamaAPI import Base

FEESANDREVENUE_BASE_URL = "https://api.llama.fi"
class FeesAndRevenue(Base):
    """"""
    def get_all_protocols(self, **args):
        """
        List all protocols along with summaries of their fees and revenue and dataType history data

        Parameters
        ----------
        excludeTotalDataChart : boolean (query)
            true to exclude aggregated chart from response
            Example: true

        excludeTotalDataChartBreakdown : boolean (query)
            true to exclude broken down chart from response
            Example: true

        dataType : string (query)
            Desired data type, dailyFees by default.
            Available values : totalFees, dailyFees, totalRevenue, dailyRevenue
            Example: dailyFees

        Return
        ----------
        JSON response
        """
        path = "/overview/fees"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=FEESANDREVENUE_BASE_URL)

    def get_protocols_chain(self, chain, **args):
        """
        List all protocols along with summaries of their fees and revenue and dataType history data by chain

        Parameters
        ----------
        chain : string (path)
            chain name, list of all supported chains can be found under allChains attribute in /overview/fees response
            Example: ethereum

        excludeTotalDataChart: boolean (query)
            true to exclude aggregated chart from response
            Example: true

        excludeTotalDataChartBreakdown: boolean (query)
            true to exclude broken down chart from response
            Example: true

        dataType: string (query)
            Desired data type, dailyFees by default.
            Available values : totalFees, dailyFees, totalRevenue, dailyRevenue
            Example: dailyFees

        Return
        ----------
        JSON response
        """
        path = f"/overview/fees/{chain}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=FEESANDREVENUE_BASE_URL)

    def get_summary_protocol(self, protocol, **args):
        """
        Get a summary of protocol fees and revenue with historical data

        Parameters
        ----------
        protocol : string (path)
            protocol slug
            Example: lyra

        dataType : string (query)
            Desired data type, dailyFees by default.
            Available values : totalFees, dailyFees, totalRevenue, dailyRevenue
            Example: dailyFees

        Return
        ----------
        JSON response
        """
        path = f"/summary/fees/{protocol}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=FEESANDREVENUE_BASE_URL)