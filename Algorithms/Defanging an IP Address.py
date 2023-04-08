class Solution:
    def defangIPaddr(self, address: str) -> str:
        address1=[]
        for i in address:
            address1=address.replace(".","[.]")
        return address1