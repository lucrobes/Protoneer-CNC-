#import grbl_link, pygcode, serial, time
import serial, time 
#print(dir(grbl_link))

#print(dir(pygcode))


# Open grbl serial port ==> CHANGE THIS BELOW TO MATCH YOUR USB LOCATION
s = serial.Serial('/dev/ttyAMA0',115200) # GRBL operates at 115200 baud. Leave that part alone.

# Open g-code file
f = open('circle.nc','r');
wakeup = str.encode("\r\n\r\n")
# Wake up grbl
s.write(wakeup)
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input

# Stream g-code to grbl
for line in f:
    l = str.encode(line.strip()) # Strip all EOL characters for consistency
    print(str.encode('Sending: ') + l)
    s.write(l + str.encode('\n')) # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print(str.encode(' : ') + grbl_out.strip())

# Wait here until grbl is finished to close serial port and file.
raw_input("  Press <Enter> to exit and disable grbl.")

# Close file and serial port
f.close()
s.close()