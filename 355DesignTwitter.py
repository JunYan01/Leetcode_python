# 355. Design Twitter


import queue

class Twitter:
    timestamp = 0
# Failed trying for a subclass to call another subclass (inside a class)   
#     class Tweet:
#         def __init__(self,ID,time):
#             self.id = ID
#             self.time = time
#             self.next = None
            
    
#     class User:
#         def __init__(self,userID):
#             self.id = userID
#             self.follower = []
#             self.head = None
        
#         def follow(self,userID):
#             self.follower.append(userID)
            
#         def unfollow(self,userID):
#             if userID != self.id and userID in self.follower:
#                 self.follower.remove(userID)
                
#         def post(self, tweetID):
#             twt = Tweet(tweetID,timestamp)
#             timestamp += 1
#             twt.next = self.head
#             self.head = twt
            
                
        
        
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetDict = {}
        self.users = {}
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            # self.users[userId] = self.User(userId)
            self.users[userId] = User(userId)
        self.users[userId].post(tweetId)    
        
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        if userId not in self.users:
            return res
        followers = self.users[userId].follower
        pq = queue.PriorityQueue()
        
        # print(userId,followers)
        for id in followers:
            twt = self.users[id].head
            if twt: pq.put(twt)
        
        while not pq.empty():
            if len(res) == 10:
                break
            twt = pq.get()
            res.append(twt.id)
            if twt.next:
                pq.put(twt.next)
        
        
        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        self.users[followerId].follow(followeeId)
        # print(followeeId,followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)

class Tweet:
    def __init__(self,ID,time):
        self.id = ID
        self.time = time
        self.next = None
        
    def __lt__(self,other):
        return self.time > other.time
            
    
class User:
    def __init__(self,userID):
        self.id = userID
        self.follower = [userID]
        self.head = None
        
    def follow(self,userID):
        if userID not in self.follower:
            self.follower.append(userID)
        
        
            
    def unfollow(self,userID):
        if userID != self.id and userID in self.follower:
            self.follower.remove(userID)
                
    def post(self, tweetID):
        twt = Tweet(tweetID,Twitter.timestamp)
        Twitter.timestamp += 1
        twt.next = self.head
        self.head = twt
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)