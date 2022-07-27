import deemix
import os

arl = "c7cc94374687d692569d03d9dc3661a69baedc99578c4814d9ad22c0400b55ff940d5f1c251ce26f22348e68d26af5bf313ed421270201a62bd88210e59e15d7887388752b8bdedf46f33121510409ca4863dadc5ae094c7411799118a1919ac"

# deezerWebpageLink = input("Paste Deezer Webpage Link: ")


def download(link, arl):
    os.system(f"deemix -b 128 -p downloads/ {link}")


download(
    "https://www.deezer.com/us/playlist/10556439182",
    "f34e92003ee42a6e9a0035b33c5a758b3e2b6e1d3946262b1a5687fbc83f9ff11d2ef42273e2b764607984007a66ec7c04aa376cddca46780ef0e35fa17c01944b42df6e8713cdc0d677a530c77e83bfa081ff099625f2920e20cd954b50598a",
)
