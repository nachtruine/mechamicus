# Mechamicus
A Discord bot with dice rolling, SRD referencing, and other utility functions.
                    
## Functions
| Command | Functionality |
|---------|---------------|
|**Utility**|
|echo|Responds 'Echo!', a good way to test connectivity|
|repeat|Responds with whatever follows the command|
|deck|Manages a deck of cards, sub-commands are available by typing '/deck help'|
|choose|Randomly selects between comma-separated values that follow the command|
|quote|Manages a collection of saved messages, sub-commands are available by typing '/quote'|
|eightball|Responds with a random selection of positive, neutral, and negative answers. May also be called with '/8ball'|
|remember|Stores and retrieves information stored with a keyword|
|**Traditional Gaming**|
|pfsrd|Searches the Pathfinder System Reference Document (www.d20pfsrd.com) for terms that follow the command|
|nethys|Searches the Archives of Nethys (www.archivesofnethys.com) for terms that follow the command|
|roll|*May be implicitly called.* Rolls dice using the patterns '(num)d(num)', '(+/-)(num)d(num)', and '(+/-)(num)'|
