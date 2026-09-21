import folium


def create_risk_map(
    latitude,
    longitude,
    risk_level,
    zoom=10
):

    risk_colors = {

        "Low": "green",
        "Medium": "orange",
        "High": "red"
    }

    map_object = folium.Map(

        location=[
            latitude,
            longitude
        ],

        zoom_start=zoom
    )

    color = risk_colors.get(
        risk_level,
        "blue"
    )

    folium.Marker(

        location=[
            latitude,
            longitude
        ],

        popup=(
            f"🌍 EarthNex<br>"
            f"Risk Level: {risk_level}"
        ),

        icon=folium.Icon(
            color=color
        )

    ).add_to(map_object)

    return map_object


if __name__ == "__main__":

    risk_map = create_risk_map(
        19.9975,
        73.7898,
        "High"
    )

    risk_map.save(
        "earthnex_risk_map.html"
    )

    print(
        "🗺️ Risk map created: "
        "earthnex_risk_map.html"
    )
