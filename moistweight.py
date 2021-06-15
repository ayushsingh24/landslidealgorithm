def Weight(moisture):

    w = moisture
    Gs = 0.993
    γw = 9807 # Unit weight of water in N/m^3
    e = 0.5

    # Unit moist weight of soil

    γt = ((1+w)*(Gs*γw))/(1+e)

    γt = round((γt /1000),2)

    # Saturated unit weight of soil

    γs = ((Gs+e)*γw) / (1+e)

    γs = round((γs / 1000),2)

    γwr = round((γw/1000),2)

    weight = [γwr,γt,γs]

    return(weight)