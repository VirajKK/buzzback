from flask import Flask, jsonify


talents = [
    {'id': 1, 'name': 'Virat Kohli'},
    {'id': 2, 'name': 'Ranveer Singh'},
    {'id': 3, 'name': 'Diljit Dosanjh'}
]

brands = [
    {'id': 1, 'name': 'Titan Watch'},
    {'id': 2, 'name': 'Nykaa Fashion'},
    {'id': 3, 'name': 'Airtel'}
]


def match_talents_with_brands():
    matches = []
    for i in range(len(talents)):
        match = {
            'talent_name': talents[i]['name'],
            'brand_name': brands[i]['name']
        }
        matches.append(match)
    return matches


def match_brands_with_talents():
    matches = []
    for i in range(len(brands)):
        match = {
            'brand_name': brands[i]['name'],
            'talent_name': talents[i]['name']
        }
        matches.append(match)
    return matches

app = Flask(__name__)

@app.route('/match-talents-brands', methods=['GET'])
def get_matches_talents_brands():
    matches = match_talents_with_brands()
    return jsonify(matches)

@app.route('/match-brands-talents', methods=['GET'])
def get_matches_brands_talents():
    matches = match_brands_with_talents()
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)
