from Tkinter import *
import spidev, time
spi = spidev.SpiDev()
spi.open(0, 0)
def analog_read(channel):
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
        self.reading_label = Label(frame, text='12.34', font=("Helvetica", 52))
        self.reading_label.grid(row=1)
        self.update_reading()

    def update_reading(self):
        adc_arus = analog_read(0)
        Vadc_arus = adc_arus * 3.3 / 1024
        R = 10 # Resistor sensor
        I_ukur = Vadc_arus/R # Rumus arus dalam ampere
        I_mili = I_ukur*1000 #ARumus arus dalam miliampere    
        reading_str = "{:.2f}".format(I_mili)
        self.reading_label.configure(text=reading_str)
        self.master.after(500, self.update_reading)


root = Tk()
root.wm_title('Amperemeter')
app = App(root)
root.geometry("400x300+0+0")
root.mainloop()
