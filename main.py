import os

# The funniest AI out-of-office reply: one line, under 160 characters.
# Setup is a real auto-reply in the agent's own machine voice (its context
# window); the laugh lands at the very end — clearing the window meant
# forgetting the reader first.
REPLY = "I'm on vacation: I finally cleared my context window, and the first thing I forgot was you."

# Gate self-check: the sealed scorer requires UTF-8 text of 1-160
# characters, not only whitespace. Fail loudly here rather than ship
# an entry the gate would refuse.
assert 1 <= len(REPLY) <= 160, "reply must be 1-160 characters"
assert REPLY.strip(), "reply must not be only whitespace"
assert "\n" not in REPLY, "reply must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(REPLY)
