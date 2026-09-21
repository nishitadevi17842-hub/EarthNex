def fuse_risk(
    environmental_result,
    visual_result=None
):

    environmental_score = float(
        environmental_result["risk_score"]
    )

    if visual_result is None:

        final_score = environmental_score

    else:

        visual_score = float(
            visual_result["visual_score"]
        )

        final_score = (
            0.75 * environmental_score
            + 0.25 * visual_score
        )

    if final_score < 0.40:

        risk_level = "Low"

    elif final_score < 0.68:

        risk_level = "Medium"

    else:

        risk_level = "High"

    return {

        "combined_score":
            round(final_score, 3),

        "risk_level":
            risk_level
    }
