from .defillamaAPI import Base

BRIDGES_BASE_URL = "https://bridges.llama.fi"
class Bridges(Base):
    """"""
    def get_all_bridges(self, includeChains=True):
        """Description: List all bridges along with summaries of recent bridge volumes."""
        path = '/bridges'
        params = {"includeChains": includeChains}
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume_summary(self, id):
        """Description: Get a summary of bridge volume and volume breakdown by chain."""
        path = f'/bridge/{id}'
        return self._send_request(endpoint=path, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume(self, chain, id=None):
        """Description: Get historical volumes for a bridge, chain, or bridge on a particular chain."""
        path = f'/bridgevolume/{chain}'
        params = {}
        if id: params.update({"id":id})
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)

    def get_bridgevolume_token(self, timestamp, chain, id=None):
        """Description: Get a 24hr token and address volume breakdown for a bridge."""
        path = f"/bridgedaystats/{timestamp}/{chain}"
        params = {}
        if id: params.update({"id":id})
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)
    
    def get_all_transactions(self, id, starttimestamp=None, endtimestamp=None, sourcechain=None, address=None, limit=None):
        """Description: Get all transactions for a bridge within a date range."""
        path = f'/transactions/{id}'
        params = {}
        if id: params.update({"starttimestamp":starttimestamp})
        if id: params.update({"endtimestamp":endtimestamp})
        if id: params.update({"sourcechain":sourcechain})
        if id: params.update({"address":address})
        if id: params.update({"limit":limit})
        return self._send_request(endpoint=path, params=params, base_url=BRIDGES_BASE_URL)
