import spidev, time
spi = spidev.SpiDev()
spi.open(0, 0)
def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out
while True:
    adc = analog_read(0)
    Vadc = adc * 3.3 / 1024
    R = 10 # Resistor sensor
    I_ukur = Vadc/R # Rumus arus dalam ampere
    I_mili = I_ukur*1000 #ARumus arus dalam miliampere
    
    print("Nilai ADC=%d\tArus (mA)=%f" % (adc, I_mili))
    time.sleep(1)
