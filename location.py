import geocoder

def get_current_city():
    try:
        g = geocoder.ip("me")

        if g.city:
            return g.city

        return "Delhi"

    except:
        return "Delhi"