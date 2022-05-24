from picker import *
from sys import exit
from tqdm import tqdm


outfile_path = input("Output file: ")

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


for opt in opts:
    opt = opt.split(" - ")[0].replace(" ", "")

    if "-" in opt:
        is_range = True
        rangestart, rangestop = opt.split("-")
        rangestart = int(rangestart)
        rangestop = int(rangestop)
    else:
        is_range = False
        rangestart = int(opt)
        rangestop = rangestart

    pbar = tqdm()
    for prefix in range(rangestart, rangestop + 1):
        if is_range:
            pbar.set_description(
                f"Outputting numbers with prefixes {rangestart}-{rangestop}"
            )
        else:
            pbar.set_description(f"Outputting numbers with prefix {rangestart}")

        with open(outfile_path, "a+") as outfile:
            if prefix >= 99:
                pbar.total = len(range(0, 100000)) * (rangestop - rangestart + 1)
                for i in range(0, 100000):
                    outfile.write(f"{prefix}{i:05d}\n")
                    pbar.update()

            else:
                for i in range(0, 1000000):
                    pbar.total = len(range(0, 1000000)) * (rangestop - rangestart + 1)
                    outfile.write(f"{prefix}{i:06d}\n")
                    pbar.update()
