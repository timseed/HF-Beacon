#Beacon

A small class that will calculate the next beacon that is due to transmit.

#Code Usage

To see which beacon is available on 14 Mhz

    dx=beacons()
    dx.SetBand(14)
    dx.run(timeout=5000)

If you wanted to switch to another band you would call

    dx.SetBand(18)

Valid bands are the same as the HF DXCC Network

    14,18,21,24,28

##Logging

If you want to see what is going on then add logging

    import logging
    from beacons import beacons
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    dx=beacons()
    dx.run(timeout=5000)

#To Do

* Maybe add 100 Watt, 10 W, 1W and .1W sections
* Range and brearing from your QTH


