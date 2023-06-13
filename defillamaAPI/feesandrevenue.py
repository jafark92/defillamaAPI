from .defillamaAPI import Base

FESSANDREVENUE_BASE_URL = "https://api.llama.fi"
class FeesAndRevenue(Base):
    """"""
    def get_all_protocols(self, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all protocols along with summaries of their fees and revenue and dataType history data."""
        path = "/overview/fees"
        params = {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(endpoint=path, params=params, base_url=FESSANDREVENUE_BASE_URL)

    def get_protocols_chain(self, chain, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all protocols along with summaries of their fees and revenue and dataType history data by chain."""
        path = f"/overview/fees/{chain}"
        params = {}
        if excludeTotalDataChart: params.update({"excludeTotalDataChart":excludeTotalDataChart})
        if excludeTotalDataChartBreakdown: params.update({"excludeTotalDataChartBreakdown":excludeTotalDataChartBreakdown})
        if dataType: params.update({"dataType":dataType})
        return self._send_request(endpoint=path, params=params, base_url=FESSANDREVENUE_BASE_URL)

    def get_summary_protocol(self, protocol, dataType=None):
        """Description: Get a summary of protocol fees and revenue with historical data."""
        path = f"/summary/fees/{protocol}"
        params = {}
        if dataType: params.update({"dataType":dataType})
        return self._send_request(endpoint=path, params=params, base_url=FESSANDREVENUE_BASE_URL)