# QA: Ch 44. Bit Manipulation — what the chapter covers and how its five sections fit together

Chapter outline being explained:

- 44.1 Bitwise operators, shifts, masks
- 44.2 Set/clear/toggle/check bit; counting set bits; power-of-two checks
- 44.3 XOR tricks, single-number problems
- 44.4 Subset enumeration with bitmasks, Gray code
- 44.5 Bit-parallel algorithms

---

# Part 1. Core concepts and terminology

Before touching any trick, it helps to agree on a small vocabulary. Every later section reuses these words.

## 1.1 Bits, words, and positions

A bit is a single binary digit, 0 or 1. A word is the group of bits a CPU handles in one instruction, usually 32 or 64 bits. Bits are numbered from the right, starting at 0, so bit i carries the value 2^i.

- LSB (least significant bit): bit 0, the rightmost one. It decides odd versus even.
- MSB (most significant bit): the leftmost bit of the word. In signed integers it is the sign bit.
- Set bit: a bit equal to 1. Clear bit: a bit equal to 0.

Take the number 10. In binary it is `1010`, so bits 1 and 3 are set and bits 0 and 2 are clear.

| bit position | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| value of the position | 8 | 4 | 2 | 1 |
| bit of the number 10 | 1 | 0 | 1 | 0 |

Reading it off: 8 + 2 = 10.

## 1.2 Mask

A mask is an integer used as a stencil. Its set bits mark "the positions I care about", and ANDing, ORing, or XORing with it touches only those positions. The mask `1 << i` has exactly one set bit at position i. The mask `(1 << k) - 1` has the k lowest bits set. For k = 4 that is `1111`.

## 1.3 Two's complement

Almost every machine stores signed integers in two's complement. To negate a number, flip all its bits and add 1, so `-x == ~x + 1`. Two consequences matter throughout the chapter:

- `-1` is all ones, which is why `~0` is "every bit set".
- `x & -x` isolates the lowest set bit of x (this is called lowbit, shown in 44.2).

## 1.4 Logical shift versus arithmetic shift

A left shift `x << k` slides bits toward the MSB and fills with zeros. Without overflow it equals x · 2^k.

A right shift `x >> k` slides bits toward the LSB. There are two flavors:

- Logical shift fills the vacated top bits with 0. Unsigned types in C and C++ use it. Java's `>>>` is a logical shift.
- Arithmetic shift copies the sign bit into the vacated top bits, which keeps negative numbers negative. Signed `>>` in Java, and in practice in C and C++, behaves this way.

## 1.5 Other terms used later

| Term | Meaning |
|---|---|
| Popcount / Hamming weight | The number of set bits in a word |
| Hamming distance | The number of positions where two words differ, which equals popcount(a ^ b) |
| Submask | A mask whose set bits are all inside another mask |
| Bitset | A packed array of bits, giving 64 flags per machine word |
| Gray code | An ordering of all n-bit numbers where neighbors differ in exactly one bit |
| SWAR | "SIMD within a register": doing parallel arithmetic on several small fields packed in one ordinary word |
| Bit-parallel | Using one word-wide operation to advance w independent sub-problems at once |

---

# Part 2. Answering the chapter, section by section

## 44.1 Bitwise operators, shifts, masks

### The four operators

Each operator works on every bit position independently, which is the key property. There is no carrying between positions (apart from shifts, which move bits as a group).

| a | b | a & b (AND) | a \| b (OR) | a ^ b (XOR) |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

NOT (`~a`) flips every bit.

A useful way to remember them:

- AND keeps a bit only when both inputs have it. As a mask, it keeps the positions where the mask is 1 and erases the others.
- OR turns a bit on when either input has it. As a mask, it forces mask positions to 1.
- XOR is "differ detector": the result bit is 1 exactly when the inputs differ. As a mask, it flips the positions where the mask is 1.

### A worked example

Let a = 12 (`1100`) and b = 10 (`1010`).

- a & b = `1000` = 8
- a | b = `1110` = 14
- a ^ b = `0110` = 6
- ~a, in 4 bits, is `0011` = 3

### An insight connecting bit operators to ordinary addition

XOR is addition without carries, and AND tells where carries are born. That gives the identity a + b = (a ^ b) + 2 · (a & b). For a = 12 and b = 10: (6) + 2 · 8 = 22 = 12 + 10. Hardware adders and some "add without +" interview problems rest on this.

### Shifts as arithmetic

- `x << k` is x · 2^k (barring overflow).
- `x >> k` is floor(x / 2^k) for non-negative x.
- `x & ((1 << k) - 1)` is x mod 2^k, since it keeps only the low k bits.
- `x >> k & 1` extracts bit k.

### Common language pitfalls

- In C and C++, shifting by an amount greater than or equal to the type's width is undefined behavior. `1 << 31` on a 32-bit signed int is also hazardous. The safe habit is `1ULL << k` when k can reach 63. (Newer C++ draft work adds shift helpers that avoid the undefined behavior; cppreference lists them with a future standard tag, so availability should be checked before relying on them.)
- Python integers have unlimited width, so `~x` equals `-x - 1` and never "wraps". To emulate 32-bit behavior, mask the result: `(~x) & 0xFFFFFFFF`.
- Java has no unsigned int type. It offers `>>>` for logical shifts and `Integer.toUnsignedLong` for conversions.
- Operator precedence in C-family languages trips people up. `x & 1 == 0` parses as `x & (1 == 0)`, so parentheses are needed: `(x & 1) == 0`.

---

## 44.2 Set, clear, toggle, check; counting set bits; power-of-two checks

### The four single-bit operations

Every one of them builds a one-hot mask `1 << i` and then applies a different operator. Start with x = 10 = `1010` and take i = 1 or 3 as shown.

| Operation | Expression | Example | Result |
|---|---|---|---|
| Set bit i | `x \| (1 << i)` | set bit 2: `1010 \| 0100` | `1110` = 14 |
| Clear bit i | `x & ~(1 << i)` | clear bit 3: `1010 & 0111` | `0010` = 2 |
| Toggle bit i | `x ^ (1 << i)` | toggle bit 1: `1010 ^ 0010` | `1000` = 8 |
| Check bit i | `(x >> i) & 1` | check bit 1: `101 & 1` | 1 (set) |

The pattern to remember: OR sets, AND with the complement clears, XOR toggles, shift-then-AND reads.

### Counting set bits

Three approaches, from simple to fast.

Approach A, check every bit. It loops once per bit of the word (32 or 64 times).

```cpp
int popcount_naive(unsigned x) {
    int c = 0;
    for (; x; x >>= 1) c += x & 1;
    return c;
}
```

Approach B, Brian Kernighan's trick. The expression `x & (x - 1)` removes the lowest set bit. The reason: subtracting 1 turns the lowest set bit into 0 and turns every zero below it into 1, so ANDing with the original wipes out exactly that one bit. The loop therefore runs once per set bit, not once per position.

```cpp
int popcount_kernighan(unsigned x) {
    int c = 0;
    for (; x; x &= x - 1) c++;
    return c;
}
```

A trace for x = 44 = `101100`:

1. `101100 & 101011 = 101000` (40), count 1
2. `101000 & 100111 = 100000` (32), count 2
3. `100000 & 011111 = 000000` (0), count 3

So popcount(44) = 3, reached in 3 iterations.

Approach C, SWAR (parallel bit counting from Hacker's Delight). Instead of looping, the word is treated as many small fields and counts are added in parallel, doubling the field width each step.

```cpp
int popcount_swar(uint32_t i) {
    i = i - ((i >> 1) & 0x55555555);                 // counts in 2-bit fields
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333);  // counts in 4-bit fields
    i = (i + (i >> 4)) & 0x0F0F0F0F;                 // counts in 8-bit fields
    return (i * 0x01010101) >> 24;                   // sum the four bytes
}
```

The 64-bit version uses wider constants and a multiplier of `0x0101010101010101` with a shift of 56. Java's `Long.bitCount` is documented in its source as coming from this same Hacker's Delight approach.

### What to use in practice

Modern languages already expose popcount, and on most CPUs it compiles to one hardware instruction (`POPCNT` on x86, `CNT`-style instructions on ARM). Hand-written versions are for learning and for platforms without a builtin.

| Language | Popcount | Other handy calls |
|---|---|---|
| C++20 | `std::popcount(x)` from `<bit>` | `countl_zero`, `countr_zero`, `countl_one`, `countr_one`, `bit_width`, `has_single_bit`, `bit_ceil`, `bit_floor`, `rotl`, `rotr` |
| GCC / Clang | `__builtin_popcount`, `__builtin_popcountll` | `__builtin_clz`, `__builtin_ctz`, `__builtin_parity` |
| Java | `Integer.bitCount`, `Long.bitCount` | `numberOfTrailingZeros`, `highestOneBit`, `BitSet.cardinality` |
| Python 3.10+ | `int.bit_count()` | `int.bit_length()` |
| Rust | `count_ones()` | `leading_zeros()`, `trailing_zeros()` |
| C# (.NET Core 3.0+) | `BitOperations.PopCount` | `LeadingZeroCount`, `TrailingZeroCount` |

One C++ caution: `std::popcount` and the rest of `<bit>` accept only unsigned integer types, so signed values should be cast first.

### Power-of-two checks

A positive power of two has exactly one set bit, for example 8 = `1000`. Applying the Kernighan trick, `x & (x - 1)` removes that single bit and leaves zero. So the test is:

```cpp
bool is_pow2(unsigned long long x) { return x != 0 && (x & (x - 1)) == 0; }
```

The `x != 0` guard is needed because 0 & (0 − 1) is also 0 but 0 is not a power of two. In C++20, `std::has_single_bit(x)` does the same job.

Checks: 8 → `1000 & 0111 = 0` (power of two). 6 → `110 & 101 = 100` (not).

Related helpers:

- Round up to the next power of two: `std::bit_ceil(x)`. Round down: `std::bit_floor(x)`.
- Number of bits needed to store x: `std::bit_width(x)`.
- Index of the highest set bit: `bit_width(x) - 1`.

### Lowbit: isolating the lowest set bit

The expression `x & -x` returns only the lowest set bit. Using two's complement, -x = ~x + 1. Everything above the lowest set bit is flipped by the NOT, the lowest set bit survives, and everything below it is zero in both. So AND keeps just that bit.

Example with x = 12 = `1100` in 4 bits: ~x = `0011`, so -x = `0100`, and `1100 & 0100 = 0100` = 4.

This is the operation behind Fenwick trees (binary indexed trees), which move between nodes by adding or subtracting lowbit.

---

## 44.3 XOR tricks and single-number problems

### The four properties that power everything

1. a ^ a = 0 (anything cancels itself)
2. a ^ 0 = a (zero is the identity)
3. a ^ b = b ^ a (commutative)
4. (a ^ b) ^ c = a ^ (b ^ c) (associative)

Because of the last two, the order in which a list is XORed never matters. Because of the first two, any value appearing an even number of times drops out, and what remains is the XOR of the values appearing an odd number of times.

### Example 1: the classic single number

In an array where every value appears twice except one, XOR everything.

```cpp
int single(const vector<int>& a) {
    int r = 0;
    for (int v : a) r ^= v;
    return r;
}
```

Take [4, 1, 2, 1, 2]. The running XOR is 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1 ^ 1) ^ (2 ^ 2) = 4. It uses O(n) time and O(1) extra space.

### Example 2: two singles, everything else in pairs

XORing everything gives x = a ^ b, where a and b are the two unique values. Since a ≠ b, x is nonzero, so it has at least one set bit. That bit is a position where a and b differ. Taking lowbit(x) picks one such position.

Steps:

1. Compute x = XOR of the whole array (this equals a ^ b).
2. Compute `low = x & -x` (use a wider type to avoid overflow if x could be the minimum int).
3. Split the array into two groups: elements with `(v & low) != 0` and elements with `(v & low) == 0`.
4. XOR each group separately. a lands in one group and b in the other, and every duplicate pair stays together in one group, so each group's XOR is exactly one of the singles.

Connections as a list: whole array → x = a ^ b → lowbit → partition by that bit → two independent single-number problems.

### Example 3: every value appears three times except one

XOR alone no longer cancels, since a ^ a ^ a = a. Two accumulators can count each bit position modulo 3:

```cpp
int single_of_three(const vector<int>& a) {
    int ones = 0, twos = 0;
    for (int v : a) {
        ones = (ones ^ v) & ~twos;
        twos = (twos ^ v) & ~ones;
    }
    return ones;
}
```

Think of `(twos, ones)` as a two-bit counter per position that cycles 00 → 01 → 10 → 00. After three appearances it resets, so only the unique value's bits remain in `ones`.

### Example 4: missing number

Given n distinct numbers from 0..n, one is missing. XOR all indices 0..n with all array values. Pairs cancel and the missing value remains.

### Example 5: prefix XOR for range queries

Define P[0] = 0 and P[i+1] = P[i] ^ a[i]. Then the XOR of a[l..r] is P[r+1] ^ P[l], because the shared prefix cancels. This lets any range-XOR query run in O(1) after O(n) preprocessing, and it is the XOR analogue of prefix sums.

### Example 6: Hamming distance

popcount(a ^ b) counts the positions where a and b differ. For 5 (`101`) and 3 (`011`): 5 ^ 3 = `110`, popcount 2, so the distance is 2.

### Example 7: swap without a temporary

```cpp
a ^= b; b ^= a; a ^= b;
```

Tracing a = A, b = B: after the first step a = A^B; then b = B ^ (A^B) = A; then a = (A^B) ^ A = B. It is a classic curiosity. Compilers do not benefit from it, and it breaks when both names refer to the same memory location (the value becomes 0), so `std::swap` is the practical choice.

---

## 44.4 Subset enumeration with bitmasks, and Gray code

### The core idea: a subset is an integer

For a set of n elements, bit i of a mask says whether element i is in the subset. The integers 0 through 2^n − 1 therefore represent all 2^n subsets exactly once.

For n = 3 with elements {a, b, c} (bit 0 = a, bit 1 = b, bit 2 = c):

| mask | binary | subset |
|---|---|---|
| 0 | 000 | {} |
| 1 | 001 | {a} |
| 2 | 010 | {b} |
| 3 | 011 | {a, b} |
| 4 | 100 | {c} |
| 5 | 101 | {a, c} |
| 6 | 110 | {b, c} |
| 7 | 111 | {a, b, c} |

Enumerating every subset is a one-line loop. Typical uses are brute-force over subsets and "does any subset sum to k".

```cpp
for (int mask = 0; mask < (1 << n); mask++) {
    long long sum = 0;
    for (int i = 0; i < n; i++)
        if (mask >> i & 1) sum += a[i];
    // use sum
}
```

This costs O(2^n · n). Because 2^n grows fast, it is practical roughly up to n of about 20 to 22.

### Enumerating the submasks of one mask

Given a mask m, the goal is to list only the submasks s of m (all bits of s lie inside m). The loop is:

```cpp
for (int s = m; s; s = (s - 1) & m) {
    // use s  (note: s = 0 is skipped)
}
// handle s = 0 separately if the empty submask is needed
```

Why it works, as a short chain of steps:

1. Subtracting 1 from s clears its lowest set bit and sets all the bits below it.
2. Those lower bits may include positions outside m, so they must go.
3. ANDing with m removes the outsiders and yields the next smaller submask.

Worked trace for m = 11 = `1011`, which has 3 set bits and so 2^3 = 8 submasks:

`1011` → `1010` → `1001` → `1000` → `0011` → `0010` → `0001` → (`0000`)

Checking one step: from `1000`, subtract 1 to get `0111`, AND with `1011` to get `0011`. The jump from `1000` straight to `0011` skips the invalid `0111` because bit 2 is not in m.

### Why total cost over all masks is 3^n

Suppose the work is the sum, over every mask m, of the number of its submasks. A mask with k set bits has 2^k submasks, so the sum is the sum over k of C(n, k) · 2^k, which the binomial theorem collapses to (1 + 2)^n = 3^n.

An intuitive version: for each of the n bit positions, the pair (m, s) has exactly three options for that bit.

1. The bit is not in m (so it is not in s either).
2. The bit is in m but not in s.
3. The bit is in both m and s.

Three choices per bit across n bits gives 3^n pairs. This bound is what makes submask-based DP feasible for n up to about 15 to 18.

### Gray code

A Gray code orders all n-bit numbers so that consecutive entries differ in exactly one bit. The i-th Gray code is computed by:

```cpp
unsigned gray(unsigned i) { return i ^ (i >> 1); }
```

For n = 3:

| i | binary of i | gray(i) |
|---|---|---|
| 0 | 000 | 000 |
| 1 | 001 | 001 |
| 2 | 010 | 011 |
| 3 | 011 | 010 |
| 4 | 100 | 110 |
| 5 | 101 | 111 |
| 6 | 110 | 101 |
| 7 | 111 | 100 |

Going from step i − 1 to step i, the bit that flips is the position of the lowest set bit of i, which is `ctz(i)` (count trailing zeros). Check: i = 4 has ctz = 2, and 010 → 110 flips bit 2.

Why bother? When each subset differs from the previous one by a single element, a running quantity can be updated with one addition or subtraction instead of being recomputed from scratch. That drops the subset-sum enumeration from O(2^n · n) to O(2^n):

```cpp
long long cur = 0;
int prev = 0;
for (int i = 1; i < (1 << n); i++) {
    int g = i ^ (i >> 1);
    int bit = __builtin_ctz(i);        // which element changed
    if (g >> bit & 1) cur += a[bit];   // element entered
    else              cur -= a[bit];   // element left
    // cur is the sum of subset g
}
```

Other places Gray codes appear: Karnaugh maps, rotary encoders (so that a half-turn read never jumps by more than one bit), and minimal-change generation of combinatorial objects.

---

## 44.5 Bit-parallel algorithms

### The idea

A 64-bit word holds 64 independent yes/no facts. One AND, OR, or shift therefore updates 64 of them at the cost of a single instruction. When a problem can be phrased as "do the same simple thing to many small states", packing those states into words can cut the running time by a factor of the word size w (typically 64, or 256 or 512 with vector instructions).

### Example 1: subset-sum with a bitset

Question: can some subset of the numbers a₁…aₙ sum to S?

Let `dp[j]` be 1 when sum j is reachable. Reachable sums after adding a number a are the old reachable sums, plus the old ones shifted up by a. In bitset form that is a single line:

```cpp
bitset<10001> dp;
dp[0] = 1;
for (int a : nums) dp |= dp << a;
// dp[S] tells whether sum S is reachable
```

Cost is O(n · S / w) rather than O(n · S). With S = 10^5 and w = 64, the word-level work is roughly 64 times smaller.

### Example 2: reachability and transitive closure

Store each row of a graph's adjacency matrix as a bitset. In Warshall's algorithm, the inner loop "if i reaches k, then i also reaches everything k reaches" becomes `row[i] |= row[k]`, processing w columns at a time. The total is O(n³ / w) instead of O(n³).

### Example 3: Shift-And string matching

Pattern of length m ≤ 64. For each character c, a mask `B[c]` marks the pattern positions where c occurs. A state word `D` has bit j set when the first j + 1 pattern characters match the text suffix just read.

Steps, per text character c:

1. Shift the state up by one and set bit 0, since a new match can always begin: `D = (D << 1) | 1`.
2. Keep only the positions whose pattern character equals c: `D &= B[c]`.
3. If bit m − 1 of `D` is set, the whole pattern ends at this position.

Trace with pattern `aba` (B['a'] = `101`, B['b'] = `010`) on text `ababa`:

| text char | D after update (bits 2..0) | match? |
|---|---|---|
| a | `001` | no |
| b | `010` | no |
| a | `101` | yes, ends at index 2 |
| b | `010` | no |
| a | `101` | yes, ends at index 4 |

All m partial matches advance in one step per text character, so the whole scan is O(n) for short patterns. The idea extends to approximate matching: Myers' bit-vector algorithm computes edit distance this way, in roughly O(n · m / w).

### Example 4: bitboards

Chess engines store each piece type as a 64-bit integer, with one bit per square. Moves for entire sets of pieces are generated by shifts and masks. For instance, shifting a pawn bitboard left by 8 pushes all pawns one rank forward in one operation, and ANDing with the empty-squares bitboard filters out blocked moves.

### Example 5: SWAR and SIMD

The SWAR popcount in 44.2 is a small bit-parallel algorithm: four byte-sized counters are added at once inside one 32-bit register. SIMD instructions (SSE, AVX2, AVX-512, NEON) apply the same principle with wider registers. AVX-512 even includes vector popcount instructions for 8, 16, 32, and 64-bit lanes.

---

# Part 3. Quick-reference sheet

| Goal | Expression |
|---|---|
| Check bit i | `(x >> i) & 1` |
| Set / clear / toggle bit i | `x \| 1<<i`, `x & ~(1<<i)`, `x ^ 1<<i` |
| Lowest set bit | `x & -x` |
| Remove lowest set bit | `x & (x-1)` |
| Low k bits mask | `(1<<k) - 1` |
| Is power of two | `x && !(x & (x-1))` |
| Popcount | `std::popcount(x)` or `x.bit_count()` in Python |
| Highest set bit index | `bit_width(x) - 1` |
| Next submask of m after s | `(s-1) & m` |
| i-th Gray code | `i ^ (i>>1)` |
| Hamming distance | `popcount(a ^ b)` |
| Range XOR | `P[r+1] ^ P[l]` |

---

# Part 4. Gap check on the chapter outline (items to decide on)

The outline was compared against what standard sources consistently pair with this topic: C++ `<bit>` and compiler builtins, CP-Algorithms (submask enumeration), competitive-programming bit-trick collections, and algorithm handbooks. These topics appear regularly in those sources but have no section in Ch 44 as currently written. Nothing has been merged or dropped; they are listed so they can be added as visible sections if wanted.

| # | Missing topic | Why it matters |
|---|---|---|
| 1 | Integer representation: two's complement, signed overflow, signed versus unsigned shifts, undefined behavior | The foundation for lowbit, `~x`, and every language pitfall in 44.1 |
| 2 | Lowbit and the Fenwick tree link | `x & -x` is currently only a side note in 44.2 |
| 3 | Bit reversal, rotation, byte swap, endianness, parity | Appear in `<bit>` (rotl, rotr, byteswap, endian) and in hashing and networking |
| 4 | Bitmask DP (TSP, Hamiltonian path, assignment problems) | The most common use of 44.4's subset enumeration |
| 5 | SOS DP (sum over subsets) and XOR/Walsh–Hadamard transforms | Standard advanced follow-up to submask enumeration |
| 6 | XOR trie, maximum XOR pair | Standard XOR application listed next to single-number problems |
| 7 | Gosper's hack (iterate over all masks with exactly k bits set) | The usual way to enumerate k-subsets |
| 8 | Bits as arithmetic: multiply/divide/mod by powers of two, branchless min, max, abs, sign tests | Frequently listed in bit-trick references |
| 9 | Per-bit reasoning problems (range AND, bitwise sum splitting, minimum flips) | A common interview and contest pattern |
| 10 | Bitset as a data structure; bit-packed arrays; Bloom filters; bitboards | Partly in 44.5, but not as an organized topic |
| 11 | Hardware intrinsics and builtins (clz, ctz, popcnt, parity) | Used throughout but not taught as a unit |
| 12 | Nim and XOR (nim-sum, Sprague–Grundy) | A famous XOR application outside array problems |

Open question for the chapter author: which of these 12 should be added as their own visible sections, and in which position within Ch 44?