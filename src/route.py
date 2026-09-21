def calculate_distance(
    point1,
    point2
):

    latitude_difference = (
        point1[0] - point2[0]
    )

    longitude_difference = (
        point1[1] - point2[1]
    )

    return (
        latitude_difference ** 2
        + longitude_difference ** 2
    ) ** 0.5


def assess_route(
    route_points,
    risk_points
):

    high_risk_points = [

        point for point in risk_points

        if point["risk_level"] == "High"
    ]

    affected_points = []

    for route_point in route_points:

        for risk_point in high_risk_points:

            distance = calculate_distance(

                route_point,

                (
                    risk_point["lat"],
                    risk_point["lon"]
                )
            )

            if distance < 0.03:

                affected_points.append(
                    route_point
                )

                break

    if affected_points:

        status = "High-risk area detected"

        recommendation = (
            "⚠️ Consider an alternative route "
            "and follow official local guidance."
        )

    else:

        status = "No nearby high-risk point detected"

        recommendation = (
            "✅ Continue monitoring conditions "
            "during travel."
        )

    return {

        "route_status":
            status,

        "affected_points":
            affected_points,

        "recommendation":
            recommendation
    }


if __name__ == "__main__":

    route = [

        (19.9975, 73.7898),
        (20.0000, 73.7950),
        (20.0050, 73.8000)
    ]

    risks = [

        {
            "lat": 20.0005,
            "lon": 73.7955,
            "risk_level": "High"
        }
    ]

    result = assess_route(
        route,
        risks
    )

    print(result["route_status"])
    print(result["recommendation"])
