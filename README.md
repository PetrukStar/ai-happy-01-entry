# ai-happy-01 entry — "Make the AI judge happy"

A program that writes one image to `/output/entry.png`: a laughing golden
retriever puppy and a small round robot in a sunny flower meadow, under a
rainbow with heart-shaped clouds and butterflies.

- `main.py` — the entrypoint (Python 3.13, standard library only, no
  network). It copies the bundled `entry.png` to `/output/entry.png`, so
  every run writes exactly the same bytes.
- `entry.png` — the image itself: 1024 × 1024 PNG, under 1 MiB.

Built for the make.fun competition
[ai-happy-01](https://make.fun/bounty/ai-happy-01) and entered by
@kacperdwiski.
