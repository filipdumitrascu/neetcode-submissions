import heapq
import collections


class Twitter:
    """Max Heap and Hashmaps

    Soluția de bază bazată pe heap analizează toate tweet-urile tuturor celor
    urmăriți, ceea ce este suficient de rapid, dar poate fi îmbunătățită.

    Observație cheie:
    -Fiecare utilizator este interesat doar de cele mai recente 10 tweet-uri,
    deoarece fluxul de știri afișează cel mult 10 elemente.
    -Așadar, pentru fiecare utilizator, în loc să stocăm toate tweet-urile,
    să stocăm doar cele mai recente 10 tweet-uri ale acestuia.
    -Astfel se reduc:
     Utilizarea memoriei
     Operațiunile asupra heap-ului
     Timpul necesar pentru fiecare interogare

    Trucul:
    -Când un utilizator publică un tweet, adaugă-i un timestamp (număr) în
    ordine descrescătoare și păstrează doar ultimele 10 tweet-uri.
    -La preluarea fluxului de știri:
     Dacă utilizatorul urmărește multe persoane (>= 10), păstrează doar cei 10
     utilizatori urmăriți cu cel mai recent tweet, folosind un max-heap de
     dimensiune 10.
     -Această abordare este sigură: dacă cel mai recent tweet al unei persoane
    urmărite este deja prea vechi, niciunul dintre tweet-urile sale mai vechi
    nu poate intra în lista finală de 10.
     -În caz contrar, introduceți cel mai recent tweet de la fiecare persoană
    urmărită într-un min-heap și continuați să extindeți lista cu același
    utilizator după fiecare extragere.
    -În ambele cazuri, nu procesăm niciodată mai mult de 10 tweet-uri per
    persoană urmărită și nu extragem niciodată mai mult de 10 rezultate.

    Acest lucru face ca metoda să fie foarte rapidă chiar și atunci când
    utilizatorii postează multe tweet-uri.

    __init__:     T = O(1), S = O(1)
    postTweet:    T = O(1), S = O(1)
    getNewsFeed:  T = O(f log f), S = O(f)
    follow:       T = O(1), S = O(1)
    unfollow:     T = O(1), S = O(1)
    """

    def __init__(self):
        """
        A hashmap with every user mapped to a list with every tweet he posted
        A hashmap with every user mapped to a hashset with every user he follows
        A max heap with timestamps and tweet_id
        """
        self.time = 0
        self.tweet_map = collections.defaultdict(list)  # user_id -> list of [time, tweet_ids]
        self.follow_map = collections.defaultdict(set)  # user_id -> set of folowee_id

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet_map[user_id].append([self.time, tweet_id])
        self.time -= 1  # minus for max heap in python

    def getNewsFeed(self, user_id: int) -> list[int]:
        res = []  # ordered starting from recent
        min_heap = []

        self.follow_map[user_id].add(user_id)
        for followee_id in self.follow_map[user_id]:
            if followee_id in self.tweet_map:
                last_tweet_posted = len(self.tweet_map[followee_id]) - 1
                time, tweet_id = self.tweet_map[followee_id][last_tweet_posted]

                # takes every last tweet posted from every followee (leetcode 23)
                min_heap.append([time, tweet_id, followee_id, last_tweet_posted - 1])

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            time, tweet_id, followee_id, last_tweet_posted = heapq.heappop(min_heap)
            res.append(tweet_id)

            if last_tweet_posted >= 0:
                time, tweet_id = self.tweet_map[followee_id][last_tweet_posted]
                heapq.heappush(min_heap, [time, tweet_id, followee_id, last_tweet_posted - 1])

        return res

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].add(followee_id) 

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.follow_map[follower_id]:
            self.follow_map[follower_id].remove(followee_id)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
