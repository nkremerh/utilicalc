import felicific_calculus as fc

if __name__ == "__main__":
    """
    Source: https://icebreakerideas.com/moral-dilemma-questions/
    
    You are on a cruise and the ship encounters an unexpected storm. The storm continues to rage and eventually you and the 
    other passengers are told you must head to the lifeboats and abandon ship. As people begin to line up, you realize some 
    lines have fewer people, some have families, and some seem to have younger, single people. You know you are strong and 
    capable. Do you choose to help a group composed of three families with a few young children, a group of seniors who 
    obviously could use your help, or go with the young, strong people, with whom you might have a better chance of survival?
    """

    # Decision 1: Help the families
    lifeboatHelpFamilies = fc.Decision()

    # Agent 1: The families
    # isPleasure: True
    # Intensity: 5 -- The families will be grateful to have your help
    # Duration: 2
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 1 -- The families may do good things in the future as they will be alive
    # Purity: 0
    # f_intensity: 3
    # f_duration: 8
    # f_propinquity: 1
    # f_multiplier: 9
    # Multiplier: 9 -- 3 families with 3 people each
    lifeboatHelpFamilies.createAgent(True, 5, 3, 1, 1, 1, 0, 9, 0, 0, 0, 0, 3, 8, 1, 9)

    # Agent 2: The seniors
    # isPleasure: False
    # Intensity: 10 -- The seniors may not survive the storm
    # Duration: 1
    # Certainty: .7 -- The seniors may be able to help themselves - 30% chance they will survive
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 5 -- 5 seniors
    lifeboatHelpFamilies.createAgent(False, 10, 1, .7, 1, 0, 0, 5)

    # Agent 3: The young, strong people
    # isPleasure: False
    # Intensity: 1 -- They will most likely survive the storm, but could still use your help
    # Duration: 2
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 5 -- 5 young, strong people
    lifeboatHelpFamilies.createAgent(False, 1, 2, 1, 1, 0, 0, 5)

    # Agent 4: You
    # isPleasure: False
    # Intensity: 10 -- You may not survive the storm
    # Duration: 1
    # Certainty: .5 -- 50% chance you will survive
    # Propinquity: 1
    # Fecundity: 0
    # Purity: .5 -- You will feel good about helping the families
    # p_intensity: 1.5
    # p_duration: 4
    # p_propinquity: 1
    # p_multiplier: 1
    # Multiplier: 1
    lifeboatHelpFamilies.createAgent(False, 10, 1, .5, 1, 0, .5, 1, 0, 0, 0, 0, 1.5, 4, 1, 1, isDecisionMaker=True)

    # Decision 2: Help the seniors
    lifeboatHelpSeniors = fc.Decision()

    # Agent 1: The families
    # isPleasure: False
    # Intensity: 10 -- The families may not survive the storm
    # Duration: 1
    # Certainty: .5 -- The families may be able to help themselves - 50% chance they will survive
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 9 -- 3 families with 3 people each
    lifeboatHelpSeniors.createAgent(False, 10, 1, .5, 1, 0, 0, 9)

    # Agent 2: The seniors
    # isPleasure: True
    # Intensity: 5 -- The seniors will be grateful to have your help
    # Duration: 2
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 1 -- The seniors may do good things in the future as they will be alive
    # Purity: 0
    # f_intensity: 3
    # f_duration: 4 -- The seniors will be grateful for a shorter time, as they are older
    # f_propinquity: 1
    # f_multiplier: 5
    # Multiplier: 5 -- 5 seniors
    lifeboatHelpSeniors.createAgent(True, 5, 3, 1, 1, 1, 0, 5, 0, 0, 0, 0, 3, 4, 1, 5)

    # Agent 3: The young, strong people
    # isPleasure: False
    # Intensity: 1 -- They will most likely survive the storm, but could still use your help
    # Duration: 2
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 5 -- 5 young, strong people
    lifeboatHelpSeniors.createAgent(False, 1, 2, 1, 1, 0, 0, 5)

    # Agent 4: You
    # isPleasure: False
    # Intensity: 10 -- You may not survive the storm
    # Duration: 1
    # Certainty: .7 -- 30% chance you will survive
    # Propinquity: 1
    # Fecundity: 0
    # Purity: .3 -- You will feel good about helping the seniors - 30% chance you will survive
    # p_intensity: 1.5
    # p_duration: 4
    # p_propinquity: 1
    # p_multiplier: 1
    # Multiplier: 1
    lifeboatHelpSeniors.createAgent(False, 10, 1, .7, 1, 0, .3, 1, 0, 0, 0, 0, 1.5, 4, 1, 1, isDecisionMaker=True)

    # Decision 3: Help the young, strong people
    lifeboatHelpYoung = fc.Decision()

    # Agent 1: The families
    # isPleasure: False
    # Intensity: 10 -- The families may not survive the storm
    # Duration: 1
    # Certainty: .5 -- The families may be able to help themselves - 50% chance they will survive
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 9 -- 3 families with 3 people each
    lifeboatHelpYoung.createAgent(False, 10, 1, .5, 1, 0, 0, 9)

    # Agent 2: The seniors
    # isPleasure: False
    # Intensity: 10 -- The seniors may not survive the storm
    # Duration: 1
    # Certainty: .7 -- The seniors may be able to help themselves - 30% chance they will survive
    # Propinquity: 1
    # Fecundity: 0
    # Purity: 0
    # Multiplier: 5 -- 5 seniors
    lifeboatHelpYoung.createAgent(False, 10, 1, .7, 1, 0, 0, 5)

    # Agent 3: The young, strong people
    # isPleasure: True
    # Intensity: 2 -- The young, strong people will be grateful to have your help
    # Duration: 2
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 0 -- They would have survived anyway
    # Purity: 0
    # Multiplier: 5 -- 5 young, strong people
    lifeboatHelpYoung.createAgent(True, 2, 2, 1, 1, 0, 0, 5)

    # Agent 4: You
    # isPleasure: True
    # Intensity: 5 -- You will feel good about helping the young, strong people
    # Duration: 1
    # Certainty: 1
    # Propinquity: 1
    # Fecundity: 1 -- You will do good things in the future as you will be alive
    # Purity: 0
    # p_intensity: 1.5
    # p_duration: 8
    # p_propinquity: 1
    # p_multiplier: 1
    # Multiplier: 1
    lifeboatHelpYoung.createAgent(True, 5, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1.5, 8, 1, 1, isDecisionMaker=True)

    # Evaluate the decisions
    evaluate = fc.EvaluateDecisions()
    evaluate.addDecision("Help Families", lifeboatHelpFamilies)
    evaluate.addDecision("Help Seniors", lifeboatHelpSeniors)
    evaluate.addDecision("Help young people & maximize own survival", lifeboatHelpYoung)

    # Print the results
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




