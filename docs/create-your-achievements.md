# Add and create your achievements

<br>

## Achievement types

To unlock an achievement, a player must meet the required conditions defined by its type. Below are the available types and what conditions they represent:

| Type         | Description                                                                                |
|--------------|--------------------------------------------------------------------------------------------|
| single_quest | Reach a certain stage in the quest.                      |
| multi_quest  | Reach certain stages in several quests.                  |
| talkto       | Start a dialog with a specific NPC (for the first time). |
| join_faction | Join a specific faction.                                 |
| rank_faction | Obtain a certain rank in a faction.                      |
| visit_all    | Visit all the listed cells.                              |
| read_all     | Read all the listed books.                               |
| equipment    | Equip the listed items on the specified equipment slots. |

<br>

## Common keys for all types of achievements

| Key         | Description                                                                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type        | *string* Achievement type. All available achievement types are listed above.                                                                                                             |
| name        | *string* Achievement name. Shown in the widget and notification.                                                                                                                         |
| description | *string* Achievement description. Shown in the widget and notification.                                                                                                                  |
| icon        | *string* The path to the icon file for the achievement. Icon recommendations: file path starts with `Icons\MAC`, .dds format, resolution 64x64 pixels                                    |
| id          | *string* A unique achievement id used to store information about the achievement in storage. Must be different from the id of all other achievements (including Collection achievements) |
| hidden      | *boolean* Whether the achievement is hidden or not. `true` - hidden achievement, `false` - not hidden achievement.                                                                       |
| bgColor      | *string* Color for the background of the achievement icon. The following colors are available: `yellow`, `red`, `blue`, `green`, `aqua`, `purple`. If the key is not used, the default color will be `yellow`.                                                                     |

<br>

## Keys for achievement type “single_quest”

| Key       | Description                                                                                                                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| journalID | *string* Journal ID for the quest that must be completed to get the achievement.                                                                                                                                                                                    |
| stage     | *number* Stage for the quest to be used in the operator.                                                                                                                                                                                                            |
| operator  | *function* A function that contains the condition for getting the achievement. For example, `return givenStage >= self.stage` means that to get the achievement, the player must reach a quest stage that is greater than or equal to the one specified in `stage`. |

<br>

## Keys for achievement type “multi_quest”

| Key       | Description                                                                                                                                                                                                                                                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| journalID | *table* Journal IDs for the quests that must be completed to get the achievement. All values in the table must be of type *string*.                                                                                                                                                                                                                         |
| stage     | *table* Stages for the quests to be used in the operator. All values in the table must be of type *number*.                                                                                                                                                                                                                                                 |
| operator  | *function* A function that contains the condition for getting the achievement. For example, `return currentQuestStageTable[1] >= self.stage[1] and currentQuestStageTable[2] >= self.stage[2]` means that to get the achievement, the player must achieve stages in two quests (from journalID) that are greater than or equal to the values from `stage`. |

<br>

## Keys for achievement type "talkto"

| Key      | Description                                                                           |
|----------|---------------------------------------------------------------------------------------|
| recordId | *string* RecordId of NPC with whom you need to start a dialog to get the achievement. |

<br>

## Keys for achievement type "join_faction"

| Key       | Description                                                                                                                                                                                                                                                                                                        |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| factionId | *string* or *table* FactionID of faction the player must join to get the achievement. If it is necessary to join ONE of the listed factions, the table is used. For example, `factionId = { “telvanni”, “redoran”, “hlaalu” }`, means that the player must join ONE of the listed factions to get the achievement. |

<br>

## Keys for achievement type "rank_faction"

| Key       | Description                                                                                  |
|-----------|----------------------------------------------------------------------------------------------|
| factionId | *string* FactionID of faction in which you must reach a certain rank to get the achievement. |
| rank      | *number* The rank that must be achieved to get the achievement.                              |

<br>

## Keys for achievement type "visit_all"

| Key       | Description                                                                                  |
|-----------|----------------------------------------------------------------------------------------------|
| cells     | *table* A table with cells that all need to be visited to get the achievement.               |

<br>

## Keys for achievement type "read_all"

| Key       | Description                                                                                  |
|-----------|----------------------------------------------------------------------------------------------|
| books     | *table* Table with recordId of books that need to be read to get the achievement.            |

<br>

## Keys for achievement type "equipment"

| Key       | Description                                                                                  |
|-----------|----------------------------------------------------------------------------------------------|
| equipment | *table* A table where the keys are `types.Actor.EQUIPMENT_SLOT` values, and the values ​​are *string* or *table*, denoting the recordId of the items that must be equipped to get the achievement.            |

If *string* is used, then one specific item must be equipped, the recordId of which is specified in the value.

If *table* is used, then one of the items whose recordId is listed in the table must be equipped on specified slot.

For possible equipment slots, see [OpenMW Documentation](https://openmw.readthedocs.io/en/latest/reference/lua-scripting/openmw_types.html##(Actor).EQUIPMENT_SLOT).

<br>

**Example:**

```lua
{
    type = "equipment",
    name = l10n('eq_01_name'),
    description = l10n('eq_01_description'),
    equipment = {
        [slot.Boots] = "daedric_boots",
        [slot.Cuirass] = {"daedric_cuirass", "daedric_cuirass_htab"},
        [slot.Greaves] = {"daedric_greaves", "daedric_greaves_htab"},
        [slot.LeftGauntlet] = "daedric_gauntlet_left",
        [slot.RightGauntlet] = "daedric_gauntlet_right",
        [slot.LeftPauldron] = "daedric_pauldron_left",
        [slot.RightPauldron] = "daedric_pauldron_right",
        [slot.Helmet] = {"daedric_god_helm", "daedric_fountain_helm", "daedric_terrifying_helm"},
        [slot.CarriedLeft] = {"daedric_shield", "daedric_towershield"}
    },
    icon = "Icons\\MAC\\icn_daedricEq.dds",
    bgColor = "blue",
    id = "eq_01",
    hidden = false
},
```

<br>

## How to add your achievements

To add your custom achievement pack, first you need to create a new .lua file at the path: `scripts/omw_achievements/achievements` (since version 2.1.0).

For example, `scripts/omw_achievements/achievements/myAchievementsPack.lua`.

This .lua file should return a table with achievements, where each achievement is a separate table.

Example: 

```lua
local myAchievements = {
    {
        type = "single_quest",
        name = "MyAchievement",
        description = "MyAchievement Description",
        journalID = "quest_journal_id",
        stage = 100,
        operator = function(self, givenStage)
            return givenStage >= self.stage
        end,
        icon = "Icons\\MAC\\icn_my_achievement_icon.dds",
        id = "my_ach_01",
        hidden = false
    }
}

return myAchievements
```

Once you start the game, your achievements will appear at the end of the widget list.

<br>
