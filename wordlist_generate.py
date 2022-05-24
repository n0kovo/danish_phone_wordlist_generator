#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from picker import *
from sys import exit
from tqdm import tqdm
from tqdm.auto import trange
from os.path import normpath
import re


outfile_path = normpath(input("Output file: "))
if bool(re.search(r"[^A-Za-z0-9_\-\\\.]", outfile_path)):
    print("Invalid output file or path specified!")
    exit()


opts = Picker(
    title="Select number ranges to include:",
    options=[
        "20-31   - General mobile telephony",
        "32      - Amager excl. Christianshavn",
        "33      - Copenhagen City (incl. Christianshavn) and Vesterbro",
        "35      - Nørrebro",
        "36      - Valby, Rødovre and Hvidovre",
        "38      - Vanløse, Frederiksberg, Nordvest and Brønshøj",
        "39      - Østerbro, Ryvang, Hellerup, Ordrup and Søborg",
        "40-42   - General mobile telephony",
        "43      - Glostrup, Albertslund, Tåstrup, Vallensbæk, Hundige and Greve",
        "44      - Herlev, Ballerup, Værløse and Bagsværd",
        "45      - Lyngby, Birkerød, Virum, Holte and Skodsborg",
        "46      - Roskilde-area",
        "47-49   - North Zealand (Frederiksborg County)",
        "501-503 - Public Person Search Service (OPS) until 01/09/2003, when OPS was closed down. Hereafter assigned to general mobile telephony.",
        "504-509 - General mobile telephony",
        "51-53   - General mobile telephony",
        "54      - Lolland and Falster",
        "55      - South Zealand and Møn",
        "56      - East Zealand (Køge-area) and Bornholm",
        "57      - Ringsted, Sorø",
        "58      - Slagelse, Korsør, Skælskør",
        "59      - Nortwest Zealand",
        "60-61   - General mobile telephony",
        "62-69   - Funen, Langeland, Ærø, Tåsinge and islands in the Funen Archipelago",
        "70      - Personal numbers and flex numbers",
        "72-79   - Southern Jutland",
        "80      - Free call numbers",
        "82      - Eastern Jutland",
        "86-89   - Eastern Jutland",
        "90      - Paid services (Humanitarian aid, sexual content, help desk etc.), public payphones",
        "96-97   - Western Jutland",
        "98-99   - Northern Jutland",
    ],
).getSelected()


if opts == False:
    print("Aborted!")
    exit()

ranges = []

total_count = 0
for opt in opts:
    opt = opt.split(" - ")[0].replace(" ", "")
    if "-" in opt:
        is_range = True
        range_start = int(opt.split("-")[0])
        range_stop = int(opt.split("-")[1]) + 1

    else:
        is_range = False
        range_start = int(opt)
        range_stop = range_start + 1

    ranges.append(range(range_start, range_stop))

    for prefix in range(range_start, range_stop):
        if prefix >= 99:
            total_count += 100000
        else:
            total_count += 1000000


bar_format = "{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{remaining}"
total_pbar = tqdm(total=total_count, position=1, bar_format=bar_format)
total_pbar.set_description("Total progress")
total_pbar.update(0)


for r in ranges:
    pbar = tqdm(position=0, leave=False, bar_format=bar_format)

    for prefix in r:
        range_start = r[0]
        range_stop = r[-1]

        if len(r) > 1:
            is_range = True
            pbar.set_description(
                f"Outputting numbers w. prefixes {range_start}-{range_stop}"
            )
        else:
            is_range = False
            pbar.set_description(f"Outputting numbers w. prefix {range_start}")

        with open(outfile_path, "a+") as outfile:
            if prefix >= 99:
                total = 100000
                pbar.total = total * len(r)
                for i in range(0, total):
                    outfile.write(f"{prefix}{i:05d}\n")
                    total_pbar.update()
                    pbar.update()
            else:
                total = 1000000
                for i in range(0, total):
                    pbar.total = total * len(r)
                    outfile.write(f"{prefix}{i:06d}\n")
                    total_pbar.update()
                    pbar.update()
