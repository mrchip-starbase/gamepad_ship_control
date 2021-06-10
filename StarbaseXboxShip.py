######  ↓↓ Configuration variables ↓↓ ######
device_idx = 0      # What device to use. Usually 0 works, you may need to change this if you have more than 1 connected.
deadzone = 5        # 0% - 100% of your input, that is snapped back to 0
square_size = 756   # Size in pixel of the square. Depends on your resolution.
res_h = 1920        # Your screen's horizontal resolution.
res_v = 1080        # Your screen's vertical resolution.
######  ↑↑ Configuration variables ↑↑ ######

import ctypes

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


######  ↓↓ Script ↓↓ ######
yaw = xbox360[device_idx].rightStickX
pitch = -xbox360[device_idx].rightStickY
diagnostics.watch(yaw)
diagnostics.watch(pitch)

#Deadzone
input_size = math.sqrt(  yaw**2 + pitch**2  )
if input_size < translate(deadzone, 0, 100, 0, 1):
	yaw = 0
	pitch = 0

yaw = translate(yaw , -1, 1, res_h/2-square_size/2 , res_h/2+square_size/2 )
pitch = translate(pitch , -1, 1, res_v/2-square_size/2 , res_v/2+square_size/2 )

ctypes.windll.user32.SetCursorPos(int(yaw), int(pitch))