📄 PhantomFloat:
Symbolic Steganography via Floating Point Representability Drift

Abstract:

This work introduces PhantomFloat, a novel steganographic encoding technique that leverages the representational 


irregularities of IEEE 754 floating point numbers as a covert information channel. Rather than embedding payloads in the
binary structure of a value, PhantomFloat encodes message bits in the semantic delta between an intended decimal and its
actual binary floating-point representation.


By treating the (ir)representability of a decimal string as a symbolic indicator—i.e., whether float(d) == d holds un
der IEEE rounding rules—this technique creates a new class of stego encoders that are both deniable and high-fidelity. Bits are transmitted not through visible values but through inductive obfuscation: a logic layer where the presence or absence of representational drift becomes the signal itself.


This approach introduces a form of semantic LSB encoding, where information is hidden in computational failure modes rather than raw data. We demonstrate a working prototype that achieves 1 bit per float using predefined pools of representable and unrepresentable decimals, and discuss extensions involving drift direction and error magnitude as higher-dimensional symbolic spaces.

PhantomFloat reframes floating point limitations—typically a source of computational error—as an expressivesubstrate for covert communication, symbolic computation, and precision-layer logic. The method opens promising directions in anti-forensic stego, numeric watermarking, symbolic VMs, and drift-resilient logic gates, representing a new paradigm in adversarial computation and meaning-carrying failure.