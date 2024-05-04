from random import choice

capital="Kathmandu"
bird="Dhaphe"
flower="Rhododendron"
song="National Song of Nepal"

def randomFunFact():
    funfact=[
        'Mount Everest: Nepal is home to Mount Everest, the tallest mountain in the world, standing at 8,848 meters (29,029 feet) above sea level.',
        'Birthplace of Buddha: Lumbini, located in Nepal, is the birthplace of Siddhartha Gautama, the founder of Buddhism.',
        'Multilingual Nation: Nepal is incredibly diverse linguistically, with over 123 languages spoken in the country.',
'Rhododendron Capital: Nepal boasts more than 30 species of rhododendron, making it a rhododendron paradise and home to the largest variety of these flowers in the world.',
'Kumari - Living Goddess: Kathmandu, the capital of Nepal, houses the Kumari, a living goddess selected from pre-pubescent girls and revered by both Hindus and Buddhists.',
'Worlds Deepest Gorge: The Kali Gandaki Gorge, located in Nepal, is one of the deepest gorges in the world, carved by the Kali Gandaki River.',
'Yeti Legends: Nepal is famous for its legends of the Yeti, a mythical creature believed to inhabit the Himalayas.'
'Gurkha Warriors: The Gurkhas, soldiers from Nepal, are renowned for their bravery and have served in the British and Indian armies for centuries.',
"Unique Flag: Nepal's flag is the only national flag in the world that is not rectangular or square; it consists of two overlapping triangles.",
'Monsoon Influence: Nepal experiences a distinct monsoon season, which heavily influences its climate and sustains its lush vegetation.',
        ]
    
    index=choice("0123456789")
    print(funfact[int(index)])

randomFunFact()


if __name__=='__main__':
    randomFunFact()