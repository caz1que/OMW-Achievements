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

<br>

## Keys for achievement type “single_quest”

First of all, we need to use the `scripts\omw_achievements\achievements\playerAchievements.lua` file.

Initially, it looks like this:

```lua
local playerAchievements = {}

return playerAchievements
```
