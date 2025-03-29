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

## 

First of all, we need to use the `scripts\omw_achievements\achievements\playerAchievements.lua` file.

Initially, it looks like this:

```lua
local playerAchievements = {}

return playerAchievements
```
