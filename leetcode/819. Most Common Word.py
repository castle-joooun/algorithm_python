class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]
