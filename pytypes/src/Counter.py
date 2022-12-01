from __future__ import annotations

import random 
from dataclasses import dataclass 
from typing import List, NewType, Optional, overload, Union
from typing_extensions import Literal

from woke.testing.contract import Contract, Library, TransactionObject, Address, Wei, Account, ChainInterface

from enum import IntEnum
from woke.testing.pytypes_generator import RequestType



class Counter(Contract):
    _abi = {b'\xd0\x9d\xe0\x8a': {'inputs': [], 'name': 'increment', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\x83\x81\xf5\x8a': {'inputs': [], 'name': 'number', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'?\xb5\xc1\xcb': {'inputs': [{'internalType': 'uint256', 'name': 'newNumber', 'type': 'uint256'}], 'name': 'setNumber', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _bytecode = "608060405234801561001057600080fd5b506101f2806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c80633fb5c1cb146100465780638381f58a14610062578063d09de08a14610080575b600080fd5b610060600480360381019061005b91906100ee565b61008a565b005b61006a610094565b604051610077919061012a565b60405180910390f35b61008861009a565b005b8060008190555050565b60005481565b6000808154809291906100ac90610174565b9190505550565b600080fd5b6000819050919050565b6100cb816100b8565b81146100d657600080fd5b50565b6000813590506100e8816100c2565b92915050565b600060208284031215610104576101036100b3565b5b6000610112848285016100d9565b91505092915050565b610124816100b8565b82525050565b600060208201905061013f600083018461011b565b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b600061017f826100b8565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82036101b1576101b0610145565b5b60018201905091905056fea2646970667358221220b785e89151baf99037c8e42edff8f4575e9ad92799cd8c12a62a471aa919b9b764736f6c63430008110033"

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", chain: Optional[ChainInterface] = None) -> Counter:
        return cls._deploy([], from_, value, gas_limit, {}, chain)

    @classmethod
    def bytecode(cls) -> bytes:
        return cls._get_bytecode({})

    @overload
    def number(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> int:
        ...

    @overload
    def number(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def number(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='call') -> Union[int, TransactionObject]:
        """
        Returns:
            uint256
        """
        return self._transact("8381f58a", [], return_tx, request_type, int, from_, to, value, gas_limit) if not request_type == 'call' else self._call("8381f58a", [], return_tx, int, from_, to, value, gas_limit)

    @overload
    def setNumber(self, newNumber: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def setNumber(self, newNumber: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def setNumber(self, newNumber: int, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        """
        Args:
            newNumber: uint256
        """
        return self._transact("3fb5c1cb", [newNumber], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("3fb5c1cb", [newNumber], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> None:
        ...

    @overload
    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=True, request_type: RequestType='default') -> TransactionObject:
        ...

    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: Wei = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool=False, request_type: RequestType='default') -> Union[None, TransactionObject]:
        return self._transact("d09de08a", [], return_tx, request_type, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("d09de08a", [], return_tx, type(None), from_, to, value, gas_limit)

