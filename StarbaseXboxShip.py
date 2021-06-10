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

def pitch_yaw_mouse():
    yaw = xbox360[device_idx].rightStickX
    pitch = -xbox360[device_idx].rightStickY
    # diagnostics.watch(yaw)
    # diagnostics.watch(pitch)

    #Deadzone
    input_size = math.sqrt(  yaw**2 + pitch**2  )
    if input_size < translate(deadzone, 0, 100, 0, 1):
        yaw = 0
        pitch = 0

    yaw = translate(yaw , -1, 1, res_h/2-square_size/2 , res_h/2+square_size/2 )
    pitch = translate(pitch , -1, 1, res_v/2-square_size/2 , res_v/2+square_size/2 )

    ctypes.windll.user32.SetCursorPos(int(yaw), int(pitch))

def roll():
	keyboard.setKey(Key.Q, xbox360[device_idx].leftShoulder )
	keyboard.setKey(Key.E, xbox360[device_idx].rightShoulder )

def strafe():
	keyboard.setKey( Key.Space , xbox360[device_idx].up )
	keyboard.setKey( Key.LeftAlt , xbox360[device_idx].down )
	keyboard.setKey( Key.D , xbox360[device_idx].right )
	keyboard.setKey( Key.A , xbox360[device_idx].left )

def fwd_bwd():
	keyboard.setKey( Key.W , xbox360[device_idx].rightTrigger >= 0.5 )
	keyboard.setKey( Key.S , xbox360[device_idx].leftTrigger >= 0.5 )

if starting:
	enabled = False
	current_toggle = False
	past_toggle = False

######  ↓↓ Actually run things ↓↓ ######
current_toggle = xbox360[device_idx].y
if past_toggle != current_toggle and current_toggle == True:
	enabled = not enabled
	keyboard.setPressed(Key.C)
past_toggle = current_toggle

if enabled:
	pitch_yaw_mouse()
	roll()
	strafe()
	fwd_bwd()