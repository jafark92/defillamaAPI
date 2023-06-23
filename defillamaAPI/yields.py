from .defillamaAPI import Base

YIELDS_BASE_URL = "https://yields.llama.fi"
class Yields(Base):
    """"""
    def get_all_pools(self):
        """
        Retrieve the latest data for all pools, including enriched information such as predictions
        
        Return
        ----------
        JSON response
        """
        path= "/pools"
        return self._send_request(endpoint=path, base_url=YIELDS_BASE_URL)

    def get_pool_chart(self, pool):
        """
        Get historical APY and TVL of a pool

        Parameters
        ----------
        pool : string (path)
            pool id, can be retrieved from /pools (property is called pool)
            Example: 747c1d2a-c668-4682-b9f9-296708a3dd90

        Return
        ----------
        JSON response
        """
        path= f"/chart/{pool}"
        return self._send_request(endpoint=path, base_url=YIELDS_BASE_URL)
