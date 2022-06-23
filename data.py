islands = [
    {
        "id": 1,
        "name": "Kauaʻi",
    },
    {
        "id": 2,
        "name": "Oʻahu",
    },
    {
        "id": 3,
        "name": "Hawaiʻi",
    },
    {
        "id": 4,
        "name": "Maui",
    },
    {
        "id": 5,
        "name": "Molokaʻi",
    }
]

activities = [
    {
        "id": 1,
        "name": "Beachgoing"
    },
    {
        "id": 2,
        "name": "Bicycles"
    },
    {
        "id": 3,
        "name": "Boat Tours"
    },
    {
        "id": 4,
        "name": "Bow Hunting"
    },
    {
        "id": 5,
        "name": "Camping"
    },
    {
        "id": 6,
        "name": "Dogs on Leash"
    },
    {
        "id": 7,
        "name": "Fishing"
    },
    {
        "id": 8,
        "name": "Hiking"
    },
    {
        "id": 9,
        "name": "Hunting"
    },
    {
        "id": 10,
        "name": "Jeep"
    },
    {
        "id": 11,
        "name": "Sightseeing"
    },
    {
        "id": 12,
        "name": "Snorkeling"
    },
    {
        "id": 13,
        "name": "Swimming"
    },
    {
        "id": 14,
        "name": "Wildlife Viewing"
    },
]

parks = [

    # KAUAʻI

    {
        "id": 1,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/ahukini-state-recreational-pier/",
        "name": "Ahukini State Recreational Pier",
        "description": "Ahukini Pier is situated at mouth of the Hanamaulu Stream. It consists of a cement pier with a wooden walkway located where the stream meets the Pacific Ocean. Ahukini Pier is an excellent place for pole fishing and crab netting. The site also offers opportunities for viewing the scenery of Hanama’ulu Bay. Hanama’ulu Bay is a State Fishery Management Area (FMA) and therefore strict regulations on spear fishing and net fishing apply to the area.",
        "activities": [7],
        "island": 1
    },
    {
        "id": 2,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/haena-state-park/",
        "name": "Hāʻena State Park",
        "description": "Hā’ena State Park is located at the northwestern extent of Kuhio Highway on Kauai’s north-shore. The park offers viewing of restored lo’i kalo (taro field), as well as the spectacular Nāpali Coast State Wilderness Park.  The park also offers beach-related activities including shore fishing and swimming at Ke’e Beach.  Hā’ena is also home to the trailhead of the world famous Kalalau Trail [11 miles], as well as Hanakāpīʻai Falls trail [4 miles].",
        "activities": [1, 8, 11, 12, 13],
        "island": 1
    },
    {
        "id": 3,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/kokee-state-park/",
        "name": "Kōkeʻe State Park",
        "description": "The park offers commanding views of the lush, amphitheater-headed Kalalau Valley from 4000 feet elevation. Wildland picnicking, tent camping and lodging. Hiking in native rain forest and along rim of Waimea Canyon; additional trails in neighboring forest reserves. Excellent area for observation of native plants, forest birds and insects. Seasonal plum picking and trout fishing. Pig hunting in public hunting area.",
        "activities": [5, 8, 9, 10, 11, 14],
        "island": 1
    },
    {
        "id": 4,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/napali-coast-state-wilderness-park/park-info/",
        "name": "Nāpali Coast State Wilderness Park",
        "description": "The Nāpali Coast is a very special place. The pali, or cliffs, provide a rugged grandeur of deep, narrow valleys ending abruptly at the sea. Waterfalls and swift flowing streams continue to cut these narrow valleys while the sea carves cliffs at their mouths. Extensive stone walled terraces can still be found on the valley bottoms where Hawaiians once lived and cultivated taro.",
        "activities": [3, 4, 5, 8, 9, 11, 14],
        "island": 1
    },
    {
        "id": 5,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/polihale-state-park/",
        "name": "Polihale State Park",
        "description": "Braving a long and rutted dirt road rewards the traveler with a stunning beach park. Picnicking and tent camping on wild coastline with large sand beach backed by dunes. Scenic setting, colorful sunsets and good views of the high sea cliffs of Nāpali Coast. Swimming in summer during calm conditions; shore fishing. Beware of strong, offshore currents. Hot, dry area.",
        "activities": [1, 5, 7, 11, 13],
        "island": 1
    },
    {
        "id": 6,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/russian-fort-elizabeth-state-historical-park/",
        "name": "Russian Fort Elizabeth State Historical Park",
        "description": "The boulder-built fort stands as a reminder of Russia’s short-lived adventure (1815-1817) in the Hawaiian Islands. Massive stacked-stone walls of the fort are a mixture of Hawaiian construction and Russian design. Self-guided walk available.",
        "activities": [11],
        "island": 1
    },
    {
        "id": 7,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/wailua-river-state-park/",
        "name": "Wailua River State Park",
        "description": "Lush river valley with riverboat cruise (fee charged) to Fern Grotto, an unusual fern-covered cave set in a tropical garden; scenic vistas of attractive waterfalls (‘Opaeka‘a Falls and Wailua Falls) and the Wailua River Valley. The Wailua Complex of Heiau (National Historic Landmark)–remains of heiau (places of worship), pu‘uhonua (places of refuge), and birthstones at this once important seat of chiefly power in old Hawaiʻi. Picnicking in riverside coconut grove; and dining and gift shopping at Wailua Marina.",
        "activities": [3, 11],
        "island": 1
    },
    {
        "id": 8,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/waimea-canyon-state-park/",
        "name": "Waimea Canyon State Park",
        "description": "Waimea Canyon State Park overlooks of one of the State’s scenic treasures – the deep, colorful gorge of Waimea Canyon. The park consists of a scenic drive, lookouts of the canyon, a viewpoint of Ni‘ihau Island, wildland picnicking and trails. Adjacent forest reserves with long, strenuous hikes into and out of the canyon. Seasonal trout fishing. Pig and seasonal goat hunting nearby.",
        "activities": [7, 9, 11],
        "island": 1
    },
    {
        "id": 9,
        "url": "https://dlnr.hawaii.gov/dsp/parks/kauai/waimea-state-recreational-pier/",
        "name": "Waimea State Recreational Pier",
        "description": "Ocean Pier fishing and picnicking. Pole fishing (restrictions) and crabbing only.",
        "activities": [7],
        "island": 1
    },

    # OʻAHU

    {
        "id": 10,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/ahupuaa-o-kahana-state-park/",
        "name": "Ahupuaʻa ʻO Kahana State Park",
        "description": "Ahupuaʻa ʻO Kahana State Park is located on the windward side of O’ahu, between Kane’ohe and Laʻie, and 26 miles from Honolulu. Kahana is a relatively unspoiled valley, and one of only a few publicly owned ahupuaʻa (ancient Hawaiian land division) in the state. An ahupuaʻa includes lands from the mountains to the sea (mauka-makai), encompassing all of the resource zones needed for subsistence. The ahupuaʻa of Kahana encompasses almost 5,300 acres, ranging from sea level at Kahana Bay to 2,670 feet at Puʻu Pauao on the crest of the Koʻolau mountains. Kahana is one of the wettest valleys on Oʻahu. Overcast skies and showers are frequent, with an average annual rainfall of 75″ along the coast to 300″ at the back of the valley. Temperatures can range from the mid-60s to the mid-80s.",
        "activities": [1, 5, 6, 7, 8, 9, 11],
        "island": 2
    },
    {
        "id": 11,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/aiea-bay-state-recreation-area/",
        "name": "ʻAiea Bay State Recreation Area",
        "description": "Along the banks of Pearl Harbor’s East Loch, the park offers picnicking opportunities and views of Pearl Harbor and the Arizona Memorial. The Pearl Harbor bike path passes through the park.",
        "activities": [2, 11],
        "island": 2
    },
    {
        "id": 12,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/diamond-head-state-monument/",
        "name": "Diamond Head State Monument",
        "description": "The unique profile of Diamond Head (Lē‘ahi) sits prominently near the eastern edge of Waikiki’s coastline. Hawaii’s most recognized landmark is known for its historic hiking trail, stunning coastal views, and military history. Diamond Head State Monument encompasses over 475 acres, including the interior and outer slopes of the crater. This broad, saucer-shaped crater was formed about 300,000 years ago during a single, explosive eruption that sent ash and fine particles in the air. As these materials settled, they cemented together into a rock called tuff, creating the crater, and which is visible from the trail in the park. Most of the vegetation and birds were introduced in the late 1800s to early 1900s. The trail to the summit of Lē‘ahi was built in 1908 as part of O‘ahu’s coastal defense system. The 0.8 mile hike from trailhead to the summit is steep and strenuous, gaining 560 feet as it ascends from the crater floor. At the summit, you’ll see bunkers and a huge navigational lighthouse built in 1917. The postcard view of the shoreline from Koko Head to Wai‘anae is stunning, and during winter, may include passing humpback whales.",
        "activities": [8, 11],
        "island": 2
    },
    {
        "id": 13,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/heeia-state-park/",
        "name": "Heʻeia State Park",
        "description": "Heʻeia State Park is a coastal site with picnicking and good views of Kaneʻohe Bay and Heʻeia Fishpond. Community programs are available as well as weekend party hall rental.",
        "activities": [11],
        "island": 2
    },
    {
        "id": 14,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/iolani-palace-state-monument/",
        "name": "ʻIolani Palace State Monument",
        "description": "‘Iolani Palace, the official residence of Hawaii’s monarchy, is a marvel of opulence, innovation and political intrigue that tells of a time when their Majesties, King Kalakaua and his sister and successor, Queen Liliuokalani, walked its celebrated halls. Today, you can enjoy one of the most spectacular living restorations in all of Polynesia and immerse yourself in Hawaii’s royal heritage. Officially dedicated in 1882, ‘Iolani Palace served as the setting for the monarchs and their courts on formal occasions. The palace hosts events, offers facility rentals, and has a gift shop. Landscaped grounds are popular for informal lawn picnics and Friday noon band concerts.  ‘Iolani Palace is a National Historic Landmark. The Palace is Administered by the Division of State Parks, but is managed by the Friends of ‘Iolani Palace under a long term lease. For more information, please contact the Friends of ‘Iolani Palace. E-mail: info@iolanipalace.org; Website: www.iolanipalace.org",
        "activities": [11],
        "island": 2
    },
    {
        "id": 15,
        "url": "",
        "name": "Kaʻena Point State Park",
        "description": "Ka‘ena Point State Park is a relatively remote and wild coastline park with hiking, picnicking, and shoreline fishing opportunities.  The park wraps around the northwest corner of the island of Oahu and is composed of two sections: the Ka‘ena Point Mokuleia Section (north shore of Oahu) and the Ka‘ena Point Keawa’ula Section (west side of Oahu). Ka‘ena Point State Park is the gateway to Ka‘ena Point Natural Area Reserve at O‘ahu’s most northwestern point.  A large sandy beach at Keawa’ula Bay with board surfing and body surfing for experts and swimming only during calm conditions in the summer; lifeguard services.",
        "activities": [1, 7, 8, 14],
        "island": 2
    },
    {
        "id": 16,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/kaiwi-state-scenic-shoreline/",
        "name": "Kaiwi State Scenic Shoreline",
        "description": "A 1-mile hike (one-way) along a paved roadway leads to a lookout atop a headland above the historic Makapuʻu lighthouse (the lighthouse itself is off-limits, but can be viewed from the trail). At various points along the route there are sweeping views of the southeastern O’ahu coastline, and migrating humpback whales may be visible during whale season. No drinking water or restrooms are available.",
        "activities": [1, 6, 7, 8, 11, 14],
        "island": 2
    },
    {
        "id": 17,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/keaiwa-heiau-state-recreation-area/",
        "name": "Keaīwa Heiau State Recreation Area",
        "description": "Keaiwa Heiau State Recreation Area is a 384-acre park located approximately 12 miles from Waikiki. Keaïwa Heiau is located at the park entry. Continue along the paved park road to the campgrounds, picnic areas, and trailhead for the ‘Aiea Loop Trail. Groves of Norfolk pines and eucalyptus trees create a forest recreation environment on the hills above the town of ‘Aiea and Pearl Harbor. A resident caretaker near the front gate should be contacted in the event of emergencies.",
        "activities": [8, 11],
        "island": 2
    },
    {
        "id": 18,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/keehi-lagoon-memorial-state-park/",
        "name": "Ke’ehi Lagoon Memorial State Park",
        "description": "Formalized under the Board of Land and Natural Resources, Ke’ehi Lagoon Memorial State Park is now part of the State of Hawaii Department of Land and Natural Resources Division of State Parks system. The park is managed by the Ke’ehi Memorial Organization. For more information please view their website at http://www.keehimemorial.org/.",
        "activities": [],
        "island": 2
    },
    {
        "id": 19,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/laie-point-state-wayside/",
        "name": "Lāʻie Point State Wayside",
        "description": "Scenic views of offshore sea arch, offshore seabird sanctuary, and the windward coast of Oʻahu. Lāʻie Point State Wayside consists of two separate parcels on either side of a dead-end residential street, with no facilities and extremely limited parking. Please respect the neighbors by enjoying this small scenic lookout without blocking driveways or other vehicles. The adjacent undeveloped point is privately owned, please respect.",
        "activities": [7, 11],
        "island": 2
    },
    {
        "id": 20,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/malaekahana-state-recreation-area/",
        "name": "Mālaekahana State Recreation Area",
        "description": "Wooded beach park with swimming, bodysurfing, beach-related activities and shore fishing. Picnicking and camping are available at Kalanai Point section and Kahuku section.",
        "activities": [1, 5, 7, 11, 13],
        "island": 2
    },
    {
        "id": 21,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/nuuanu-pali-state-wayside/",
        "name": "Nuʻuanu Pali State Wayside",
        "description": "Impressive view of windward Oʻahu from brink of pali (cliffs) at 1200 feet elevation in the Ko’olau Range. Winds are usually so strong that one can lean against the wall of wind.",
        "activities": [11],
        "island": 2
    },
    {
        "id": 22,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/puu-o-mahuka-heiau-state-historic-site/",
        "name": "Puʻu O Mahuka Heiau State Historic Site",
        "description": "Puʻu o Mahuka Heiau is the largest heiau (religious site or temple) on Oʻahu, covering almost 2 acres. The name is translated as “hill of escape”. Undoubtedly, this heiau played an important role in the social, political, and religious system of Waimea Valley which was a major occupation center of Oʻahu in the pre-contact period.",
        "activities": [11],
        "island": 2
    },
    {
        "id": 23,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/puu-ualakaa-state-wayside/",
        "name": "Puʻu ʻUalakaʻa State Wayside",
        "description": "Forested area on a cinder cone close to downtown Honolulu. Lookout provides sweeping view of southern O’ahu from Diamond Head to Pearl Harbor, including Honolulu and Manoa Valley. Picnic shelters available. Start of trailhead for ‘Ualaka’a Loop Trail (a 1-mile loop).",
        "activities": [8, 11],
        "island": 2
    },
    {
        "id": 24,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/queen-emma-summer-palace/",
        "name": "Queen Emma Summer Palace",
        "description": "Hānaiakamalama (The Southern Cross), or Queen Emma Summer Palace, served as a summer retreat for Queen Emma of Hawaii from 1857 to 1885, as well as for her husband King Kamehameha IV, and their son, Prince Albert Edward. It is a now a historic landmark, museum, and tourist site preserved by the Daughters of Hawai‘i. Queen Emma Summer Palace was added to the National Register of Historic Places in 1972.",
        "activities": [11],
        "island": 2
    },
    {
        "id": 25,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/royal-mausoleum-state-monument/",
        "name": "Royal Mausoleum State Monument",
        "description": "The Royal Mausoleum State Monument is the burial place of Hawaiian royalty. It includes members of the Kamehameha and Kalakaua Dynasties with their retainers.",
        "activities": [],
        "island": 2
    },
    {
        "id": 26,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/sand-island-state-recreation-area/",
        "name": "Sand Island State Recreation Area",
        "description": "Sand Island State Recreation Area offers weekends-only shoreline camping within a heavily industrialized area very close to the urban core of Honolulu and the flight path of the Honolulu International Airport. This park is also adjacent to the Sand Island Off Highway Vehicle (OHV) day use riding area, which contains tracks and trails for motorized OHV’s and non-motorized BMX bikes. Sand Island is an arid, urban coastal park which offers picnicking, camping, walking, shore fishing and board surfing. It fronts a small sand beach and has good views of Honolulu Harbor and ocean sunsets. (14.0 acres)",
        "activities": [1, 7],
        "island": 2
    },
    {
        "id": 27,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/ulupo-heiau-state-historic-site/",
        "name": "Ulupō Heiau State Historic Site",
        "description": "Ulupō Heiau measures 140 by 180 feet with walls up to 30 feet in height. The construction of this massive terraced platform required a large work force under the direction of a powerful ali’i. Several Oʻahu chiefs lived at Kailua and probably participated in ceremonies at Ulupō Heiau, including Kakuhihewa in the 1400s and Kuali’i in the late 1600s. Kuali’i fought many battles and he may have rededicated Ulupō Heiau as a heiau luakini. Maui chief Kahekili came to Oʻahu in the 1780s and lived in Kailua after defeating Oʻahu high chief Kahahana for control of the island. Kamehameha I worked at Kawai Nui fishpond and is said to have eaten the edible mud (lepo ai ia) of Kawai Nui when there was a shortage of kalo. But by 1795 when Kamehameha I conquered Oʻahu, it is believed that Ulupō Heiau was already abandoned.",
        "activities": [11],
        "island": 2
    },
    {
        "id": 28,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/waahila-ridge-state-recreation-area/",
        "name": "Waʻahila Ridge State Recreation Area",
        "description": "Wildland picnicking on a Norfolk Island pine forested ridge with fine views of Manoa and Palolo valleys. Enjoy hardy family hiking in the forest reserve.",
        "activities": [8, 11],
        "island": 2
    },
    {
        "id": 29,
        "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/wahiawa-freshwater-state-recreation-area/",
        "name": "Wahiawā Freshwater State Recreation Area",
        "description": "Enjoy picnicking along the wooded shore of Wahiawa Reservoir (a.k.a. Lake Wilson). Year-round shore and boat fishing. Check with the State DLNR Division of Aquatic Resources for applicable fishing restrictions. No swimming or water skiing. Boating is only for fishing purposes. Boat ramp at the park.",
        "activities": [7],
        "island": 2
    },

    # HAWAIʻI

    {
        "id": 30,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/akaka-falls-state-park/",
        "name": "ʻAkaka Falls State Park",
        "description": "Pleasant self-guided walk through lush tropical vegetation to scenic vista points overlooking the cascading Kahuna Falls and the free-falling ‘Akaka Falls, which plunges 442 feet into a stream-eroded gorge. The 0.4-mile loop footpath requires some physical exertion. (65.4 acres)",
        "activities": [8, 11],
        "island": 3
    },
    {
        "id": 31,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/hapuna-beach-state-recreation-area/",
        "name": "Hāpuna Beach State Recreation Area",
        "description": "Landscaped beach park with swimming during calm seas, bodysurfing during periods of shore breaks, sunbathing and other beach-related activities, picnicking and shelter lodging opportunities. Dangerous rip currents and pounding shore breaks during periods of high surf! Waves over 3 feet high are for experts – all others should stay out of the water and away from the shoreline! Lifeguard services. Hiking opportunity along the coastal trail. (61.8 acres)",
        "activities": [1, 7, 12, 13],
        "island": 3
    },
    {
        "id": 32,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/hulihee-palace/",
        "name": "Huliheʻe Palace",
        "description": "The Hulihe‘e Palace is located in historic Kailua-Kona, Hawai‘i, on Ali‘i Drive. Once a summer vacation home for Hawaiian royalty, today Hulihe‘e Palace is a museum showcasing Victorian artifacts from the era of King Kalākaua and Queen Kapi‘olani.",
        "activities": [11],
        "island": 3
    },
    {
        "id": 33,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/kalopa-state-recreation-area/",
        "name": "Kalōpā State Recreation Area",
        "description": "Lodging, picnicking and easy family nature hike (0.7-mile loop trail) in a native ‘ohi’a forest at a 2000-foot elevation. Trail passes through the beginnings of an arboretum of the Island’s native plants. Additional trails in the adjoining forest reserve, including a 2-mile horse loop trail. (100.0 acres)",
        "activities": [5, 8],
        "island": 3
    },
    {
        "id": 34,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/kealakekua-bay-state-historical-park/",
        "name": "Kealakekua Bay State Historical Park",
        "description": "Site of the first extensive contact between Hawaiians and Westerners with the arrival of Captain Cook in 1779. Viewing of Hikiau Heiau, a traditional religious site, and the Captain Cook monument at a distance across Kealakekua Bay (4.0 acres).",
        "activities": [3, 11, 12, 14],
        "island": 3
    },
    {
        "id": 35,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/kekaha-kai-kona-coast-state-park/",
        "name": "Kekaha Kai (Kona Coast) State Park",
        "description": "Mahai’ula section has a sandy beach and dune offering opportunities for swimming and beach-related activities. A picnic area with tables is available. A 4.5-mile hike north through this wilderness park on the historic coastal trail, Ala Kahakai, leads to Kua Bay. Midway, a hike to the summit of Pu’u Ku’ili, a 342-foot high cinder cone, offers an excellent view of the coastline. Dry and hot with no drinking water. Maniniʻōwali (Kua Bay) section at north end of park offers swimming during calm seas, bodysurfing during periods of shore breaks, sunbathing, picnicking and other beach-related activities. Hiking opportunity along the coastal trail. Dangerous rip currents and pounding shore breaks during periods of high surf! Waves over 3 feet high are for experts – all others should stay out of the water and away from the shoreline! No lifeguard services.",
        "activities": [1, 7, 8, 11, 12, 13],
        "island": 3
    },
    {
        "id": 36,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/kiholo-state-park-reserve/",
        "name": "Kīholo State Park Reserve",
        "description": "This area is under park reserve status and still undergoing conceptual planning for future public use. The area is a stark, lava-covered coastal park with small bays, sparsely vegetated coastline, historic lava flows, and wide open spaces. Gates are locked nightly. When entrance gates are locked for the night, vehicles will not be able to enter or leave the park.",
        "activities": [1, 5, 7, 8, 11, 12, 13, 14],
        "island": 3
    },
    {
        "id": 37,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/kohala-historical-sites-state-monument/",
        "name": "Kohala Historical Sites State Monument",
        "description": "Viewing of Mo’okini Heiau and Kamehameha I Birthsite. A National Historic Landmark, Mo’okini is one of the most famous luakini heiau (sacrificial temples) on the island. The birthsite is a memorial to Hawaiʻi’s greatest king who united all the island chiefdoms into a kingdom. (6.7 acres)",
        "activities": [11],
        "island": 3
    },
    {
        "id": 38,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/lapakahi-state-historical-park/",
        "name": "Lapakahi State Historical Park",
        "description": "Learn about the tradition Hawaiian lifestyle by taking a self-guided tour through the partially restored remains of this ancient Hawaiian coastal settlement. Nearby ocean waters comprise a marine preserve with various activities regulated. (262.0 acres)",
        "activities": [8, 11],
        "island": 3
    },
    {
        "id": 39,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/lava-tree-state-monument/",
        "name": "Lava Tree State Monument",
        "description": "Viewing of an excellent example of a forest of lava trees along an 0.7 mile loop trail. This unusual volcanic feature is the result of a lava flow that swept through this forested area and left behind lava molds of the tree trunks. Picnicking opportunities. (17.1 acres)",
        "activities": [11],
        "island": 3
    },
    {
        "id": 40,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/mackenzie-state-recreation-area/",
        "name": "MacKenzie State Recreation Area",
        "description": "Low cliffed, wild volcanic coastline with picnicking in an ironwood grove. Good shore fishing. Old Hawaiian coastal trail traverses the park. (13.1 acres)",
        "activities": [7, 11],
        "island": 3
    },
    {
        "id": 41,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/manuka-state-wayside/",
        "name": "Manukā State Wayside",
        "description": "A rest stop with an opportunity to picnic among a collection of native and introduced trees. A 2-mile nature hike through the adjacent Manukā Natural Area Reserve offers an experience in Hawaiian natural history.",
        "activities": [5, 8],
        "island": 3
    },
    {
        "id": 42,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/wailoa-river-state-recreation-area/",
        "name": "Wailoa River State Recreation Area",
        "description": "Pleasure walking, quiet relaxation, informal games and events, picnicking, and boat fishing are provided for in this landscaped park set around Wailoa River. Boat ramp provided. Fishing restrictions. Information services and cultural displays at Wailoa Center which is accessible through Piopio street. (131.9 acres)",
        "activities": [7, 8, 11],
        "island": 3
    },
    {
        "id": 43,
        "url": "https://dlnr.hawaii.gov/dsp/parks/hawaii/wailuku-river-state-park/",
        "name": "Wailuku River State Park",
        "description": "Viewpoints of geologic and scenic interest along Wailuku River. There are two separate park areas. Boiling Pots is a succession of big pools connected by underground flow or cascades and whose waters roll and bubble as if boiling. The exposed hexagonal columns that line the pools were formed by the slow cooling of basalt lava. The 80-foot Rainbow Falls is renowned for the rainbow formed from its mist many mornings. Legends say that the cave beneath the waterfall was the home of Hina, mother of the demigod Maui. (16.3 acres)",
        "activities": [11],
        "island": 3
    },

    # MAUI

    {
        "id": 44,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/halekii-pihana-heiau-state-monument/",
        "name": "Halekiʻi-Pihana Heiau State Monument",
        "description": "Remains of two important heiau (places of worship) that were rededicated as war temples by Kahekili, Maui’s last ruling chief. Viewpoint of Central Maui. (10.2 acres)",
        "activities": [11],
        "island": 4
    },
    {
        "id": 45,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/iao-valley-state-monument/",
        "name": "ʻĪao Valley State Monument",
        "description": "A paved 0.6 mile walk provides a scenic viewpoint of Kuka‘emoku (a.k.a. the ʻIao Needle), an erosional feature which abruptly rises 1200 feet from the valley floor.  Learn about the plants brought by the Hawaiians who settled in ʻIao Valley by taking a short walk through a botanical garden. This valley is rich in cultural and spiritual values and is the site of the battle of Kepaniwai where the forces of Kamehameha I conquered the Maui army in 1790.",
        "activities": [11],
        "island": 4
    },
    {
        "id": 46,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/kaumahina-state-wayside/",
        "name": "Kaumahina State Wayside",
        "description": "Forested rest stop with exotic plants. Picnicking and scenic viewpoint of northeast Maui coastline. No drinking water. (7.8 acres)",
        "activities": [11],
        "island": 4
    },
    {
        "id": 47,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/makena-state-park/",
        "name": "Mākena State Park",
        "description": "Scenic wildland beach park characterized by prominent cinder cone Pu‘u Ola‘i and large white sand beach. Swimming during calm seas, bodysurfing, board surfing, shore fishing, and beach- related activities. No drinking water available. (164.4 acres)",
        "activities": [1, 7, 11, 12, 13],
        "island": 4
    },
    {
        "id": 48,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/polipoli-spring-state-recreation-area/",
        "name": "Polipoli Spring State Recreation Area",
        "description": "Camping and lodging (one cabin) within the fog belt of the Kula Forest Reserve at 6200 foot elevation. Extensive trail system in the forest reserve, including through a forest reminiscent of the conifer forests of the Pacific Northwest coast. Sweeping views of Central and West Maui, Kahoʻolawe, Molokaʻi and Lanaʻi in clear weather. Pig and seasonal bird hunting. Hikers should wear bright colored clothing – hunters may be in the area. Nights are generally cold; winter nights frequently have below freezing temperatures. No campground showers. (10.0 acres). PLEASE NOTE: The Polipoli Cabin cannot be reserved through our online system. Visitors must walk-in or call the Maui District office for reservations.",
        "activities": [5, 8, 9],
        "island": 4
    },
    {
        "id": 49,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/puaa-kaa-state-wayside/",
        "name": "Puaʻa Kaʻa State Wayside",
        "description": "Rest stop and picnicking in the rain forest. An idyllic area with small scenic waterfalls and pools. (5.0 acres)",
        "activities": [11],
        "island": 4
    },
    {
        "id": 50,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/waianapanapa-state-park/",
        "name": "Waiʻānapanapa State Park",
        "description": "Remote, wild, volcanic coastline offering solitude and respite from urban life. Lodging, camping, picnicking, shore fishing and hardy family hiking along an ancient Hawaiian coastal trail which leads to Hana. Excellent opportunity to view a seabird colony and natural stone arch. Other features include native hala forest, heiau (religious temple), sea stacks, blow holes and small black sand beach.",
        "activities": [1, 5, 7, 8, 11, 13],
        "island": 4
    },
    {
        "id": 51,
        "url": "https://dlnr.hawaii.gov/dsp/parks/maui/wailua-valley-state-wayside/",
        "name": "Wailua Valley State Wayside",
        "description": "Viewpoint of Ke‘anae Valley and Ko‘olau Gap in Haleakala’s rim, and of Wailua Village with taro lo‘i fields. (1.5 acres)",
        "activities": [11],
        "island": 4
    },

    # MOLOKAʻI

    {
        "id": 52,
        "url": "https://dlnr.hawaii.gov/dsp/parks/molokai/palaau-state-park/",
        "name": "Pālāʻau State Park",
        "description": "Scenic overview of historic Kalalupapa to which persons with Hansen’s Disease (leprosy) were once banished. Short trail leads to a phallic stone thought to enhance fertility. Picnicking and camping in a ironwood grove. (233.7 acres)",
        "activities": [5, 11],
        "island": 5
    }
]
