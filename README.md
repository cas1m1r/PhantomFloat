# PhantomFloat

PhantomFloat — hide messages in the weird edges of floating point math.  
Think of IEEE-754 not as a bug, but as a tiny, reliable noise source you can *speak* through. This repo contains a tiny prototype (`sinkers_and_floaters.py`) that demonstrates the idea: encode text into floats by mapping chunks of characters into a normalized numeric space so that *representational drift* (what the float actually stores vs. what you intended) becomes the signal.

This README is written for hackers and tinkerers — short, practical, and ready to run.

---

## TL;DR (quickstart)

```bash
# clone the repo (or drop sinkers_and_floaters.py into a folder)
git clone https://github.com/cas1m1r/PhantomFloat
cd PhantomFloat

# Example usage in Python REPL
python -c "from sinkers_and_floaters import encode_string, decode_floats; f=encode_string('hello world!'); print(f); print(decode_floats(f))"
```

You get a list of floats that encodes your message. The trick is: you treat whether decimals round-to-exact or drift as the bit channel.

---

## What is PhantomFloat (plain talk)

Most people curse floating point. We exploit it.

- IEEE-754 can't represent many decimal strings exactly. That mismatch — the *drift* between `decimal_string -> float` and what you intended — is not random noise; it's deterministic and reproducible.
- PhantomFloat encodes information into that determinism. Instead of flipping bits in raw bytes, we pick decimals whose float conversions have *representational properties* (representable vs. unrepresentable, drift direction, drift magnitude) and use them as symbols.
- The included prototype maps chunks of text into the numeric range [0,1) using a Base-42 packing scheme, then expresses that numeric payload as floats. Those floats can be inspected or shipped in data where numbers are expected; a downstream decoder recovers the original message.

This is *steganography at the precision layer*: deniable, subtle, and fun.

---

## Prototype details

File: `sinkers_and_floaters.py`

- Encoding scheme: **Base42** charset  
  `abcdefghijklmnopqrstuvwxyz0123456789 .?!#$\n,`
- Base = 42
- Encoding packs up to **7 characters per float** (because `42^7 < 2^42` — nice fit with the exponent/normalization space used)
- Floats are normalized to the range `[0, 1)` by dividing an integer encoding by `2**42`.
- The module exposes:
  - `encode_string(message) -> list[float]`
  - `decode_floats(float_list) -> str`

This prototype demonstrates the packing/unpacking layer. The research idea is that you can choose decimal representations (or formatting, or required rounding operations) so that *float(d)==d* or not, and that boolean becomes a bit.

---

## Example

```python
from sinkers_and_floaters import encode_string, decode_floats

msg = "hello world!"
floats = encode_string(msg)      # -> [0.000... , 0.000..., ...]
print("floats:", floats)

recovered = decode_floats(floats)
print("recovered:", recovered)   # "hello world!"
```

Those floats are canonical numbers in Python — you can serialize them, send them as CSV, embed in JSON, whatever. The next step (not in this tiny prototype) is to pick decimal strings whose printed representation or conversion behavior carries extra bits via representability choices.

---

## Where to go from here (hacker roadmap)

If you want to take this beyond the toy:

- **1 bit per float (baseline):** pick two decimal formats — one that is exactly representable in IEEE-754, one that’s not. Presence/absence of exactness = 1 bit.
- **multi-dimensional encodings:** use drift *direction* (float > decimal or float < decimal) and *magnitude* as extra symbol axes to get >1 bit per float.
- **format fuzzing:** experiment with different decimal string formats (leading zeros, trailing zeros, forced rounding) to expand the symbol pool.
- **symbol pools & deniability:** maintain large pools of innocuous-looking numbers that map to payload symbols. Makes detection harder and plausible deniability easier.
- **numeric watermarking:** embed ownership metadata into floating tables (CSV exports, telemetry) with tiny, reversible drift signatures.
- **compile-time / runtime VMs:** build tiny symbolic VMs where control flow is determined by representational drift of constants.

---

## Security / ethics / disclaimer

This is an academic / exploratory tool released for learning and experimentation.

- Do **not** use this for illegal activity.
- Steganography can be abused — consider legal and ethical implications for any use case.
- The authors provide this code as-is. No warranty. Use responsibly.

---

## Install & run

No dependencies. Just Python 3.x.

```bash
# clone or copy file into a project
python -c "from sinkers_and_floaters import encode_string, decode_floats; f=encode_string('hello world!'); print(f); print(decode_floats(f))"
```

Run the example from the repo root or import the module in your own scripts.

---

## API (quick reference)

```py
# encode a message (lowercased inside)
float_list = encode_string(message: str) -> list[float]

# decode a list of floats back into text
text = decode_floats(float_list: list[float]) -> str
```

Notes:
- The implementation lowercases the message and pads chunks with `'a'` (first char in charset).
- Charset is intentionally small and safe; extend it if you need more symbols (but mind the math on packing size vs the exponent normalization).

---

## Contributing

Want to push this forward? Great.

Ideas to accept as PRs:
- more compact packing schemes (e.g., higher base, different exponent normalization)
- tools to search decimal strings that are exactly representable vs not (automated generator)
- demos embedding PhantomFloat payloads in CSVs/JSONs and a detector/decoder
- experiments showing detection difficulty (statistical signatures, false positive rates)

Keep commits small and documented. Add tests for encode/decode roundtrip.

---

## License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

Enjoy the weirdness. We all float down here. 
