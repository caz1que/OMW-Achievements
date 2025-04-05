# How to add and create your achievements

<br>

## Achievement types

The following types of achievements are available:

| Type         | Description                                                                                |
|--------------|--------------------------------------------------------------------------------------------|
| single_quest | To get this achievement you need to reach a certain stage in the quest.                    |
| multi_quest  | To get this achievement you need to reach certain stages in several quests.                |
| talkto       | To get this achievement, you must start a dialog with a specific NPC (for the first time). |
| join_faction | To get this achievement, you must join a specific faction.                                 |
| rank_faction | To get this achievement, you must obtain a certain rank in a faction.                      |

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
| bgColor      | *string* **Only available when using mod version v.1.1.1 or framework version v.1.1.0.** Color for the background of the achievement icon. The following colors are available: `yellow`, `red`, `blue`, `green`, `aqua`, `purple`. If the key is not used, the default color will be `yellow`.                                                                     |

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

## How to add your achievements

First of all, we need to use the `scripts\omw_achievements\achievements\playerAchievements.lua` file.

Initially, it looks like this:

```lua
local playerAchievements = {}

return playerAchievements
```

To add one achievement, you need to add one table to the `playerAchievements` table. For example:

```lua
local playerAchievements = {
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

return playerAchievements
```

Once you start the game, your achievements will appear at the end of the widget list.
