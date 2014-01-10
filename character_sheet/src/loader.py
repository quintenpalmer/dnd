import json

import player


def load_player(name):
    return player.Player(**json.load(open('characters/%s.json' % name)))

def save_player(player_obj):
    with open('characters/%s.json' % player_obj.name, 'w') as f:
        f.write(json.dumps(json.loads(player_obj.serialize()), indent=4))

if __name__ == '__main__':
    p1 = load_player('Bobbit')
    print(p1)
    p1.level += 1
    print(p1)
    save_player(p1)
    p1.level -= 1
    print(p1)
    save_player(p1)
