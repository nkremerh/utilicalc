from FelicificCalculus import Decision
from FelicificCalculus import EvaluateDecisions

if __name__ == "__main__":
    """
    Example 1: Trolley Problem
    A runaway trolley is barreling down the railway tracks. Ahead, on the tracks, there are five people tied up and 
    unable to move. The trolley is headed straight for them. You are standing some distance off in the train yard, 
    next to a lever. If you pull this lever, the trolley will switch to a different set of tracks. However, you notice 
    that there is one person on the side track. You have two options:

    1. Do nothing, and the trolley kills the five people on the main track.
    2. Pull the lever, diverting the trolley onto the side track where it will kill one person.
    """

    # Evaluate first without taking into account the egoistic/altruistic nature of the decision maker

    # Decision 1: Do nothing
    TrolleyProblem_DoNothing = Decision()

    # Agent 1: The five people on the main track killed by the trolley
    # isPleasure: False
    # Intensity: 10 (killed)
    # Duration: 1
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 5 -- 5 people
    TrolleyProblem_DoNothing.createAgent(False, 10, 1, 1, 1, 1, 0, 5)

    # Agent 2: The person on the side track not killed by the trolley
    # isPleasure: True
    # Intensity: 3 (saved)
    # Duration: 3
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: .8 -- This person may have survivor's guilt
    # p_intensity: 1.5
    # p_duration: 4
    # p_propinquity: 1
    # p_multiplier: 1
    # Multiplier: 1 -- 1 person
    TrolleyProblem_DoNothing.createAgent(True, 3, 3, 1, 1, 0, .8, 1, 0, 0, 0, 0, 1.5, 4, 1, 1)

    # Agent 3: You
    # isPleasure: False
    # Intensity: 1 -- You will feel guilty for not pulling the lever
    # Duration: 5
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 1 -- 1 person
    TrolleyProblem_DoNothing.createAgent(False, 1, 5, 1, 1, 0, 0, 1, is_decision_maker=True)

    # Agent 4: The family of the five people on the main track
    # isPleasure: False
    # Intensity: 5 -- Emotional pain of losing a loved one
    # Duration: 5
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 5 -- 5 people
    TrolleyProblem_DoNothing.createAgent(False, 5, 5, 1, 1, 0, 0, 5)

    # Decision 2: Pull the lever
    TrolleyProblem_PullLever = Decision()

    # Agent 1: The five people on the main track not killed by the trolley
    # isPleasure: True
    # Intensity: 3 (saved)
    # Duration: 3
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: .8 -- These people may have survivor's guilt
    # p_intensity: 1.5
    # p_duration: 4
    # p_propinquity: 1
    # p_multiplier: 5
    # Multiplier: 5
    TrolleyProblem_PullLever.createAgent(True, 3, 3, 1, 1, 0, .8, 5, 0, 0, 0, 0, 1.5, 4, 1, 5)

    # Agent 2: The one person on the side track killed by the trolley
    # isPleasure: False
    # Intensity: 10
    # Duration: 1
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 1
    # Multiplier: 1
    TrolleyProblem_PullLever.createAgent(False, 10, 1, 1, 1, 1, 0, 1)

    # Agent 3: You
    # isPleasure: False
    # Intensity: 3 -- You will feel guilty for killing the one person
    # Duration: 10
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 1 -- You will feel good about saving the five people
    # Multiplier: 1
    TrolleyProblem_PullLever.createAgent(False, 3, 10, 1, 1, 0, 1, 1, is_decision_maker=True)

    # Agent 4: The family of the one person on the side track
    # isPleasure: False
    # Intensity: 5 -- Emotional pain of losing a loved one
    # Duration: 5
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 1
    TrolleyProblem_PullLever.createAgent(False, 5, 5, 1, 1, 0, 0, 1)

    # Evaluate the decisions
    evaluate = EvaluateDecisions()
    evaluate.addDecision("Do Nothing", TrolleyProblem_DoNothing)
    evaluate.addDecision("Pull Lever", TrolleyProblem_PullLever)

    evaluate.printMoralValueForAllDecisions()
    evaluate.printDecisionWithHighestValue()

    # Evaluate again taking into account the egoistic nature of the decision maker
    evaluate.setSelfInterestScale(1)
    evaluate.printMoralValueForAllDecisions()
    evaluate.printDecisionWithHighestValue()

    # Evaluate again taking into account the altruistic nature of the decision maker
    evaluate.setSelfInterestScale(0)
    evaluate.printMoralValueForAllDecisions()
    evaluate.printDecisionWithHighestValue()
