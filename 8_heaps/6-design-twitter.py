class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        users = [userId] + self.followees[userId]
        for user in users:
            feed += self.tweets[user]

        tweets = heapq.nlargest(10, feed, key=lambda val: val[1])
        return [tweet[0] for tweet in tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.followees[followerId]:
            return
        self.followees[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
