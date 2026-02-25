import json

INPUT = "data/min_time_route.json"
OUTPUT = "data/min_time_route.geojson"

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

# WRT route points (expects list of dicts with lat/lon)
coords = [[p["lon"], p["lat"]] for p in data["route"]]  # GeoJSON order: lon, lat

geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "WRT final route"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": coords
            }
        }
    ]
}

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(geojson, f, indent=2)

print("✅ Written:", OUTPUT)