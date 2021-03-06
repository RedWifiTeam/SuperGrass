#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
from Extra.banner import banner
from Extra.usage import parser
import sys
from Scaner.dirPathScan import DirpathScan


if __name__ == '__main__':
    banner()
    args = parser.parse_args()
    print(args)
    if args.durl:
        DirpathScan(args.durl)
    elif args.url:
        pass