#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

from kalman_filter import InstantKalmanFilter
from kalman_filter import KalmanFilter


def FourierTransform(f,x,dt,N):
    yf = fft(f)/(len(t)/2) # 離散フーリエ変換&規格化
    freq = np.linspace(0, 1.0/dt, N) # frequency step
    return freq,yf
def LowPassFilter(yf,freq):
    fc = 20  # カットオフ周波数
    yf[(freq > fc)] = 0
    return yf
def InverseFourierTransform(yf,t):
    # 高速逆フーリエ変換（時間信号に戻す）
    f = np.fft.ifft(yf)
    return t,f

def main():
    kf = InstantKalmanFilter()
    kf2 = InstantKalmanFilter()
    kf3 = KalmanFilter()
    kf4 = KalmanFilter()
    df = pd.read_csv('../powerpo6_mini.csv')
    N = len(df['count'])
    t = df['time']
    speed = df['speed_x']
    pos = df['pos_x']
    dt = df['response']
    pixelw  = df['pixel_w']
    pixelh  = df['pixel_h']

    #ave_dt = (t[N-1] - t[0])/N

    plot_pos = []
    plot_speed = []
    plot_t = []
    estimated_pos = []
    estimated_speed= []
    estimated_accel= []
    speed1 = []
    speed2 = []
    pre_p = 666666
    pre_pp =666666
    
    sum_v = 0
    count = 0
    bunsan = 0
    response = []
    pre_t = 0.
    pixel = []
    for z,zz,tt,ddt,pw,ph in zip(pos,speed,t,dt,pixelw,pixelh):
        
        if not (zz == 0.0):
            pass
        pixel.append(pw*ph)
        if not(pre_t == 0.):
            response.append( tt - pre_t)

        plot_pos.append(z)
        plot_speed.append(zz)
        plot_t.append(tt)
        pp = kf3.test(zz)

        i = np.asscalar(pp[0])
        estimated_speed.append(i)
        i = np.asscalar(pp[1])
        estimated_accel.append(i)
        """
        if(pre_pp == 666666):
            pre_p = p
            pre_pp = pp
        """
        pre_t = tt
        #else:
        #    pass


    x_ran = np.arange(2, 12, 0.5)

    """"""""""""""""""
    plt.figure(1,figsize=(14.0,6.0))
    """"""""""""""""""
    plt.subplot(5,1,1)
    plt.plot(plot_t,plot_pos)
    plt.title("pos_x")
    plt.xlim(2,12)
    plt.xticks(x_ran)
    plt.grid(color='b',linestyle='dotted',linewidth=0.5)
    plt.minorticks_on()

    plt.ylabel("m")
    """"""""""""""""""
    plt.subplot(5,1,2)
    plt.title(" speed_x(Amount of change per count) And estimated_speed")
    plt.plot(t,speed)
    plt.plot(plot_t,estimated_speed)
    plt.xticks(x_ran)
    plt.xlim(2,12)
    #plt.ylim(0,1.5)
    plt.grid(color='b',linestyle='dotted',linewidth=0.5)
    plt.minorticks_on()
    plt.ylabel("m/s(count)")

    """"""""""""""""""
    plt.subplot(5,1,3)
    plt.title("response[hz]")
    plt.plot(t,[1./h for h in dt])
    plt.grid(color='b',linestyle='dotted',linewidth=0.5)
    plt.xlim(2,12)
    plt.xticks(x_ran)
    plt.minorticks_on()
    plt.ylabel("hz")
    """"""""""""""""""
    plt.subplot(5,1,4)
    plt.plot(t,[v/h for v, h in zip(speed, dt)])
    plt.title("speed_x (observed)")
    plt.xlim(2,12)
    plt.xticks(x_ran)
    plt.grid(color='b',linestyle='dotted',linewidth=0.5)
    plt.minorticks_on()
    plt.ylabel("m/s")
    """"""""""""""""""
    """"""""""""""""""
    plt.subplot(5,1,5)
    plt.plot(t,pixel)
    plt.title("pixel")
    plt.xlim(2,12)
    plt.xticks(x_ran)
    plt.ylim(0,10000)
    plt.grid(color='b',linestyle='dotted',linewidth=0.5)
    plt.minorticks_on()
    plt.xlabel("time [s]")
    plt.ylabel("pixel")
    """"""""""""""""""
    plt.tight_layout()
    plt.savefig("01")
    plt.show()
if __name__ == '__main__':
    N = 10
    dt = 1
    t = np.arange(0, N*dt, dt) # time
    freq = np.linspace(0, 1.0/dt, N) # frequency step
    main()