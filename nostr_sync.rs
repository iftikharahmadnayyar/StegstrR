
// src-tauri/src/nostr_sync.rs - Nostr relay sync using nostr-sdk
// Cargo.toml: nostr-sdk = "0.32"
use nostr_sdk::prelude::*;
pub async fn publish_image_event(payload: String, relay: &str) -> Result<String> {
    let keys = Keys::generate();
    let client = Client::new(&keys);
    client.add_relay(relay).await?;
    client.connect().await;
    let event = EventBuilder::text_note(payload, []).to_event(&keys)?;
    client.send_event(event.clone()).await?;
    Ok(event.id.to_hex())
}
