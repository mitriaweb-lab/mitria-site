#!/usr/bin/env python3
"""
Patches content files with targeted string replacements.
Never replaces whole files. Only modifies specific strings.
"""
import os
import json

def replace_in_file(filepath, old, new, label):
    with open(filepath, 'r') as f:
        content = f.read()
    if old not in content:
        print(f"  ! NOT FOUND in {filepath}: {label}")
        return False
    content = content.replace(old, new, 1)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  + {label}")
    return True

changes = 0

# === #4: Moona → Muna in koh-klang.md ===
print("\n--- #4: Muna/Moona fix ---")
if replace_in_file(
    "src/projects/koh-klang.md",
    "Our friends Mat and Moona",
    "Our friends Mat and Muna",
    "Moona → Muna in koh-klang.md"
):
    changes += 1

# === #17: Profit % in home.json ===
print("\n--- #17: Profit percentage ---")
with open("src/_data/home.json", 'r') as f:
    home = json.load(f)
home["aboutText1"] = home["aboutText1"].replace(
    "almost all of the profit is reinvested into community-led projects",
    "over 80% of our profits are reinvested into community-led projects"
)
with open("src/_data/home.json", 'w') as f:
    json.dump(home, f, indent=2)
print("  + Updated profit % in home.json")
changes += 1

# === #21: EVP description in partners.json ===
print("\n--- #21: EVP description ---")
with open("src/_data/partners.json", 'r') as f:
    partners = json.load(f)
for p in partners["partners"]:
    if p["name"] == "Elephant Valley Project":
        p["description"] = "Hands-off elephant sanctuary in Mondulkiri, Cambodia, providing refuge for rescued elephants since 2006."
        print("  + Rewrote EVP description")
        changes += 1
        break
with open("src/_data/partners.json", 'w') as f:
    json.dump(partners, f, indent=2)

# === #26: Contact form dropdown ===
print("\n--- #26: Contact form dropdown ---")
with open("src/_data/pageSettings.json", 'r') as f:
    ps = json.load(f)
ps["contactFormOptions"] = "Hmong Village Hike & Homestay, Ethical Elephants & Karen Culture, Coastal Conservation & Community Life, Custom Itinerary, Volunteering, School Groups, Projects / Donations, Other"
with open("src/_data/pageSettings.json", 'w') as f:
    json.dump(ps, f, indent=2)
print("  + Updated contact form options")
changes += 1

# === #14: Thailand intro ===
print("\n--- #14: Thailand intro ---")
if replace_in_file(
    "src/countries/thailand.md",
    "Thailand is woven from ancient kingdoms, distinct cultures, and modern rhythms. Monks sweep temple grounds at dawn while bustling streets pulse with urban life. In the rural highlands, the new generations seamlessly blend ethnic traditions with the latest Tik Tok trends. It's almost impossible to step where no tourist has tread before here, but there's also never been a better ability to connect and contribute in positive ways.",
    "Thailand spans ancient temple cities, highland farming communities, and a coastline shaped by fishing and tourism. In the rural north, Karen and Hmong communities maintain distinct cultural practices while navigating the pressures of a rapidly modernizing economy. Overtourism is a real problem here, but meaningful connections are still possible when you know where to look and who to travel with.",
    "Thailand intro rewrite"
):
    changes += 1

# === #15: Cambodia intro ===
print("\n--- #15: Cambodia intro ---")
if replace_in_file(
    "src/countries/cambodia.md",
    "In Cambodia, the sacred and the scarred walk side-by-side. Beneath the grandeur of Angkor's carved faces lies a deeper story of resilience: of farmers rebuilding livelihoods, artists reviving lost dances, and elders telling stories that were once almost silenced. From the rice paddies that stretch through the plains to the jungled hills of Mondulkiri that shelter rare wildlife and indigenous villages, the people here deal with trauma by cracking jokes and purveying a humbleness that borders on deprecation, but don't let the soft smiles fool you. Cambodians wear their history like a scar and a crown.",
    "Cambodia carries the weight of the Khmer Rouge era and the complexities of rapid development, but the people building lives here don't ask to be defined by that history. Farmers in Battambang province grow rice and raise families. Artists in Siem Reap train in classical dance traditions that survived near-extinction. In the forested hills of Mondulkiri, Bunong communities protect ancestral land and the wildlife that depends on it. The humor is sharp, the hospitality is generous, and the stories are told on the storytellers' own terms.",
    "Cambodia intro rewrite"
):
    changes += 1

# === #16: Vietnam intro ===
print("\n--- #16: Vietnam intro ---")
if replace_in_file(
    "src/countries/vietnam.md",
    "Vietnam's story runs like its rivers: winding through dynasties, colonial rule, and hard-fought independence. Rice paddies mirror the sky, and cities hum with a determined energy born from rebuilding and remembering. In the alleys of Hanoi's Old Quarter or the lantern-lit streets of H\u1ed9i An, history is not just preserved; it's lived, layered into the cadence of daily life.\n\nThe highlands are home to ethnic minority groups such as the Hmong, Dao, and Tay, while the coast offers fishing villages, limestone islands, and bustling markets.",
    "Vietnam stretches from the terraced highlands of the north to the river deltas of the south, with 54 recognized ethnic groups, a complex colonial and wartime history, and cities that move at a pace that takes getting used to. We don't currently run experiences or projects in Vietnam, but we're exploring partnerships with community organizations in the northern highlands and central coast. If you're planning travel here, get in touch and we can connect you with organizations doing good work.",
    "Vietnam intro rewrite"
):
    changes += 1

# === #16: Malaysia intro ===
print("\n--- #16: Malaysia intro ---")
if replace_in_file(
    "src/countries/malaysia.md",
    "Malaysia is a meeting place of trade winds, migration routes, and centuries of cultural exchange. Once part of ancient maritime kingdoms and later a prize of colonial powers, it now holds many worlds within one border. In the highland tea fields, on the wooden jetties of fishing villages, and in the call to prayer drifting through tropical rain, Malaysia's history is not locked in museums; it breathes in the everyday.\n\nThe peninsula offers Malay, Chinese, and Indian heritage intertwined, while Borneo's wild interior shelters rare wildlife like orangutans, proboscis monkeys, and pygmy elephants.",
    "Malaysia sits at the crossroads of Malay, Chinese, Indian, and indigenous Orang Asli and Dayak cultures, shaped by centuries of maritime trade and colonial occupation. Borneo's interior holds some of the oldest rainforest on earth, and the communities living there are working to keep it standing. We don't yet have on-the-ground partnerships in Malaysia, but we're building connections with conservation and community organizations in Sabah and Sarawak. Contact us if you're planning travel here and want recommendations.",
    "Malaysia intro rewrite"
):
    changes += 1

# === #18: Rename screenshot images ===
print("\n--- #18: Rename screenshot images ---")
renames = {
    "screenshot-2569-02-13-at-12.11.17\u202fpm.png": "arukharka-monastery.png",
    "screenshot-2569-02-13-at-12.19.14\u202fpm.png": "laos-community-1.png",
    "screenshot-2569-02-13-at-12.19.29\u202fpm.png": "laos-community-2.png",
}
for old_name, new_name in renames.items():
    old_path = os.path.join("src/images", old_name)
    new_path = os.path.join("src/images", new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"  + Renamed {old_name} → {new_name}")
        changes += 1
    else:
        print(f"  ! File not found: {old_name}")

# Update references to renamed images
print("\n--- #18: Update image references ---")
ref_updates = {
    "src/projects/arukharka.md": (
        "screenshot-2569-02-13-at-12.11.17\u202fpm.png",
        "arukharka-monastery.png"
    ),
}
for filepath, (old_ref, new_ref) in ref_updates.items():
    replace_in_file(filepath, old_ref, new_ref, f"Image ref in {filepath}")
    changes += 1

# Laos has two screenshot references
replace_in_file(
    "src/countries/laos.md",
    "screenshot-2569-02-13-at-12.19.14\u202fpm.png",
    "laos-community-1.png",
    "Image ref 1 in laos.md"
)
changes += 1
replace_in_file(
    "src/countries/laos.md",
    "screenshot-2569-02-13-at-12.19.29\u202fpm.png",
    "laos-community-2.png",
    "Image ref 2 in laos.md"
)
changes += 1

print(f"\nDone. {changes} changes applied.")
