import base64

# Base64-encoded SHA-512 hashes
hashes = [
    "sha512-rcwC3TQKAe2v/8lLef/QtCPf7aXHaINQK4rrQfRSqEniSzjfHKp2puNRiDg83LlvldPaSMD6aDSwKPMP36tEEg==",
    "sha512-JeWgZm97pm4zAk+MvNNodtuNUNFe082xN5Zj2RU/N/yCAq3qZMnaiENIF3swHo/Ae+Ju06jx3VeGAH/rqoAEoA==",
    "sha512-yrd1XMobAelLE0xAoM/hP3axL+jcB+V8KhqdTQItU7063qODLZOtgHB/y5KPY0H0Cev/2f7LVwp1KY0//grUmg=="
]

for h in hashes:
    # Remove the 'sha512-' prefix
    base64_hash = h.split('-', 1)[1]
    # Decode base64 to binary
    binary_hash = base64.b64decode(base64_hash)
    print(f"Binary hash: {binary_hash}")
