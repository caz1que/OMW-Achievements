# Test your achievements

I highly recommend testing achievements in debug mode. Especially if you want to get them in your playthrough later.

**How to enable debug mode in the OpenMW launcher:**

- Go to "Settings" -> "Debug" -> tick the checkbox "Skip menu and create a default character".
- This will create a new save directory.

<br>

## How to test getting achievement type "single_quest"

1. Open the game console (by default ~).
2. Enter the command `journal "<journalID>" <stage>`, where:
- journalID - key `journalID` from the table of your achievement
- stage - key `stage` from the table of your achievement
3. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "multi_quest"

1. Open the game console (by default ~).
2. The process is the same as in "single_quest", but the 'journal' command must be entered for each quest. The order in which the commands are executed does not matter.
3. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "talkto"

There are two options:
- Find the necessary NPC for the dialogue manually
- Create a new copy of the NPC and place it right in front of the player using the console command: `player->placeatme "<recordId>" 1,1,1 1`, where `recordId` is the value of the `recordId` key from your achievement table

After that, you should start a dialogue with this NPC. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "join_faction"

1. Open the game console (by default ~).
2. Enter the command `PCJoinFaction "<factionId>"`, where `factionId` is the ID of the faction you need to join to get the achievement.
3. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "rank_faction"

1. Open the game console (by default ~).
2. Enter the command `PCJoinFaction "<factionId>"`, where `factionId` is the ID of the faction in which you need to achieve a certain rank to get the achievement.
3. Enter the command `PCRaiseRank "<factionId>"` the required number of times until you reach the rank required to unlock the achievement.
4. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "visit_all"

1. Open the game console (by default ~).
2. Enter the command `coc "<cellId>"`, where `cellId` is one of the ID cells that must be visited to get the achievement.
3. Enter the `coc` command for each cell listed in the cells table.
4. After the player has visited all the listed cells, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "read_all"

1. Open the game console (by default ~).
2. Enter the command `player->additem "<bookId>" 1`, where `<bookId>` is one of the Ids of the books that must be read to get the achievement.
3. Add all the required books to the player's inventory using this command and then read them all.
4. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "equipment"

1. Open the game console (by default ~).
2. Enter the command `player->additem "<itemId>" 1`, where `<itemId>` is the id of one of the items that must be equipped to get the achievement.
3. Add all the required items to the player's inventory using this command and then equip these items to the slots listed in the `equipment` table.
4. If you used a table in the `equipment` table values, you only need to equip one item from that table.
5. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".

<br>

## How to test getting achievement type "equipment"

1. Open the game console (by default ~).
2. Enter the command `set <variable> to <value>`, where `<variable>` is the name of the variable whose `<value>` needs to be reached.
3. If all is well, you will receive a notification that the achievement has been unlocked, and in the achievements widget it will be marked as "unlocked".
