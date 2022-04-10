'''

==== ex.: args.txt ================================
-v
-c=4
-u=http://200.152.38.155/CNPJ/K3241.K03200Y1.D20312.EMPRECSV.zip
-u=http://200.152.38.155/CNPJ/K3241.K03200Y2.D20312.EMPRECSV.zip
-----------------------------------------------
no arquivo se as strings estão separadas por espaço, chega um argumento único.
e se udar `-u<espace>nome_do_arquivo`
 o nome do arquivo dentro da lista contem o espaço !!!

'''

import argparse
import sys

from asyncdown import asyncdown


DESCRIPTION = 'Concurrently download files'


def command_line_parser(sys_args):

    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        fromfile_prefix_chars='@args')

    parser.add_argument('-u', '--urls-list', nargs='+', action="extend", required=True)
    parser.add_argument('-c', '--concurrent-downloadas', type=int, default=5)
    parser.add_argument('-v', '--verbose', default=False, action=argparse.BooleanOptionalAction)

    args = parser.parse_args(sys_args)
    return args


def main(sys_args):

    args = command_line_parser(sys_args)
    print(f'===={args.urls_list}====')
    print(f'===={args.verbose}====')
    print(f'===={args.concurrent_downloadas}====')

    # ad = asyncdown.ADDownload(args.urls_list)

if __name__ == '__main__':

    main(sys.argv[1:])
