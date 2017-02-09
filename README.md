# Mechamicus
A Discord bot with dice rolling, chat logging, and other utility functions.
                    
## Functions
| Command | Functionality |
|---------|---------------|
|**Utility**|
|echo|Responds 'Echo!', a good way to test connectivity|
|repeat|Responds with whatever follows the command|
|deck|Manages a deck of cards, sub-commands are available by typing '/deck'|
|choose|Randomly selects between comma-separated values that follow the command|
|quote|Manages a collection of saved messages, sub-commands are available by typing '/quote'|
|**Traditional Gaming**|
|pfsrd|Searches the Pathfinder System Reference Document (www.d20pfsrd.com) for terms that follow the command|
|nethys|Searches the Archives of Nethys (www.archivesofnethys.com) for terms that follow the command|
|roll|*May be implicitly called.* Rolls dice using the patterns '(num)d(num)', '(+/-)(num)d(num)', and '(+/-)(num)'|