state_size = 1600
block_size = 1024

capacity = state_size - block_size

lane_size = 64

capacity_lanes = capacity // lane_size
message_lanes = block_size // lane_size

print("State size:", state_size, "bits")
print("Block size:", block_size, "bits")
print("Capacity:", capacity, "bits")

print("Message lanes:", message_lanes)
print("Capacity lanes:", capacity_lanes)

print("All capacity lanes become nonzero after one complete absorption step.")
