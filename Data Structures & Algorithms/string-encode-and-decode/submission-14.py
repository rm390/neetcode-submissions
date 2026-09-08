class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '<>'
        return '///'.join(strs)
    def decode(self, s: str) -> List[str]:
        a = s.split("///")

        if a == ["<>"]:
            return []
        
        return a

