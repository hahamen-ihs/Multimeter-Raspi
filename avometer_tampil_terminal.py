import spidev, time
spi = spidev.SpiDev()
spi.open(0, 0)
def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out
while True:
    adc_arus = analog_read(0)
    adc_tegangan = analog_read(1)
    adc_resistansi = analog_read(2)

    #Pengukuran arus
    Vadc_arus = adc_arus * 3.3 / 1024
    R_arus = 10 # Resistor sensor arus
    I_ukur = Vadc_arus/R_arus # Rumus arus dalam ampere
    I_mili = I_ukur*1000 #ARumus arus dalam miliampere

    #Pengukuran tegangan
    Vadc_tegangan = adc_tegangan * 3.3 / 1024
    R1 = 100000 # Resistor R1=100kohm
    R2 = 1000 # Resistor R2=1kohm    
    V_ukur = Vadc_tegangan*(R1+R2)/R2 # Rumus tegangan dalam volt

    #Pengukuran resistansi
    Vadc_resistansi = adc_resistansi * 3.3 / 1024
    Vcc = 3.3 
    R_sensor = 1000 # Resistor Sensor R_sensor=1kohm    
    R_ukur = R_sensor/((Vcc/Vadc_resistansi)-1) # Rumus Resistansi dalam ohm
    
    print("Arus(mA)=%f\tTegangan(Volt)=%f\tResistansi(Ohm)=%f" % (I_mili, V_ukur, R_ukur))
    time.sleep(1)
