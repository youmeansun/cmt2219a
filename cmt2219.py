from machine import Pin, SPI

class CMT2219A(object):
  def __init__(self):
    self.spi = SPI(1, baudrate=200000, polarity=0, phase=0) #MOSI=GPIO13, MISO=GPIO12, SCK=GPIO14
    self.csb = Pin(16, Pin.OUT, value=1)
    self._reg = bytearray(62)

  def read_reg(self, addr):
    b = bytearray([0x80 + addr])
    self.csb.off()
    self.spi.write(b)
    t = self.spi.read(1)
    self.csb.on()
    return t[0]

  def write_reg(self, addr, val):
    b = bytearray([addr, val])
    self.csb.off()
    self.spi.write(b)
    self.csb.on()

  def read_config(self):
    f = open('reg.txt', 'r')
    for r in f.read().split('\r'):
      if r.find('\t') == 4:
        a,v = r.split('\t')
        self._reg[int(a, 16)] = int(v,16)
    f.close()    


  def read_table(self):
    for i in range(len(self._reg)):
      self._reg[i] = self.read_reg(i)


  def write_table(self):
    for i in range(len(self._reg)):
      self.write_reg(i, self._reg[i])

