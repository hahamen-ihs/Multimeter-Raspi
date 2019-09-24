from Tkinter import *
import spidev, time
spi = spidev.SpiDev()
spi.open(0, 0)
def pembacaan_avometer(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc = ((r[1]&3) << 8) + r[2]
    return adc

class App:
	
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='ARUS (mA)', font=("Helvetica", 32))
        label.grid(row=0)
        self.reading_label1 = Label(frame, text='12.34', font=("Helvetica", 32))
        self.reading_label1.grid(row=1)
        self.update_arus()
        label = Label(frame, text='TEGANGAN (Volt)', font=("Helvetica", 32))
        label.grid(row=2)
        self.reading_label2 = Label(frame, text='12.34', font=("Helvetica", 32))
        self.reading_label2.grid(row=3)
        self.update_tegangan()
        label = Label(frame, text='RESISTANSI (Ohm)', font=("Helvetica", 32))
        label.grid(row=4)
        self.reading_label3 = Label(frame, text='12.34', font=("Helvetica", 32))
        self.reading_label3.grid(row=5)
        self.update_resistansi()
        
    def update_arus(self):
        #Pembacaan Arus
        adc_arus = pembacaan_avometer(0)
        Vadc_arus = adc_arus * 3.3 / 1024
        R = 10 # Resistor sensor
        I_ukur = Vadc_arus/R # Rumus arus dalam ampere
        I_mili = I_ukur*1000 #ARumus arus dalam miliampere
        baca_arus = "{:.2f}".format(I_mili)
        self.reading_label1.configure(text=baca_arus)
        self.master.after(500, self.update_arus)

    def update_tegangan(self):
        #Pembacaan Tegangan
        adc_tegangan =  pembacaan_avometer(1)
        Vadc_tegangan = adc_tegangan * 3.3 / 1024
        R1 = 100000 # Resistor R1=100kohm
        R2 = 1000 # Resistor R2=1kohm    
        V_ukur = Vadc_tegangan*(R1+R2)/R2 # Rumus tegangan dalam volt 
        baca_tegangan = "{:.2f}".format(V_ukur)
        self.reading_label2.configure(text=baca_tegangan)
        self.master.after(500, self.update_tegangan)
        
    def update_resistansi(self):
        #Pembacaan Resistansi
        adc_resistansi = pembacaan_avometer(2)
        Vadc_resistansi = adc_resistansi * 3.3 / 1024
        Vcc = 3.3 
        R_sensor = 1000 # Resistor Sensor R_sensor=1kohm    
        R_ukur = R_sensor/((Vcc/Vadc_resistansi)-1) # Rumus Resistansi dalam ohm  
        baca_resistansi = "{:.2f}".format(R_ukur)
        self.reading_label3.configure(text=baca_resistansi)
        self.master.after(500, self.update_resistansi)
        
root = Tk()
root.wm_title('AVOmeter')
app = App(root)
root.geometry("400x400+0+0")
root.mainloop()
