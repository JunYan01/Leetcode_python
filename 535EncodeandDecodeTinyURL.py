535Encode and Decode TinyURL

class Codec:
    
    def __init__(self):
        self.pool = itertools.permutations(string.printable, 6)
        self.cache = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = next(self.pool)
        self.cache[key] = longUrl
        return key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cache[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))