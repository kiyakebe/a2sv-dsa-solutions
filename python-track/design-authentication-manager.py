class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.authentication = {}
        self.time_to_live = timeToLive

        # count the tokens that are going to expire at the saame time
        self.token_expiration_count = collections.defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.authentication[tokenId] = currentTime
        self.token_expiration_count[currentTime + self.time_to_live] += 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.authentication and self.authentication[tokenId] + self.time_to_live > currentTime:

            self.token_expiration_count[self.authentication[tokenId] + self.time_to_live] -= 1

            if self.token_expiration_count[self.authentication[tokenId] + self.time_to_live] == 0:
                del self.token_expiration_count[self.authentication[tokenId] + self.time_to_live]

            self.authentication[tokenId] = currentTime
            self.token_expiration_count[currentTime + self.time_to_live] += 1

    def countUnexpiredTokens(self, currentTime: int) -> int:
        total_unexpired_token = 0
        for i, val in self.token_expiration_count.items():
            if i > currentTime:
                total_unexpired_token += val
        return total_unexpired_token



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)