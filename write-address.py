import re

# Read address.txt
with open("address.txt", "r") as f:
    content = f.read()

# Extract Bluetooth MAC address
match = re.search(r"([0-9A-F]{2}(:[0-9A-F]{2}){5})", content, re.IGNORECASE)
if not match:
    raise ValueError("No Bluetooth address found!")

bt_address = match.group(1)
print(f"Found BT address: {bt_address}")

# Read config file
with open("SBFspot.cfg", "r") as f:
    cfg = f.read()

# Replace BTAddress line
cfg = re.sub(r"BTAddress=.*", f"BTAddress={bt_address}", cfg)

# Write back
with open("SBFspot.cfg", "w") as f:
    f.write(cfg)

print("SBFspot.cfg updated successfully.")