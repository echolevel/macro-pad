import storage, usb_cdc, usb_midi
import board, digitalio

startupkey = digitalio.DigitalInOut(board.GP0)
startupkey.direction = digitalio.Direction.INPUT
startupkey.pull = digitalio.Pull.UP


# If the top left button isn't held down on startup, disable
# mass storage, USB MIDI, and CDC (serial) modes
if startupkey.value:    
    storage.disable_usb_drive()
    usb_midi.disable()
    usb_cdc.disable()
    usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.CONSUMER_CONTROL))
    
    
