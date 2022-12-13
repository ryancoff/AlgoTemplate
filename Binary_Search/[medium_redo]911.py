# 911. Online Election
"""
Releated-Id: 1146
"""
import bisect
times = [0, 5, 10, 15, 20, 25, 30]

print(bisect.bisect_right(times, 12))

# Lee Sol (99%)
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0): lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]

# Optimized Sol  (94.29)
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0  # leader, num votes for leader

        for p, t in itertools.izip(persons, times):
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:  # lead change
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t):
        i = bisect.bisect(self.A, (t, float('inf')), 1)
        return self.A[i-1][1]

# Sol for any number of candidates (85.32%)
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
  
        self.personNames = sorted(set(persons))
        self.votes = {p:[(0,0)] for p in self.personNames} # {time, currentVotes}
        self.rankBoard = []
 
        currentMaxVotes = 0
        recent_vote_ret = 0

        for (p,t) in zip(persons,times):

            current_candidate = self.votes[p] # candidate p
            current_candidate_votes = current_candidate[-1][1]+1 # total votes util now of p
            current_candidate.append((t,current_candidate_votes))

            if current_candidate_votes > currentMaxVotes:
                currentMaxVotes = current_candidate_votes
                self.rankBoard.append((t,p))
            
            elif current_candidate_votes == currentMaxVotes and recent_vote_ret < t:
                currentMaxVotes = current_candidate_votes
                self.rankBoard.append((t,p))


    def q(self, t: int) -> int:
        left, right = 0, len(self.rankBoard)
        while left < right:
            mid = left + (right-left)//2
            if self.rankBoard[mid][0] <= t: # binarySearch right # [0,0] [1,1] [2,1]
                left = mid + 1
            else:
                right = mid


# Sol for Two People
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.prefix_sum = 0
        self.prefix_sums = []
        for p in persons:
            self.prefix_sum += p
            self.prefix_sums.append(self.prefix_sum)
        self.times = times
        

    def q(self, t: int) -> int:

        left, right = 0, len(self.times)
        while left < right:
            mid = left + (right-left)//2
            if self.times[mid] <= t: # binarySearch right
                left = mid + 1
            else:
                right = mid

        idx = left - 1
        totalVoteOne = self.prefix_sums[idx]
        totalVoteZero = idx + 1 - totalVoteOne # 0-indexed
        if totalVoteOne == totalVoteZero:
            if self.persons[idx] == 0:
                return 0
            else:
                return 1
        elif totalVoteOne > totalVoteZero:
            return 1
        else:
            return 0