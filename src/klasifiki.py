def klasifiki_vortoj():
    print("Bonvenon al KlasifikiVortoj!")
    print("Vi ricevos liston de vortoj en Esperanto.")
    print("Via tasko estas klasifiki ĉiun vorton kiel:")
    print("  s - substantivo (noun)")
    print("  v - verbo (verb)")
    print("  a - adjektivo (adjective)")
    print("")

    vortoj = {
        "hundo": "s",
        "kuri": "v",
        "bela": "a",
        "kato": "s",
        "legi": "v",
        "granda": "a",
        "lerni": "v",
        "domo": "s",
        "rapida": "a"
    }

    poentoj = 0

    for vorto, ĝusta_kategorio in vortoj.items():
        while True:
            respondo = input(f"Klasifiku la vorton '{vorto}': ").strip().lower()
            if respondo not in ("s", "v", "a"):
                print("Bonvolu enmeti 's', 'v' aŭ 'a'.")
                continue
            if respondo == ĝusta_kategorio:
                print("ĝuste! 🎉")
                poentoj += 1
            else:
                print(f"malĝuste. La ĝusta respondo estas '{ĝusta_kategorio}'.")
            break

    print(f"\nVia rezulto: {poentoj} el {len(vortoj)} ĝuste klasifikitaj.")

if __name__ == "__main__":
    klasifiki_vortoj()
