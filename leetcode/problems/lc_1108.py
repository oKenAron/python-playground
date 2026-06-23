class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_split = address.split(".")
        return "[.]".join(address_split)
