**What can it do?**

This simple micropython script can read a [CMOSTEK RFPDK](http://www.hoperf.cn/ic/rf_receiver/CMT2219A.html) register value table file, then write the values  to CMT2219A  registers.

Tested in a ESP8266 board running official micropython v1.14 .

**Wiring****

`.-----------------------.              .---------------.`
`|                     16|--------------|CSB            |`
`|    ESP8266            |              |    CMT2219A   |`
`|              (CLK ) 14|--------------|SCL            |`
`|              (MISO) 13|---------+----|SDA            |`
`|              (MOSI) 12|--{R1K}--'    '---------------'`
`'-----------------------'`



**Get "reg.txt"**

Export CMT2219A register table file by [CMOSTEK RFPDK V1.51](http://www.hoperf.cn/ic/rf_receiver/CMT2219A.html), rename the file "yourname_Reg.exp" to "reg.txt". delete the lines from the beginning to "Addr	Value" in the file.



**Download files**

In uPyCraft, download "cmt2219.py" and "reg.txt" to your esp8266 board.



**Try to use**

`from cmt2219 import CMT2219A`
`radio = CMT2219A()`
`radio.read_config()`
`radio.write_table()`
