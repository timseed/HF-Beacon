__author__ = 'timseed'
import logging
import sys
import datetime
import time


class beacon(object):
    freq = [14.1, 18.11, 21.15, 24.930, 28.2]  # in Mhz

    def __init__(self, CALL, Country, b14, b18, b21, b24, b28, Owner, status):
        self.CALL = CALL
        self.Country = Country
        self.band_time = []
        self.band_time.append(beacon.time_str_to_secs(b14))
        self.band_time.append(beacon.time_str_to_secs(b18))
        self.band_time.append(beacon.time_str_to_secs(b21))
        self.band_time.append(beacon.time_str_to_secs(b24))
        self.band_time.append(beacon.time_str_to_secs(b28))
        self.Owner = Owner
        self.status = status

    @staticmethod
    def time_str_to_secs(tstr):

        '''
        Replace Time_Str to seconds
        :param tstr:  In format of Min:Secs
        :return: int time_in_seconds
        '''

        try:
            min, sec = tstr.split(':')
            return int(min) * 60 + int(sec)
        except:
            return -1


class beacons(object):

    freq = [14.1, 18.11, 21.15, 24.930, 28.2]  # in Mhz
    ref_datetime=datetime.datetime(2016,1,1,0,0,0)





    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.bands = [14, 18, 21, 24, 28]  # in Mhz
        self.selected_band = 0  # 14 Mhz
        self.beacons = []
        # Setup the Beacon Definitions
        self.beacons.append(beacon('U1UN', 'United Nations', '00:00', '00:10', '00:20', '00:30', '00:40', 'UNRC', 'OK'))
        self.beacons.append(beacon('VE8AT', 'Canada', '00:10', '00:20', '00:30', '00:40', '00:50', 'RAC/NARC', 'OK'))
        self.beacons.append(beacon('W6WX', 'United States', '00:20', '00:30', '00:40', '00:50', '01:00', 'NCDXF', 'OK'))
        self.beacons.append(beacon('KH6RS', 'Hawaii', '00:30', '00:40', '00:50', '01:00', '01:10', 'Maui ARC', 'OFF9'))
        self.beacons.append(beacon('ZL6B', 'New Zealand', '00:40', '00:50', '01:00', '01:10', '01:20', 'NZART', 'OK'))
        self.beacons.append(beacon('VK6RBP', 'Australia', '00:50', '01:00', '01:10', '01:20', '01:30', 'WIA', 'OFF4'))
        self.beacons.append(beacon('JA2IGY', 'Japan', '01:00', '01:10', '01:20', '01:30', '01:40', 'JARL', 'OK'))
        self.beacons.append(beacon('RR9O', 'Russia', '01:10', '01:20', '01:30', '01:40', '01:50', 'SRR', 'OK'))
        self.beacons.append(beacon('VR2B', 'Hong Kong', '01:20', '01:30', '01:40', '01:50', '02:00', 'HARTS', 'OK'))
        self.beacons.append(beacon('4S7B', 'Sri Lanka', '01:30', '01:40', '01:50', '02:00', '02:10', 'RSSL', 'OK'))
        self.beacons.append(beacon('ZS6DN', 'South Africa', '01:40', '01:50', '02:00', '02:10', '02:20', 'ZS6DN', 'OK'))
        self.beacons.append(beacon('5Z4B', 'Kenya', '01:50', '02:00', '02:10', '02:20', '02:30', 'ARSK', 'OK'))
        self.beacons.append(beacon('4X6TU', 'Israel', '02:00', '02:10', '02:20', '02:30', '02:40', 'IARC', 'OK'))
        self.beacons.append(beacon('OH2B', 'Finland', '02:10', '02:20', '02:30', '02:40', '02:50', 'SRAL', 'OK'))
        self.beacons.append(beacon('CS3B', 'Madeira', '02:20', '02:30', '02:40', '02:50', '00:00', 'ARRM', 'OFF4'))
        self.beacons.append(beacon('LU4AA', 'Argentina', '02:30', '02:40', '02:50', '00:00', '00:10', 'RCA', 'OK'))
        self.beacons.append(beacon('OA4B', 'Peru', '02:40', '02:50', '00:00', '00:10', '00:20', 'RCP', 'OK'))
        self.beacons.append(beacon('YV5B', 'Venezuela', '02:50', '00:00', '00:10', '00:20', '00:30', 'RCV', 'OK'))

    def SetBand(self, band):
        if band in self.bands:
            self.selected_band = self.bands.index(band)
            self.logger.info(str.format('Band changed to {}', band))
            self.logger.info(str.format('Freq to Listen is {}', self.freq[self.selected_band]))
            self.logger.info(str.format('Freq to Listen is {}', self.freq[self.selected_band]))

        else:
            self.logger.error(str.format('Bad Band requested {}', band))

    def getdelay(self):
        tnow = datetime.datetime.now()
        delay = 10.0 - tnow.timestamp() % 10
        return tnow, delay

    def minsec(self,offset):
        '''
        Return Minute and Seconds offset of Timeslice
        :param offset:
        :return: Tuple (Min,Sec)
        '''
        Min=int(offset/60)
        Sec=offset-(Min*60)
        return (Min,Sec)

    def getstation(self):
        ts_now = datetime.datetime.now()
        time_diff=(beacons.ref_datetime - ts_now).seconds
        next_beacon = ('Unk', 'Unk')
        second_in_phase = 300-((time_diff) % 300)
        print("Seconds in Phase = %d"%second_in_phase)
        #next_active = (((int(second_in_phase / 10)) * 10) + 10) % 180
        next_active = (((int(second_in_phase / 10)) * 10) + 10) %180
        OSet=self.minsec(next_active)
        print("Next Active %d in secs is %d Min %d "%(next_active,OSet[0],OSet[1]))

        self.logger.info(str.format('Band {} Seconds {} next {} ', self.selected_band, second_in_phase, next_active))

        for b in self.beacons:
            if b.band_time[self.selected_band] == next_active:
                self.logger.info(str.format('Band time Index {}  {}', b.CALL, b.band_time[self.selected_band]))
                next_beacon = (b.CALL, b.Country)
                return next_beacon
        self.logger.error(str.format('Can not calculate next beacon'))
        return next_beacon

    def run(self, timeout=30):
        tnow, delay = self.getdelay()
        self.logger.info(str.format('timenow is {}', tnow.timestamp()))
        self.logger.info(str.format('delay   is {}', delay))
        while (timeout > 0):
            timeout = timeout - delay
            next_station = self.getstation()
            self.logger.info(str.format('Call {} Country {}', next_station[0], next_station[1]))
            print(str.format('{} {} Mhz Station {}  Country {} ', self.freq[self.selected_band],self.bands[self.selected_band], next_station[0],
                             next_station[1]))
            time.sleep(delay)
            tnow, delay = self.getdelay()

            self.logger.info(str.format('timenow is {}', tnow.timestamp()))
            self.logger.info(str.format('delay   is {}', delay))
        self.logger.info('Loop run ended')

    def dump_band(self, band_id):
        print(str.format('Dumping Band ID {}', band_id))
        for b in self.beacons:
            print(str.format('Time offset {} ', b.band_time[band_id]))


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    dx = beacons()
    dx.SetBand(int(sys.argv[1]))
    dx.run(timeout=5000)
    # dx.dump_band(4)
