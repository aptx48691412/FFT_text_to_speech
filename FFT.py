import sys
sys.path.append('/Users/shotaro-y/Library/Python/3.8/lib/python/site-packages')
# -*- coding:utf-8 -*-
import pyaudio
RATE=44100
p=pyaudio.PyAudio()
N=100
CHUNK=1024*N
r= 1.059463094
r12=r*r*r*r
stream=p.open(  format = pyaudio.paInt16,
        channels = 1,
        rate = RATE,
        frames_per_buffer = CHUNK,
        input = True,
        output = True) # inputとoutputを同時にTrueにする
stream1=p.open( format = pyaudio.paInt16,
        channels = 1,
        rate = int(RATE*r12),
        frames_per_buffer = CHUNK,
        input = True,
        output = True) # inputとoutputを同時にTrueにする
while stream.is_active():
    input = stream.read(CHUNK)
    output = stream1.write(input)
