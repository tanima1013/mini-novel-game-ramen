CHARACTERS = {

    "player": {
        "name": "主人公",
        "color": "#FFFFFF"
    },

    "sale": {
        "name": "店員",
        "color": "#FF77AA"
    },

    "boss": {
        "name": "魔王",
        "color": "#FF77AA"
    },

    "mysterious": {
        "name": "???",
        "color": "#8888FF"
    }
}


SCENARIO = [

    # 0
    {
        "type": "text",
        "character": "player",
        "background": "bg_home.png",
        "text": "腹減った。早く家に帰ってご飯食べよ。"
    },

    # 1
    {
        "type": "narration",
        "background": "bg_ramen.png",
        "text": "目の前にラーメン二郎の店があった。"
    },

    # 2
    {
        "type": "narration",
        "background": "ramen1.png",
        "text": "主人公は週に1、2回は食べるほどラーメンが好きだ。"
    },

    # 3
    {
        "type": "narration",
        "background": "ramen1.png",
        "text": "特に二郎系が好きで、濃厚なスープ、太くモチモチした麺、柔らかく美味しいチャーシュー、強烈なニンニクの香りと味を味わいたく来店することが多い。"
    },

    # 4
    {
        "type": "narration",
        "background": "ramen1.png",
        "text": "だが、最近はゲームやコンビニでも金を使っているため、余裕がなくなってきている。"
    },

    # 5
    {
        "type": "narration",
        "text": "そのため、最近は無駄な出費は抑え、ご飯も家で済ますようにしていた。"
    },

    # 6
    {
        "type": "narration",
        "background": "bg_ramen.png",
        "text": "悩んだ末に、主人公は..."
    },

    # 7
    {
        "type": "choice",
        "background": "bg_ramen.png",
        "choices": [

            {
                "text": "二郎に行く。",
                "next": 8
            },

            {
                "text": "家で食べる。",
                "next": 19
            }

        ]
    },

    # 8
    {
        "type": "text",
        "background": "bg_ramen.png",
        "character": "player",
        "text": "ああ、我慢できない!"
    },

    # 9
    {
        "type": "narration",
        "background": "ramen4.png",
        "text": "主人公は食券を店員に渡し席についた。"
    },

    # 10
    {
        "type": "narration",
        "background": "ramen4.png",
        "text": "...10分後"
    },

    # 11
    {
        "type": "text",
        "background": "ramen4.png",
        "character": "sale",
        "text": "ニンニク入れますか?"
    },

    # 12
    {
        "type": "text",
        "background": "ramen4.png",
        "character": "player",
        "text": "ニンニク、アブラ、カラメで。"
    },

    # 13
    {
        "type": "text",
        "background": "ramen2.png",
        "character": "sale",
        "text": "はいっ!お待たせしました!ニンニク、アブラ、カラメです。"
    },

    # 14
    {
        "type": "text",
        "background": "ramen2.png",
        "character": "player",
        "text": "いただきます!"
    },

    # 15
    {
        "type": "narration",
        "background": "ramen2.png",
        "text": "...10分後"
    },

    # 16
    {
        "type": "text",
        "background": "ramen3.png",
        "character": "player",
        "text": "ご馳走様でした。"
    },

    # 17
    {
        "type": "text",
        "background": "nightsky.png",
        "character": "player",
        "text": "満腹、満腹。美味しかった。"
    },

    # 18
    {
        "type": "end",
        "background": "Apple.png",
        "title": "満足END",
        "text": "帰りにリンゴジュースを買った。"
    },

    # 19
    {
        "type": "text",
        "background": "nightsky.png",
        "character": "player",
        "text": "家にまだご飯あるし、食べようと思えばいつでも食えるし、我慢しよう。"
    },

    # 20
    {
        "type": "end",
        "background": "end2.png",
        "title": "節約END",
        "text": "節約できた。"
    }
]
