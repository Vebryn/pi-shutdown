pi-shutdown
===========

Shutdown(/power on) Raspberry Pi with pushbutton

## What's new?

* button debouncing from GPIO library instead of manual debouncing
* python 3.7 compatibility
* code linting (pylint3)
* reboot feature removed as power off/on do the same
* systemd unit to manage script execution
* Debian package building script

## Installation

* connect pushbutton to GPIO pin 5 and ground
* power on rpi
* install pi-shutdown package

```
dpkg -i py-shutdown_1.x_all.deb
```

* systemd unit starts automatically

When button is pressed, Pi shuts down.
While shut down, if button is connected to GPIO pin 5, then pressing the button powers on Pi.

## Debugging

* stop systemd unit
* start pishutdown script

```
systemctl stop pi-shutdown
sudo pishutdown.py
```

## Package building script

* install prerequisites

```
sudo apt install build-essential devscripts debhelper --no-install-recommends
```

* source building script and manage changelog

```
. build_debian_package
dch --increment
dch --release
```

* build package

```
./build_debian_package
```
