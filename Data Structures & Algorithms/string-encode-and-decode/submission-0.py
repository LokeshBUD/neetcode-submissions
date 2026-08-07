class Solution:
    """
    This problem is basically telling us to encode and decode. Encoding essentially what we are trying to do is taking the length of each string given in the input array, and we are essentially combining all of that and providing an encoded string. The way that we are encoding it is basically telling the decoder how to separate the strings rather than adding a prop, like a normal ciphering to it. 

    The idea for encoding is to take the length of each input string and add that to the front of the variable, in front of that string, so that the decoder knows how many characters to look for in each word. 
    """
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res) 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res