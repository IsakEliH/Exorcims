class HighScores:
    def __init__(self, scores: list):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        highest = []
        relative = self.scores[:]

        if len(relative) >= 3:
            for _ in range(3):
                high_score = max(relative)
                highest.append(high_score)
                relative.remove(high_score)

            return highest
        else:
            return sorted(relative, reverse=True)
