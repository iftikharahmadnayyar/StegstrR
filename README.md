# Stegstr R - WhatsApp-Resilient Steganographic Messenger
Built for stegstr.com contest

## What this is
Robust steganography that survives WhatsApp/Telegram/Instagram recompression.
Method: DCT-QIM mid-frequency + Spread Spectrum x16 + Reed-Solomon(255,223)

## Features (Client Requirements)
1. AI Agent Operability: CLI with --json, MCP server, REST API
2. Networking: Nostr relay sync (nostr-sdk), encrypted NIP-04 payloads
3. Invisibility: PSNR >42dB, no visual artifacts
4. Robustness: Survives 5x WhatsApp forwards (q=75, 1600px, EXIF strip)

## Quick Run (No Build)
Prebuilt binaries in /dist (after npm run build)
- Windows: StegstrR.exe
- macOS: StegstrR.dmg
- Linux: StegstrR.AppImage
- CLI: stegstr-cli

## Build from Source
Prereqs: Node 18+, Rust stable
```
npm install
npm run tauri dev
npm run build:win  # or build:mac / build:linux
cd src-tauri && cargo build --release --bin stegstr-cli
```

## CLI Usage (for AI Agents)
./stegstr-cli post "Hello Nostr" --output bundle.json
./stegstr-cli embed cover.png -o stego.png --payload @bundle.json --encrypt --strength high
./stegstr-cli detect stego.png --json
./stegstr-cli detect stego_whatsapp_5x.jpg --json  # still works
./stegstr-cli publish stego.png --relay wss://relay.damus.io
./stegstr-cli subscribe --relay wss://relay.damus.io

## Test WhatsApp Survival
python test_survival.py
# Simulates WhatsApp: JPEG q=75, resize 1600, 5x re-encode

## Links
- Contest: https://www.freelancer.in/contest/stegstr-app-development-contest-2774754
- Reference: https://stegstr.com
- Original: https://github.com/brunkstr/Stegstr
