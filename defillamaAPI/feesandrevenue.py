from .defillamaAPI import Base

FEESANDREVENUE_BASE_URL = "https://api.llama.fi"
class FeesAndRevenue(Base):
    """"""
    def get_all_protocols(self, **args):
        """Description: List all protocols along with summaries of their fees and revenue and dataType history data."""
        path = "/overview/fees"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=FEESANDREVENUE_BASE_URL)

    def get_protocols_chain(self, chain, **args):
        """Description: List all protocols along with summaries of their fees and revenue and dataType history data by chain."""
        path = f"/overview/fees/{chain}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=FEESANDREVENUE_BASE_URL)

    def get_summary_protocol(self, protocol, **args):
        """Description: Get a summary of protocol fees and revenue with historical data."""
        path = f"/summary/fees/{protocol}"
        params = self._get_params_dict(**args)
        return self._send_request(endpoint=path, params=params, base_url=FEESANDREVENUE_BASE_URL)