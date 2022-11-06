"""
The purpose of this class is to provide a set of methods for calculating the moral value of an action.
The moral value of an action is the sum of the moral value of the consequences of the action.
We will calculate this by using Jeremy Bentham's formula, called the "Felicific Calculus", which is defined as such:

Variables:
    For pleasure:
    I = the intensity of pleasure
    D = the duration of pleasure
    C = certainty of pleasure
    N = propinquity or nearness of pleasure
    F = fecundity or probability of 2nd order pleasure (the pleasure stemming from the pleasure)
    P = purity or probability of 2nd order pain (the pain stemming from the pleasure)
    M = multiplier for number of people affected equally by the pleasure

    For pain:
    I = the intensity of pain
    D = the duration of pain
    C = certainty of pain
    N = propinquity or nearness of pain
    F = fecundity or probability of 2nd order pain (the pain stemming from the pain)
    P = purity or probability of 2nd order pleasure (the pleasure stemming from the pain)
    M = multiplier for number of people affected equally by the pain

Formula:
    For each person affected by the action, the moral value of the action is calculated as follows:
        C * (I * D * N * M) must be calculated for each pleasure and pain, and for each 2nd order pleasure and pain.
        For 2nd order pleasure and pain, the same formula is used, but C is replaced with F or P, respectively.
        Pain is calculated as a negative value, and pleasure is calculated as a positive value.
        The sum of all of these values is the moral value of the action for this person.

    All of these values are summed together to get the total moral value of an action.
"""

"""
Consequence of an action
"""


class Consequence:
    def __init__(self, intensity, duration, certainty, propinquity, multiplier, isPleasure):
        self.intensity = intensity
        self.duration = duration
        self.certainty = certainty
        self.propinquity = propinquity  # TODO: Change to 1/propinquity?
        self.multiplier = multiplier
        self.isPleasure = isPleasure

    def getMoralValue(self):
        if self.isPleasure:
            return self.certainty * (self.intensity * self.duration * self.propinquity * self.multiplier)
        else:
            return -1 * self.certainty * (self.intensity * self.duration * self.propinquity * self.multiplier)


"""
Agent(s) affected by an action, each instance has a list of consequences
Fecundity and purity (and their corresponding variables f_... and p_...) are only used for 2nd order consequences
Fecundity and purity are the probability of a 2nd order consequence.
Each Agents instance has a list of consequences, which are instances of the Consequence class and are added up by
the getMoralValue method to get the moral value of the action for this agent.
"""


class Agent:
    def __init__(self, isPleasure, intensity, duration, certainty, propinquity, fecundity, purity, multiplier,
                 f_intensity=0, f_duration=0, f_propinquity=0, f_multiplier=0,
                 p_intensity=0, p_duration=0, p_propinquity=0, p_multiplier=0):  # TODO: Are f_multiplier and p_multiplier necessary?

        self.consequences = []

        self.consequences.append(Consequence(intensity, duration, certainty, propinquity, multiplier, isPleasure))

        # The following lines are used to add 2nd order consequences.
        if isPleasure:
            self.consequences.append(
                Consequence(f_intensity, f_duration, fecundity, f_propinquity, f_multiplier, True))

            self.consequences.append(Consequence(p_intensity, p_duration, purity, p_propinquity, p_multiplier, False))

        else:
            self.consequences.append(
                Consequence(f_intensity, f_duration, fecundity, f_propinquity, f_multiplier, False))

            self.consequences.append(Consequence(p_intensity, p_duration, purity, p_propinquity, p_multiplier, True))

    def getMoralValue(self):
        moralValue = 0

        for consequence in self.consequences:
            moralValue += consequence.getMoralValue()

        return moralValue


"""
Decision to be made, which has consequences for multiple agents
self_interest_scale is a value between 0 and 1, which is used to weight the consequences of the decision in order to
look at the consequences for the decision maker from an egoistic (1) or altruistic (0) perspective.
"""


class Decision:
    def __init__(self, self_interest_scale=None):
        self.self_interest_scale = self_interest_scale
        self.agents = []

    def createAgent(self, isPleasure, intensity, duration, certainty, propinquity, fecundity, purity, multiplier,
                    f_intensity=0, f_duration=0, f_propinquity=0, f_multiplier=0,
                    p_intensity=0, p_duration=0, p_propinquity=0, p_multiplier=0, is_decision_maker=False):

        if is_decision_maker:
            self.agents.append(
                (Agent(isPleasure, intensity, duration, certainty, propinquity, fecundity, purity, multiplier,
                       f_intensity, f_duration, f_propinquity, f_multiplier,
                       p_intensity, p_duration, p_propinquity, p_multiplier), True))

        else:
            self.agents.append(
                (Agent(isPleasure, intensity, duration, certainty, propinquity, fecundity, purity, multiplier,
                       f_intensity, f_duration, f_propinquity, f_multiplier,
                       p_intensity, p_duration, p_propinquity, p_multiplier), False))

    def getMoralValue(self):
        totalMoralValue = 0

        for agent in self.agents:
            if self.self_interest_scale is not None:
                if agent[1]:
                    totalMoralValue += agent[0].getMoralValue() * self.self_interest_scale
                else:
                    totalMoralValue += agent[0].getMoralValue() * (1 - self.self_interest_scale)
            else:
                totalMoralValue += agent[0].getMoralValue()

        return round(totalMoralValue, 2)

    def setSelfInterestScale(self, self_interest_scale):
        self.self_interest_scale = self_interest_scale

    def checkForDecisionMaker(self):
        for agent in self.agents:
            if agent[1]:
                return True
        return False



"""
Evaluates multiple decisions can print the decision with the highest moral value
Decisions are created outside of this class and added through addDecision
"""


class EvaluateDecisions:
    def __init__(self):
        self.decisions = []

    def addDecision(self, decision_name, decision):
        self.decisions.append((decision_name, decision))

    def setSelfInterestScale(self, self_interest_scale):
        if self_interest_scale > 1 or self_interest_scale < 0:
            raise ValueError("Self interest scale must be between 0 and 1.")

        for decision in self.decisions:
            if not decision[1].checkForDecisionMaker():
                print("Warning: Decision " + decision[0] + " does not have a decision maker.")

        if self_interest_scale == 0:
            print("Set self interest to Altruistic")
        elif self_interest_scale == 1:
            print("Set self interest to Egoistic")

        for decision in self.decisions:
            decision[1].setSelfInterestScale(self_interest_scale)

    def printMoralValueForAllDecisions(self):
        for decision in self.decisions:
            print(decision[0] + ": " + str(decision[1].getMoralValue()))

    def printBestDecision(self):
        bestDecisionName, bestDecision = max(self.decisions, key=lambda x: x[1].getMoralValue())

        print("The best decision is: " + bestDecisionName + ". with a moral value of " + str(
            bestDecision.getMoralValue()))

        if bestDecision.self_interest_scale is not None:
            print("This decision was made with a self interest scale of " + str(bestDecision.self_interest_scale))
        print()
