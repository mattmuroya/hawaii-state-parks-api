# Hawaii State Parks API

**Base URL:** `hawaii-state-parks-api.herokuapp.com/api`

[OpenAPI Specification](https://www.openapis.org/) 3.0-compliant RESTful API
that provides name, description, and park activities for each of Hawaii's state
parks, monuments, and recreation areas by island.

_**Note:** Park data and description copy for this API was collected from
[https://dlnr.hawaii.gov/dsp/](https://dlnr.hawaii.gov/dsp/). This API is not
maintained by nor affiliated with the Hawaii DLNR or Division of State Parks in
any way._

[SwaggerUI Demo](https://hawaii-state-parks-api.herokuapp.com/)

## **`GET:`** /parks

Returns a list of parks with park names, IDs, descriptions, activities, location
(island), and a URL to the park's DNLR page. Optionally, you can provide query
parameters to filter results by activities and by island. If you do not provide
any query parameters, the request returns a complete list of all parks data.

### Query Parameters

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Required?</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>activities</code></td>
      <td><code>array[integer]</code></td>
      <td><code>false</code></td>
      <td>A list of activity IDs by which to filter results, separated by commas. The response contains only parks that include at least one of the specified activities.<br /><br /><strong>Example:</strong><br /><br /><code>/parks?activities=1,3,5</code><br /><br /><a href="#activity-ids">List of possible values</a></td>
    </tr>
    <tr>
      <td><code>islands</code></td>
      <td><code>array[integer]</code></td>
      <td><code>false</code></td>
      <td>A list of island IDs by which to filter results, separated by commas. The response contains only parks located on one of the specified islands.<br /><br /><strong>Example:</strong><br /><br /><code>/parks?islands=3,4</code><br /><br /><a href="#island-ids">List of possible values</a></td>
    </tr>
  </tbody>
</table>

### Sample Request

```console
curl -X GET "https://hawaii-state-parks-api.herokuapp.com/api/parks?activities=8,14&islands=2"
```

### Sample Responses

#### `200`: OK

```json
[
  {
    "id": 15,
    "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/kaena-point-state-park/",
    "name": "Kaʻena Point State Park",
    "description": "Ka‘ena Point State Park is a relatively remote and wild coastline park with hiking, picnicking, and shoreline fishing opportunities.  The park wraps around the northwest corner of the island of Oahu and is composed of two sections: the Ka‘ena Point Mokuleia Section (north shore of Oahu) and the Ka‘ena Point Keawa’ula Section (west side of Oahu). Ka‘ena Point State Park is the gateway to Ka‘ena Point Natural Area Reserve at O‘ahu’s most northwestern point.  A large sandy beach at Keawa’ula Bay with board surfing and body surfing for experts and swimming only during calm conditions in the summer; lifeguard services.",
    "activities": ["Beachgoing", "Fishing", "Hiking", "Wildlife Viewing"],
    "island": "Oʻahu"
  },
  {
    "id": 16,
    "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/kaiwi-state-scenic-shoreline/",
    "name": "Kaiwi State Scenic Shoreline",
    "description": "A 1-mile hike (one-way) along a paved roadway leads to a lookout atop a headland above the historic Makapuʻu lighthouse (the lighthouse itself is off-limits, but can be viewed from the trail). At various points along the route there are sweeping views of the southeastern O’ahu coastline, and migrating humpback whales may be visible during whale season. No drinking water or restrooms are available.",
    "activities": [
      "Beachgoing",
      "Dogs on Leash",
      "Fishing",
      "Hiking",
      "Sightseeing",
      "Wildlife Viewing"
    ],
    "island": "Oʻahu"
  }
]
```

<table>
  <thead>
    <tr>
      <th>Response item</th>
      <th>Type</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>id</code></td>
      <td><code>integer</code></td>
      <td>The park ID. Each park has a unique ID value.</td>
    </tr>
    <tr>
      <td><code>url</code></td>
      <td><code>string</code></td>
      <td>The URL for the park page on the Hawaii DLNR website.</td>
    </tr>
    <tr>
      <td><code>name</code></td>
      <td><code>string</code></td>
      <td>The park name.</td>
    </tr>
    <tr>
      <td><code>description</code></td>
      <td><code>string</code></td>
      <td>A brief description of the park from the Hawaii DLNR website.</td>
    </tr>
    <tr>
      <td><code>activities</code></td>
      <td><code>array[string]</code></td>
      <td>An array of activities available at the park.</td>
    </tr>
    <tr>
      <td><code>island</code></td>
      <td><code>string</code></td>
      <td>The name of the island on which the park is located.</td>
    </tr>
  </tbody>
</table>

#### `400`: Invalid query parameters

```json
{
  "error": "Invalid query parameters"
}
```

## **`GET:`** /parks/{parkId}

Returns park name, description, activities, and island for a specific park by
its park ID.

### Path Parameters

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type</th>
      <th>Required?</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>parkId</code></td>
      <td><code>integer</code></td>
      <td><code>true</code></td>
      <td>The ID for the park you want to get.<br /><br /><a href="#park-ids" >List of possible values</a></td></tr>
  </tbody>
</table>

### Sample Request

```console
curl -X GET "https://hawaii-state-parks-api.herokuapp.com/api/parks/28"
```

### Sample Responses

#### `200`: OK

```json
{
  "id": 28,
  "url": "https://dlnr.hawaii.gov/dsp/parks/oahu/waahila-ridge-state-recreation-area/",
  "name": "Waʻahila Ridge State Recreation Area",
  "description": "Wildland picnicking on a Norfolk Island pine forested ridge with fine views of Manoa and Palolo valleys. Enjoy hardy family hiking in the forest reserve.",
  "activities": ["Hiking", "Sightseeing"],
  "island": "Oʻahu"
}
```

<table>
  <thead>
    <tr>
      <th>Response item</th>
      <th>Type</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>id</code></td>
      <td><code>integer</code></td>
      <td>The park ID. Each park has a unique ID value.</td>
    </tr>
    <tr>
      <td><code>url</code></td>
      <td><code>string</code></td>
      <td>The URL for the park page on the Hawaii DLNR website.</td>
    </tr>
    <tr>
      <td><code>name</code></td>
      <td><code>string</code></td>
      <td>The park name.</td>
    </tr>
    <tr>
      <td><code>description</code></td>
      <td><code>string</code></td>
      <td>A brief description of the park from the Hawaii DLNR website.</td>
    </tr>
    <tr>
      <td><code>activities</code></td>
      <td><code>array[string]</code></td>
      <td>An array of activities available at the park.</td>
    </tr>
    <tr>
      <td><code>island</code></td>
      <td><code>string</code></td>
      <td>The name of the island on which the park is located.</td>
    </tr>
  </tbody>
</table>

#### `400`: Invalid park ID

```json
{
  "error": "Invalid park ID"
}
```

#### `404`: Park ID not found

```json
{
  "error": "Park ID not found"
}
```

## **`GET:`** /activities

Returns a list of park activities and their associated activity IDs. No
additional parameters.

### Sample Request

```console
curl -X GET "http://hawaii-state-parks-api.herokuapp.com/api/activities"
```

### Sample Responses

#### `200`: OK

```json
[
  {
    "id": 1,
    "name": "Beachgoing"
  },
  {
    "id": 2,
    "name": "Bicycles"
  },
  ...
]
```

<table>
  <thead>
    <tr>
      <th>Response item</th>
      <th>Type</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>id</code></td>
      <td><code>integer</code></td>
      <td>The activity ID. Each activity has a unique ID value.</td>
    </tr>
    <tr>
      <td><code>name</code></td>
      <td><code>string</code></td>
      <td>The activity name.</td>
    </tr>
  </tbody>
</table>

## **`GET:`** /islands

Returns a list of islands and their associated island IDs. No additional
parameters.

### Sample Request

```console
curl -X GET "http://hawaii-state-parks-api.herokuapp.com/api/islands"
```

### Sample Responses

#### `200`: OK

```json
[
  {
    "id": 1,
    "name": "Kauaʻi"
  },
  {
    "id": 2,
    "name": "Oʻahu"
  },
  ...
]
```

<table>
  <thead>
    <tr>
      <th>Response item</th>
      <th>Type</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>id</code></td>
      <td><code>integer</code></td>
      <td>The island ID. Each island has a unique ID value.</td>
    </tr>
    <tr>
      <td><code>name</code></td>
      <td><code>string</code></td>
      <td>The island name.</td>
    </tr>
  </tbody>
</table>

## Activity IDs

| ID  | Activity         |
| --- | ---------------- |
| 1   | Beachgoing       |
| 2   | Bicycles         |
| 3   | Boat Tours       |
| 4   | Bow Hunting      |
| 5   | Camping          |
| 6   | Dogs on Leash    |
| 7   | Fishing          |
| 8   | Hiking           |
| 9   | Hunting          |
| 10  | Jeep             |
| 11  | Sightseeing      |
| 12  | Snorkeling       |
| 13  | Swimming         |
| 14  | Wildlife Viewing |

## Island IDs

| ID  | Island   |
| --- | -------- |
| 1   | Kauaʻi   |
| 2   | Oʻahu    |
| 3   | Hawaiʻi  |
| 4   | Maui     |
| 5   | Molokaʻi |

## Park IDs

| id  | park                                         |
| --- | -------------------------------------------- |
| 1   | Ahukini State Recreational Pier              |
| 2   | Hāʻena State Park                            |
| 3   | Kōkeʻe State Park                            |
| 4   | Nāpali Coast State Wilderness Park           |
| 5   | Polihale State Park                          |
| 6   | Russian Fort Elizabeth State Historical Park |
| 7   | Wailua River State Park                      |
| 8   | Waimea Canyon State Park                     |
| 9   | Waimea State Recreational Pier               |
| 10  | Ahupuaʻa ʻO Kahana State Park                |
| 11  | ʻAiea Bay State Recreation Area              |
| 12  | Diamond Head State Monument                  |
| 13  | Heʻeia State Park                            |
| 14  | ʻIolani Palace State Monument                |
| 15  | Kaʻena Point State Park                      |
| 16  | Kaiwi State Scenic Shoreline                 |
| 17  | Keaīwa Heiau State Recreation Area           |
| 18  | Ke’ehi Lagoon Memorial State Park            |
| 19  | Lāʻie Point State Wayside                    |
| 20  | Mālaekahana State Recreation Area            |
| 21  | Nuʻuanu Pali State Wayside                   |
| 22  | Puʻu O Mahuka Heiau State Historic Site      |
| 23  | Puʻu ʻUalakaʻa State Wayside                 |
| 24  | Queen Emma Summer Palace                     |
| 25  | Royal Mausoleum State Monument               |
| 26  | Sand Island State Recreation Area            |
| 27  | Ulupō Heiau State Historic Site              |
| 28  | Waʻahila Ridge State Recreation Area         |
| 29  | Wahiawā Freshwater State Recreation Area     |
| 30  | ʻAkaka Falls State Park                      |
| 31  | Hāpuna Beach State Recreation Area           |
| 32  | Huliheʻe Palace                              |
| 33  | Kalōpā State Recreation Area                 |
| 34  | Kealakekua Bay State Historical Park         |
| 35  | Kekaha Kai (Kona Coast) State Park           |
| 36  | Kīholo State Park Reserve                    |
| 37  | Kohala Historical Sites State Monument       |
| 38  | Lapakahi State Historical Park               |
| 39  | Lava Tree State Monument                     |
| 40  | MacKenzie State Recreation Area              |
| 41  | Manukā State Wayside                         |
| 42  | Wailoa River State Recreation Area           |
| 43  | Wailuku River State Park                     |
| 44  | Halekiʻi-Pihana Heiau State Monument         |
| 45  | ʻĪao Valley State Monument                   |
| 46  | Kaumahina State Wayside                      |
| 47  | Mākena State Park                            |
| 48  | Polipoli Spring State Recreation Area        |
| 49  | Puaʻa Kaʻa State Wayside                     |
| 50  | Waiʻānapanapa State Park                     |
| 51  | Wailua Valley State Wayside                  |
| 52  | Pālāʻau State Park                           |
