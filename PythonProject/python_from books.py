# print('what is your name')
# name = input()
# print('hello', name, "Nice to meet you")
#
# import subprocess
#
# profile = subprocess.check_output("nets WLAN show profile", shell=True).decode("utf-8")
# names = [line.split(":")[1].strip()
#          for line in profile.split("\n") if "All User Profile" in line]
#
# for i, n in enumerate(names, 1):
#     print(f"{i}. {n}")
#
# ch = int(input("\nChoose Wi-Fi number: "))
# Wi-Fi = names[ch - 1]
#
# result = subprocess.check_output(
#     f'netsh wlan show profile "{Wi-Fi}" key=clear',
#     shell=True).decode("utf-8")
#
# # Extract and print the password
# for line in result.split("\n"):
#     if "Key Content" in line:
#         print(line)

import urllib.request

def send_key_no_requests(ip, key, timeout=2):
    url = f"https://{ip}:8060/keypress/{key}"
    req = urllib.request.Request(url, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status if hasattr(resp, "status") else 200
            body = resp.read().decode("utf-8", errors="ignore")
            return status, body
    except Exception as e:
        return None, str(e)
##!/usr/bin/env python3
# name=roku_remote.py
"""
Simple Roku remote via network (HTTP ECP).

Usage examples:
  python roku_remote.py --discover
  python roku_remote.py --ip 192.168.1.40 Home
  python roku_remote.py --ip 192.168.1.40 Play
  python roku_remote.py --ip 192.168.1.40 "VolumeUp"

Commands (common):
  Home, Up, Down, Left, Right, Select, Back,
  Play, Pause, Rev, Fwd, Info, Power, VolumeUp, VolumeDown

Notes:
  - Install requests: pip install requests
  - Discovery scans a /24 based on your primary outbound IP (best-effort).
"""

import socket
import urllib.error
import urllib.request
from typing import List, Tuple

DEFAULT_PORT = 8060

# map common lower-case names to Roku key names (case-sensitive expected by Roku)
KEY_MAP = {
    "home": "Home",
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "select": "Select",
    "back": "Back",
    "play": "Play",
    "pause": "Pause",
    "rev": "Rev",
    "fwd": "Fwd",
    "info": "Info",
    "power": "Power",
    "volume": "VolumeUp",
    "volume down": "VolumeDown",
    # add more mappings if you want (e.g., "channel": "ChannelUp")
}

def normalize_key(key: str) -> str:
    k = key.strip()
    lower = k.lower()
    if lower in KEY_MAP:
        return KEY_MAP[lower]
    # If user provided exact Roku key, use it as-is (capitalization preserved)
    return k

def send_key(ip: str, key: str, timeout: float = 2.0) -> bool:
    key = normalize_key(key)
    url = f"https://{ip}:{DEFAULT_PORT}/keypress/{key}"
    req = urllib.request.Request(url, data=b"", method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status if hasattr(resp, "status") else resp.getcode()
            if status in (200, 201, 204):
                print(f"Sent {key} to {ip} (HTTP {status})")
                return True
            print(f"Failed to send {key} to {ip}: HTTP {status}")
            return False
    except urllib.error.URLError as e:
        print(f"Error sending {key} to {ip}: {e}")
        return False

def query_device(ip: str, timeout: float = 1.0) -> str | None:
    url = f"https://{ip}:{DEFAULT_PORT}/query/device-info"
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status if hasattr(resp, "status") else resp.getcode()
            if status == 200:
                return resp.read().decode("utf-8", errors="ignore")
    except urllib.error.URLError:
        pass
    return None

def get_local_ipv4() -> str | None:
    # Trick: open UDP socket to public IP and read local socket name (no actual packets sent)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        return local_ip
    except Exception:
        return None
    finally:
        s.close()

def discover_roku(timeout_per_host: float = 0.5) -> List[Tuple[str, str]]:
    local_ip = get_local_ipv4()
    if not local_ip:
        print("Could not determine local IP address.")
        return []

    # Assume /24 subnet
    base_ip = ".".join(local_ip.split(".")[:-1])
    found_devices = []
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        device_info = query_device(ip, timeout=timeout_per_host)
        if device_info:
            found_devices.append((ip, device_info.strip()))
            print(f"Found Roku at {ip}: {device_info.strip()}")
    return found_devices