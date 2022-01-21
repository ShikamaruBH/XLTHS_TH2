# Default librarys
import numpy as np

# Put environment variable here
VOWELS = 'aeiou'
TINHIEUHUANLUYEN_NAMES = ['01MDA', '02FVA', '03MAB', '04MHB', '05MVB', '06FTB', '07FTC', '08MLD', '09MPD', '10MSD', '11MVD', '12FTD', '14FHH', '15MMH', '16FTH', '17MTH', '18MNK', '19MXK', '20MVK', '21MTL', '22MHL']
TINHIEUKIEMTHU_NAMES = ['23MTL', '24FTL', '25MLM', '27MCM', '28MVN', '29MHN', '30FTN', '32MTP', '33MHP', '34MQP', '35MMQ', '36MAQ', '37MDS', '38MDS', '39MTS', '40MHS', '41MVS', '42FQT', '43MNT', '44MTT', '45MDV']
FRAME_LENGHT_IN_SECOND = .03
FRAME_SHIFT_IN_SECOND = .01

# Threshold of STE
THRESHOLD = 0.06827

# Threshold of MA
# THRESHOLD = 0.11918

N = 13
N_FFT = 1024

K = 1