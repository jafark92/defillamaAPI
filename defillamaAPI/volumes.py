from .defillamaAPI import Base

VOLUMES_BASE_URL = "https://api.llama.fi"
class Volumes(Base):
    """"""
    def get_all_dexs(self, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all dexs along with summaries of their volumes and dataType history data."""
        path = "/overview/dexs"
        params = self._get_params_dict(excludeTotalDataChart,excludeTotalDataChartBreakdown, dataType)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_chain(self, chain, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all dexs along with summaries of their volumes and dataType history data filtering by chain."""
        path = f"/overview/dexs/{chain}"
        params = self._get_params_dict(excludeTotalDataChart,excludeTotalDataChartBreakdown, dataType)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dex_hist_data(self, protocol, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: Get a summary of dex volume with historical data."""
        path = f"/summary/dexs/{protocol}"
        params = self._get_params_dict(excludeTotalDataChart,excludeTotalDataChartBreakdown, dataType)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_options(self, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all options dexs along with summaries of their volumes and dataType history data."""
        path = "/overview/options"
        params = self._get_params_dict(excludeTotalDataChart,excludeTotalDataChartBreakdown, dataType)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_chain(self, chain, excludeTotalDataChart=None, excludeTotalDataChartBreakdown=None, dataType=None):
        """Description: List all options dexs along with summaries of their volumes and dataType history data filtering by chain."""
        path = f"/overview/options/{chain}"
        params = self._get_params_dict(excludeTotalDataChart,excludeTotalDataChartBreakdown, dataType)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)

    def get_dexs_protocol(self, protocol, dataType=None):
        """Description: Get a summary of options dex volume with historical data."""
        path = f"/summary/options/{protocol}"
        params= self._get_params_dict(dataType)
        return self._send_request(endpoint=path, params=params, base_url=VOLUMES_BASE_URL)