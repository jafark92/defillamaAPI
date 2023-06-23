from .defillamaAPI import Base

ABI_DECODER_BASE_URL = "https://abi-decoder.llama.fi"
class ABIDecoder(Base):
    """"""
    def get_abi(self, functions=None, events=None):
        """
        Get the ABI for a function or event signature.

        Parameters
        ----------
        functions : string (query)
            function 4 byte signatures, you can add many signatures by joining them with ','
            Example: 0x23b872dd,0x18fccc76,0xb6b55f25,0xf5d07b60

        events : string (query)
            event signatures, you can add many signatures by joining them with ','
            Example: 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef,0xc42079f94a6350d7e6235f29174924f928cc2ac818eb64fed8004e115fbcca67,0x4cc7e95e48af62690313a0733e93308ac9a73326bc3c29f1788b1191c376d5b6
        
        Return
        ----------
        JSON response
        """
        path = '/fetch/signature'
        params = {}
        if functions is None and events is None:
            return {"message": "Kindly provide either functions or events"}
        params = self._get_params_dict(functions, events)
        return self._send_request(endpoint=path, params=params, base_url=ABI_DECODER_BASE_URL)
    
    def get_abi_contract(self, chain, address, functions=None, events=None):
        """
        Get the verbose ABI for a function or event signature for a particular contract

        Parameters
        ----------
        chain : string (path)
            Chain the smart contract is located in
            Available values: arbitrum, avalanche, bsc, celo, ethereum, fantom, optimism, polygon, tron
            Example: ethereum

        address : string (path)
            Address of the smart contract
            Example: 0x02f7bd798e765369a9d204e9095b2a526ef01667

        functions : string (query)
            function 4 byte signatures, you can add many signatures by joining them with ','
            Example: 0xf43f523a,0x95d89b41,0x95d89b41,0x70a08231,0x70a08231

        events : string (query)
            event signatures, you can add many signatures by joining them with ','
            Example: 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef,0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925
        
        Return
        ----------
        JSON response
        """
        path = f'/fetch/contract/{chain}/{address}'
        if functions is None and events is None:
            return {"message": "Kindly provide either functions or events"}
        params = self._get_params_dict(functions, events)
        return self._send_request(endpoint=path, params=params, base_url=ABI_DECODER_BASE_URL)
