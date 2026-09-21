from datetime import datetime


def generate_alert(
    risk_level,
    location="Monitored Area"
):

    messages = {

        "Low":
            "Current conditions indicate lower observed risk.",

        "Medium":
            "Increased monitoring is recommended.",

        "High":
            "High observed risk conditions detected. "
            "Follow official safety guidance."
    }

    alert = {

        "timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "location":
            location,

        "risk_level":
            risk_level,

        "message":
            messages.get(
                risk_level,
                "Risk status unavailable."
            )
    }

    return alert


if __name__ == "__main__":

    result = generate_alert(
        "High",
        "Test Location"
    )

    print("🚨 EARTHNEX ALERT")
    print(result["message"])
