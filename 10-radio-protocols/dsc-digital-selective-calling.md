# DSC — Digital Selective Calling

- **Category:** Radio protocols
- **Style:** DO–CONFIRM
- **When to use:** Reference for using DSC on a fixed VHF/DSC set.
- **Equipment:** DSC-capable VHF with a **registered MMSI** and GPS input.

> Killer items are shown in **bold**.

## Setup prerequisites
- [ ] **MMSI programmed into the radio and registered** with the authority
- [ ] **GPS connected** to the radio (so distress calls carry position)
- [ ] Crew briefed on where the DSC distress button is and how it works

## Sending a DSC distress alert
1. [ ] **Lift the spring-loaded cover over the red DISTRESS button**
2. [ ] For a designated alert: select the nature of distress (if time allows)
3. [ ] **Press and hold the button (~5 seconds) until it transmits**
4. [ ] The radio auto-tunes to Ch 16 — **follow up with a voice MAYDAY**
5. [ ] Await acknowledgement; the alert repeats until acknowledged

## Individual / routine DSC call
- [ ] Enter the other station's MMSI (or select from directory)
- [ ] Choose the working channel to propose
- [ ] Send; when acknowledged, both sets switch to the working channel for voice

## Cancelling an accidental DSC distress
- [ ] **Do NOT just switch off** — cancel it properly
- [ ] Reset the alert on the set, then transmit a voice cancellation on Ch 16:
```
ALL STATIONS x3, THIS IS <boat name x3> <MMSI/callsign>
CANCEL MY DISTRESS ALERT OF <time> UTC. <boat name>. OUT
```

## Notes & gotchas
- A DSC distress sends your **identity and GPS position** digitally in seconds —
  it's the fastest, most reliable way to raise the alarm; use it first, then voice.
- No GPS input = no position in the alert; **verify GPS is connected**.
- Accidental alerts happen — always cancel them; never leave one unaddressed.
