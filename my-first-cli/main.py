from argparse import ArgumentParser, Namespace

#initialise the parser and add arguments 
parser = ArgumentParser()

parser.usage = "This tool can be used to find the exponent of a number given two inputs"
group = parser.add_mutually_exclusive_group()

parser.add_argument('a', type=int, help="The base value")
parser.add_argument('b', type=int, help="The exponent")
group.add_argument('-v', '--verbose', action='count',
                    help='Provides a verbose description. Use -vv for extra  verbose.')
group.add_argument('-s', '--silent', action='store_true',
                    help='Generate a silent version of the output')

args: Namespace = parser.parse_args()
result: int = args.a ** args.b

#conditional statement depending on arguments
if args.silent:
    print("Silenced!")
else:
    match args.verbose:
        case 1:
            print(f'The result is {result}')
        case 2:
            print(f'{args.a} ** {args.b} = {result}')
        case _:
            print(result)


