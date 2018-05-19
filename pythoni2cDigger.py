import smbus

bus=smbus.SMBus(1)
for i in range(0x03,0x77):
        try:
                bus.write_quick(i)
                print hex(i)
        except Exception as e:
                if e.args[0] == 16:
                        print '%s(UU)'%hex(i)
                pass
