import argparse


# FIXME: refactor with tests
def parser_example():
    parser = argparse.ArgumentParser(description="Parser",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('mandatory_string', type=str, help='Help mandatory string param') #here we can't put 'mandatory-string'
    parser.add_argument('-os', '--opt-str', type=str, default='Optional string', help='Help optional string')
    parser.add_argument('-ms', '--mand-str', type=str, help='Help mandatory string', required=True)
    parser.add_argument('-i', '--int-param', type=int, default=7, help='Help int param')
    parser.add_argument('-f', '--float-param', type=float, default=7.7, help='Help float param')
    parser.add_argument('-si', '--me-gusta', action='store_true', help='Help for true parameter')
    parser.add_argument('-no', '--no-me-gusta', action='store_false', help='Help false parameter')
    parser.add_argument('-l','--list', nargs='+', help='List of arguments, ex: python argument_io.py -l 1 2 3')
    parser.set_defaults(my_list=[7, 77, 777], my_string='bazinga')
    args = parser.parse_args()
    print("Mandatory string:", args.mandatory_string)
    print("Mandatory string -ms:", args.mand_str)
    print("Store true -si:", args.me_gusta)
    print("Input list {}, type: {}".format(args.list, type(args.list)))
    print("Default list {}, type: {}".format(args.my_list, type(args.my_list)))
    """
    $ python argument_io.py AAA -ms BBB -si -l 1 2 3
    Mandatory string: AAA
    Mandatory string -ms: BBB
    Store true -si: True
    Input list ['1', '2', '3'], type: <class 'list'>
    Default list [7, 77, 777], type: <class 'list'>
    """

if __name__ == '__main__':
    parser_example()


