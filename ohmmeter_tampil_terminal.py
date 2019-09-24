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
    Vcc = 3.3 
    R_sensor = 1000 # Resistor Sensor R_sensor=1kohm    
    R_ukur = R_sensor/((Vcc/Vadc)-1) # Rumus Resistansi dalam ohm
       
    print("Nilai ADC=%d\tResistansi (Ohm)=%f" % (adc, R_ukur))
    time.sleep(1)
