# README.md

# Samsung Ex‑Link TV Integration for Home Assistant

Control Samsung televisions over **RS‑232C (Ex‑Link)** using an Ethernet‑to‑Serial bridge (e.g. StarTech NETRS2321P).

---

## Features

| Feature                | Supported |
| ---------------------- | --------- |
| Power on/off           | ✅        |
| Volume up/down         | ✅        |
| Mute toggle            | ✅        |
| HDMI source select 1‑4 | ✅        |
| Media Player entity    | ✅        |

> ℹ️ Additional Ex‑Link commands can easily be added in `samsungtv.py`.

---

## Requirements

- Home Assistant **2024.5** or newer
- An Ethernet‑to‑RS‑232 adapter (tested with **StarTech NETRS2321P**)
- Samsung TV model with a **3.5 mm Ex‑Link / RS‑232C** service port
- Proper serial cable/adapter (3.5 mm TRS ⟷ DB‑9 to your bridge)

---

## Installation

1. Copy the `samsung_exlink` folder into `config/custom_components/`.
2. Restart Home Assistant.
3. In the UI: **Settings → Devices & Services → + Add Integration** → search for **Samsung Ex‑Link TV**.
4. Enter:
   - **Name** – Friendly name for the TV entity.
   - **Host** – IP address of your Ethernet‑to‑Serial bridge.
   - **Port** – TCP port (default `23`).

---

## Configuration Options

No YAML needed! All configuration is handled via the UI. To change settings later, open the integration in **Devices & Services** and choose **Configure**.

---

## Services

This integration relies on built‑in Media Player services (`media_player.turn_on`, `media_player.volume_up`, etc.). If you add custom commands to `SamsungExLinkTV`, expose them via Home Assistant [Button](https://www.home-assistant.io/integrations/button/) or [Select](https://www.home-assistant.io/integrations/select/) entities.

---

## Extending the Integration

1. **Add commands**: Implement a new method in `samsungtv.py` that calls `_send()` with the correct byte sequence.
2. **Expose as service**: Wrap the new method in an entity service or button helper.

PRs are welcome! Follow the [Home Assistant developer docs](https://developers.home-assistant.io/) and maintain `black`/`isort` formatting.

---

## Troubleshooting

- **Cannot connect** – Verify the bridge IP/port and that the TV’s Ex‑Link feature is enabled (some models require Service Menu).
- **No response** – Check serial wiring (tip = TX, ring = RX, sleeve = GND) and baud (default 9600 8‑N‑1).
- **Firewall** – Ensure Home Assistant can reach the bridge IP/port.
