#!/usr/bin/env python3
# -*- coding: utf-8 -*
import argparse
import os

import cambriantools as ct


# parser and settings
parser = argparse.ArgumentParser(prefix_chars='--')
parser.add_argument('--path', type=str, default='./data')
parser.add_argument('--save_path', type=str, default='./save')
main_args = parser.parse_args()


#
filedirs = ct.files.get_filedirs(main_args.path)
for filedir in filedirs:
    save_path = os.path.split(filedir)[0].replace(main_args.path, main_args.save_path)
    print(f'filedir={filedir}; save_path={save_path}')
    ct.pdfs.save_imgs_from_pdf(filedir, save_path)