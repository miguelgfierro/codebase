import argparse
from datetime import datetime
from dateutil.parser import isoparse


def parse_args(arguments=[]):
    """Example of argparse with different inputs.
    Args:
        arguments (list): Arguments passed as a list of strings. This argument
                          can be used when calling the function from a
                          notebook. Alternatively when using the command line,
                          we don't need this variable.
    Examples:
        >>> cmd = 'AAA -ms BBB -si -l 1 2 3'
        >>> args = parse_args(['AAA', '-ms', 'BBB', '-si', '-l', '1', '2', '3', '-d', '2020-01-06'])
        Mandatory string: AAA
        Mandatory string -ms: BBB
        Store true -si: True
        Input list ['1', '2', '3'], type: <class 'list'>
        Default list [7, 77, 777], type: <class 'list'>
        Date: 06/01/2020, 00:00:00

    """
    parser = argparse.ArgumentParser(
        description="Parser", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # here we can't put 'mandatory-string'
    parser.add_argument(
        "mandatory_string", type=str, help="Help mandatory string param"
    )
    parser.add_argument(
        "-os",
        "--opt-str",
        type=str,
        default="Optional string",
        help="Help optional string",
    )
    parser.add_argument(
        "-ms", "--mand-str", type=str, help="Help mandatory string", required=True
    )
    parser.add_argument("-i", "--int-param", type=int, default=7, help="Help int param")
    parser.add_argument(
        "-f", "--float-param", type=float, default=7.7, help="Help float param"
    )
    parser.add_argument(
        "-si", "--me-gusta", action="store_true", help="Help for true parameter"
    )
    parser.add_argument(
        "-no", "--no-me-gusta", action="store_false", help="Help false parameter"
    )
    parser.add_argument(
        "-l",
        "--list",
        nargs="+",
        help="List of arguments, ex: python argument_io.py -l 1 2 3",
    )
    parser.add_argument(
        "-d",
        "--date",
        default=datetime.now().isoformat(),
        type=isoparse,
        help="Date for an event (format: YYYY-MM-DD)",
    )
    parser.set_defaults(my_list=[7, 77, 777], my_string="bazinga")
    if arguments:  # when calling from notebook
        args = parser.parse_args(arguments)
    else:  # when calling from command line
        args = parser.parse_args()
    print("Mandatory string:", args.mandatory_string)
    print("Mandatory string -ms:", args.mand_str)
    print("Store true -si:", args.me_gusta)
    print("Input list {}, type: {}".format(args.list, type(args.list)))
    print("Default list {}, type: {}".format(args.my_list, type(args.my_list)))
    print("Date: {}".format(args.date.strftime("%d/%m/%Y, %H:%M:%S")))
    return args


if __name__ == "__main__":
    parse_args()
