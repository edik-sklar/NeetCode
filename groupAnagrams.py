from collections import deque, defaultdict

class Solution:
    from collections import defaultdict


    def groupAnagrams(self, strs: list[str]):
        results = defaultdict(list)
        for w in strs:
            key = tuple(sorted(w))  # ("a","e","t") is the key for "eat","tea","ate"
            results[key].append(w)
        return list(results.values())

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        # defaultdict automatically creates [] for new keys
        results = defaultdict(list)
        for w in strs:
            # build a temp dict that with values as count for unique chars in the word
            w_dict = {}
            # iterate chars over sorted characters in a word
            for char in sorted(w):
                w_dict[char] = 1 + w_dict.get(char, 0)
            # creating a unique key for result dict from the temp dict
            key = "".join([f"{k}{v}" for k, v in w_dict.items()])
            results[key].append(w)
        return list(results.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))
print(s.groupAnagrams2(strs))
        # li_deque = deque()
        # counter_list = []
        # li_li = [sorted(w) for w in strs]
        #     for c in li_li:
        #         # w_list.sort()
        #         w_dict = {}
        #         # print(w_list)
        #         for i, c in enumerate(w_list):
        #             w_dict[w] = 1 + w_dict.get(w, 0)
        #         print(w_dict)
        #         li_deque.append(w_dict)
        # while li_deque:
        #     same = []
        #     d = li_deque.popleft()
        #     same.append(d)
        #     for dd in li_deque:
        #         if  dd == d:
        #             same.append(dd)
        #     li_deque = deque([ddd for ddd in li_deque if ddd != d])
        #     counter_list.append(same)
        # print(counter_list)











# results = []
# for i, w in enumerate(strs):
#     for c in sorted(w):
#         w_dict[c] = 1+ w_dict.get(c, 0)
#     results.append((w_dict, i))
#
# results = []
# for i, w in enumerate(strs):
#     w_dict = {} # Reset for every word
#     for c in sorted(w):
#         w_dict[c] = 1 + w_dict.get(c, 0)
#     key = "".join([f"{k}{v}" for k, v in w_dict.items()])
#     # Output for "banana": "a3b1n2"
#
#     results.append((key, i))
