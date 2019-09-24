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
    R1 = 100000 # Resistor R1=100kohm
    R2 = 1000 # Resistor R2=1kohm    
    V_ukur = Vadc*(R1+R2)/R2 # Rumus tegangan dalam volt
       
    print("Nilai ADC=%d\tTegangan (Volt)=%f" % (adc, V_ukur))
    time.sleep(1)
