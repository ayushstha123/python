
def hello(name,lang):
    greetings={
        "English":"Hello",
        "Spanish":"Ola",
        "German":"Hallo",
        "Nepali":"K cha"
    }

    msg=f"{greetings[lang]} {name}"
    print(msg)

if __name__ =='__main__':
        
    import argparse

    parser=argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n","--name" , metavar="name",
        required=True,help="The name of the person to greet"
    )

    parser.add_argument(
        "-l","--lang",metavar="language",
        required=True , choices=["English","Spanish","German","Nepali"],
        help="the language of the greeting"
    )

    args=parser.parse_args()
    # msg=f"hello {args.name}!"
    # print(msg)

hello(args.name,args.lang)