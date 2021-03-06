import requests
import json

test = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]
]

test2 = {"s": ["test", "test2"]}


def get_chess():
    try:
        r = requests.get('http://wec2021.herokuapp.com/api/chess', data={'id': '1'})
        print(r.json())
        print(r.status_code)
        return r.json()["board"], r.json()["player"]
    except:
        print("Problem conntecting to server GET")



def board_to_json(board):
    out = []
    for row in board:
        outrow = []
        for piece in row:
            outrow.append(piece)
        out.append(outrow)
    print(out)


def put_chess(board, player):
    try:
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        # print(json.dumps(test))
        # board_to_json(test)
        r = requests.post('http://wec2021.herokuapp.com/api/chess', json={"board": board, "player": player}, headers=headers)
    except:
        print("Problem conntecting to server PUT")
