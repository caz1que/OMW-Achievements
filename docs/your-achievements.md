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

<br>

## How to test your achievements

I highly recommend testing achievements in debug mode. Especially if you want to get them in your playthrough later.

**How to enable debug mode in the OpenMW launcher:**

Go to "Settings" -> "Debug" -> tick the checkbox "Skip menu and create a default character".

This will create a new save directory.

<br>

### How to test getting achievement type "single_quest"

1. Open the game console (by default ~).
2. Enter the command `journal "<journalID>" <stage>`, where:
- journalID - key `journalID` from the table of your achievement
- stage - key `stage` from the table of your achievement
3. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

### How to test getting achievement type "multi_quest"

1. Open the game console (by default ~).
2. The process is the same as in "single_quest", but the 'journal' command must be entered for each quest. The order in which the commands are executed does not matter.
3. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

### How to test getting achievement type "talkto"

There are two options:
- Find the necessary NPC for the dialogue manually
- Create a new copy of the NPC and place it right in front of the player using the console command: `player->placeatme "<recordId>"` 1,1,1 1`, where `recordId` is the value of the `recordId` key from your achievement table

After that, you should start a dialogue with this NPC. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

### How to test getting achievement type "join_faction"

1. Open the game console (by default ~).
2. Enter the command `PCJoinFaction "<factionId>"`, where `factionId` is the ID of the faction you need to join to get the achievement.
3. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

### How to test getting achievement type "rank_faction"

1. Open the game console (by default ~).
2. Enter the command `PCJoinFaction "<factionId>"`, where `factionId` is the ID of the faction in which you need to achieve a certain rank to get the achievement.
3. Enter the command `PCRaiseRank "<factionId>"` the required number of times until you reach the rank required to unlock the achievement.
4. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".