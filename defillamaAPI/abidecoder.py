from .defillamaAPI import Base

ABI_DECODER_BASE_URL = "https://abi-decoder.llama.fi"
class ABIDecoder(Base):
    """"""
    def get_abi(self, functions=None, events=None):
        """Description: Get the ABI for a function or event signature."""
        path = '/fetch/signature'
        params = {}
        if functions is None and events is None:
            return {"message": "Kindly provide either functions or events"}
        params = self._get_params_dict(functions, events)
        return self._send_request(endpoint=path, params=params, base_url=ABI_DECODER_BASE_URL)
    
    def get_abi_contract(self, chain, address, functions=None, events=None):
        """Description: Get the verbose ABI for a function or event signature for a particular contract"""
        path = f'/fetch/contract/{chain}/{address}'
        if functions is None and events is None:
            return {"message": "Kindly provide either functions or events"}
        params = self._get_params_dict(functions, events)
        return self._send_request(endpoint=path, params=params, base_url=ABI_DECODER_BASE_URL)
