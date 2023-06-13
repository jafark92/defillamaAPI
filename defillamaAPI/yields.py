from .defillamaAPI import Base

YIELDS_BASE_URL = "https://yields.llama.fi"
class Yields(Base):
    """"""
    def get_all_pools(self):
        """Description: Retrieve the latest data for all pools, including enriched information such as predictions"""
        path= "/pools"
        return self._send_request(endpoint=path, base_url=YIELDS_BASE_URL)

    def get_pool_chart(self, pool):
        """Description: Get historical APY and TVL of a pool"""
        path= f"/chart/{pool}"
        return self._send_request(endpoint=path, base_url=YIELDS_BASE_URL)
