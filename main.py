# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from vsi_client import VSI

if __name__ == "__main__":
    vsi = VSI()
    print(vsi.list_vsi())
    print(vsi.stop_vsi("test-vm"))
    print(vsi.list_vsi())
    print(vsi.start_vsi("test-vm"))
    print(vsi.list_vsi())
