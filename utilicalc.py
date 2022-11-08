#! /usr/bin/python

def nextOrderConsequences(consequences):
    furtherConsequences = []
    for consequence in consequences:
        furtherConsequences.append(0)
    return furtherConsequences

def utilityCalculus(act, agents, consequences):
    score = 0
    for agent in agents:
        agentScore = 0
        agentConsequences = consequences[agent]
        for consequence in agentConsequences:
            agentScore = agentScore + consequence
        furtherConsequences = nextOrderConsequences(agentConsequences)
        for consequence in furtherConsequences:
            agentScore = agentScore + consequence
        print("Score for {0} is {1}.".format(agent, agentScore))
        score = score + agentScore
    print("Score for {0} is {1}.".format(act, score))
    return score

utilityCalculus("Buying a pack of cigarettes", ["Me", "Neighbor 1", "Neighbor 2", "Stranger 1", "Stranger 2", "Tobacco Company", "Gas Station"], {"Me": [3, -5, -1], "Neighbor 1": [-2], "Neighbor 2": [-2], "Stranger 1": [-2], "Stranger 2": [-4], "Tobacco Company": [2], "Gas Station": [3]})
